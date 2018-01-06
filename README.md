# Community Chatbot Musings

## Problem: How do we automate instructions using chatbots? 

Can we automate form registration using a chatbot and is it useful for public events?
Can we automate canvanizer results to store the data in some central database and is this more efficient than sending a pic of the canvanizer?

## Solution -- attempt

Let's try various channels and determine what can be used best for
non-techincal users.

- [x] Telegram
--    Good and easy setup so far.
- [] Slack
- [] Google Assistant

### Usage

Developing: 

0. Use conda or pip to install the requirements.
1. Add your API token to telegram using the handy sh file: `source setup.sh`
    - Otherwise, you can just add the export to your terminal
2. Create a Postgres database and add basic params. For example, I am using `database.ini` with `setup.sql` as my test databases.
3. Run the bot with `python comchatter_boy.py`

Current Test Bot:

1. Add @comchatter_bot to Telegram. TODO: need to deploy somewhere else.
2. Try "/register" or "/info"




