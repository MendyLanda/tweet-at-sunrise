########################### TWEET PARAMETERS ###########################
# Only need to change the values in this file                          #
# if your tweet content has placeholders (e.g. {1}, {2}, etc.)         #
# fill the placeholders in the tweet content with the specified values #
########################################################################

################################## EXAMPLE ##################################
# If the tweet content is "Hello {1}! It is currently {2} in {3}." and the  #
# values are "World", "sunny", and "New York", the tweet content will be    #
# "Hello World! It is currently sunny in New York."                         #
#############################################################################

# dont change the variable name "placeholders" you can edit anything else
# values are strings or convertiable (e.g. "Hello World!" or e.g. datetime.now())
from datetime import datetime  # just an example

placeholders = [
    datetime.now().year,  # just an example
]
