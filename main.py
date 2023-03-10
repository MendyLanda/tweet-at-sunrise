import yaml
import datetime
import time
import pytz
import schedule
import tweepy

from astral.sun import sun
from astral.geocoder import database, lookup

from tweet_parameters import placeholders


def get_next_sunrise(city: str):
    """Returns the next sunrise time for the specified city as a UTC datetime object."""
    # get a LocationInfo object for the specified city
    try:
        city = lookup(city, database())
    except KeyError:
        raise ValueError(
            f"City '{city}' not found in the database. For a list of valid cities, see https://sffjunkie.github.io/astral/#cities"
        )

    # if its between 12am and 12pm, get the sunrise for today, otherwise get the sunrise for tomorrow
    if datetime.datetime.now().hour < 12:
        sunrise_date = datetime.date.today()
    else:
        sunrise_date = datetime.date.today() + datetime.timedelta(days=1)

    return sun(city.observer, date=sunrise_date, tzinfo=pytz.utc).get("sunrise")


def tweet(api, tweet_content):
    # tweet the message
    try:
        api.update_status(tweet_content)
        print(f"Tweeted: {tweet_content} at {datetime.datetime.now()}")
    except Exception as e:
        print(f"Error: {e}")


def convert_utc_to_local(utc_datetime: datetime.datetime):
    """Converts a UTC datetime object to a system local datetime object."""
    return utc_datetime.astimezone(pytz.timezone(time.tzname[0]))


def is_sunrise(city: str):
    """Returns True if it is currently sunrise in the specified city, otherwise returns False."""
    # get the next sunrise time for the specified city
    sun = get_next_sunrise(city)
    # get the local time for the next sunrise time for the specified city
    l_sun = convert_utc_to_local(sun)

    l_time = datetime.datetime.now()
    return l_sun.hour == l_time.hour and l_sun.minute == l_time.minute


def fill_tweet_placeholder(tweet_content: str, *values: str):
    """Replaces the placeholders in the tweet content with the specified values (if any)."""
    # if no values are passed, return the tweet content as is
    if len(values) == 0:
        return tweet_content
    # loop through the values and replace the placeholders with the values
    for i, value in enumerate(values):
        tweet_content = tweet_content.replace(f"{{{i+1}}}", str(value))
    return tweet_content


def tweet_and_reschedual(api, tweet_content, city):
    tweet(api, tweet_content)
    next_sunrize = convert_utc_to_local(get_next_sunrise(city))
    schedule.every().day.at(f"{next_sunrize.strftime('%H:%M')}").do(
        tweet_and_reschedual, api, tweet_content, city
    )


def main():
    # read the config data from the config.yaml file. this is a yaml file because it's easier to read and write than a json file
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # create an API client using the Twitter API keys and tokens from the config
    auth = tweepy.OAuthHandler(config["consumerKey"], config["consumerSecret"])
    auth.set_access_token(config["accessToken"], config["accessTokenSecret"])
    api = tweepy.API(auth)

    next_sunrize = convert_utc_to_local(get_next_sunrise(config["city"]))
    schedule.every().day.at(f"{next_sunrize.strftime('%H:%M')}").do(
        tweet_and_reschedual,
        api,
        fill_tweet_placeholder(config["tweetContent"], *placeholders),
        config["city"],
    )

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
