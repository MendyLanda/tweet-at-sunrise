# tweet-on-sunrise

This project is a simple Twitter bot that tweets a message at sunrise in a specified city.

## Requirements

*   Python 3.6+
*   The following Python packages:
    *   pytz
    *   tweepy
    *   astral

## Setup

1.  Clone or download the project files.
2.  Create a virtual environment for the project and install the necessary packages. You can use the following commands to create a virtual environment and install the necessary packages:
        `python3 -m venv venv`
        `source venv/bin/activate`
        `pip install -r requirements.txt`
3.  Create a new Twitter app at [https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
4.  Generate the necessary API keys and access tokens for your app.
5.  Rename the `config_template.yml` file to `config.yml` and fill in the necessary values with your API keys and access tokens.
6.  Set the city you want the sunrise time for in the `config.yml` file. A list of supported cities can be found at [https://sffjunkie.github.io/astral/#cities](https://sffjunkie.github.io/astral/#cities).
7.  Set the content of your tweet in the `config.yml` file. You can use placeholders (e.g. `{1}`, `{2}`, etc.) in your tweet content to insert dynamic values.
8.  If you want to use placeholders in your tweet content, edit the `placeholders` list in the `tweet_parameters.py` file with the values you want to use.
9.  Run the `main.py` file to start the bot.

## Customization

You can customize the following parameters in the `config.yml` file:

*   `consumerKey`: Your Twitter API consumer key (also known as the API key).
*   `consumerSecret`: Your Twitter API consumer secret (also known as the API secret key).
*   `accessToken`: Your Twitter API access token.
*   `accessTokenSecret`: Your Twitter API access token secret.
*   `city`: The city you want the sunrise time for. A list of supported cities can be found at [https://sffjunkie.github.io/astral/#cities](https://sffjunkie.github.io/astral/#cities).
*   `tweetContent`: The content of your tweet. You can use placeholders (e.g. `{1}`, `{2}`, etc.) in your tweet content to insert dynamic values.

If you want to use placeholders in your tweet content, you can customize the `placeholders` list in the `tweet_parameters.py` file with the values you want to use to replace the placeholders.

## Troubleshooting

*   Make sure you filled in the necessary values in the `config.yml` file.
*   If you get an error message saying that the `config.yml` file is missing, make sure you renamed the `config_template.yml` file to `config.yml`.
*   If you get an error 403 when trying to access the Twitter API, make sure you filled in the correct API keys and access tokens in the `config.yml` file. and that you have **write access** to the Twitter account you are trying to tweet from.
## Acknowledgements

*   The [astral](https://github.com/sffjunkie/astral) library was used to calculate the sunrise time.
*   The [pytz](https://github.com/newvem/pytz) library was used to handle time zones.
*   The [tweepy](https://github.com/tweepy/tweepy) library was used to access the Twitter API.

## License
MIT License

to get all installed packages in your virtual environment run: pip freeze > requirements.txt