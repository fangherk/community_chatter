"""
   comchatter_bot.py
  
   Program to receive basic sign-up information from students.  

   Stores the follwing info to a csv:
        1. First Name
        2. Last Name 
        3. Email
        4. Mobile Number
        5. Grade Level
        6. Teacher Name
"""
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import os, logging


# Enable basic logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Variables for Bot Setup
API_TOKEN = os.environ["comchatter"]

# States
NAME_FIRST, NAME_LAST, EMAIL, MOBILE, GRADE, NAME_TEACHER, DONE, END = range(8)
REPLY, STEPS = 98, 99

# Counter
counter= 0 
labels = ["first", "last", "email", "mobile", "grade", "teacher"]
output = {}


reply_keyboard = [["Begin"]]
next_keyboard = [["Next"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
next_markup = ReplyKeyboardMarkup(next_keyboard, one_time_keyboard=True)

###################################################################################
def register(bot, update):
    update.message.reply_text(
        "Welcome to registration! I will ask a few questions to get your basic information. "
        "Let's get started!")
    
    update.message.reply_text("What is your FIRST name?")
    return NAME_FIRST

def name_first(bot, update, user_data):
    """ Get the user's first name """
    text = update.message.text
    bounce(text)
    update.message.reply_text("What is your LAST name?")
    return counter


def name_last(bot, update, user_data):
    """ Get the user's last name """
    text = update.message.text
    bounce(text)
    update.message.reply_text("What is your email?")
    return counter


def email(bot, update, user_data):
    """ Get the user's email """
    text = update.message.text
    bounce(text)
    update.message.reply_text("What is your mobile?")
    return counter


def mobile(bot, update, user_data):
    """ Get the user's mobile number """
    text = update.message.text
    bounce(text)
    update.message.reply_text("What is your grade?")
    return counter


def grade(bot, update, user_data):
    """ Get the user's grade"""
    text = update.message.text
    bounce(text)
    update.message.reply_text("What is the name of your teacher?")
    return counter

def name_teacher(bot, update, user_data):
    """ Get the user's teacher  """
    text = update.message.text
    update.message.reply_text("Thank You for registering!")
    bounce(text)
    return counter

def bounce(text):
    global counter
    output[labels[counter]] = text
    counter = counter % 8
    counter += 1

def received_info(bot, update, user_data):
    text = update.message.text
    # update.message.reply_text("Nice, you gave me {} so far".format(text), reply_markup=next_markup)
    update.message.reply_text("Nice, you gave me {} so far".format(text))
    global counter
    output[labels[counter]] = text
    counter += 1
    print(counter)
    return counter
 

def error(bot, update, error):
    """ Log basic errors """
    logger.warning('Update "%s" caused error "%s"', update, error)
    

def done(bot, update, user_data):
    user_data.clear()
    return ConversationHandler.END

###################################################################################
def main():
    # Create an event handler and pass it the bot's token.
    updater = Updater(API_TOKEN)

    # Use a dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with states
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('register', register)],

        states={
            REPLY: [MessageHandler(Filters.text,
                                   received_info,
                                   pass_user_data=True),
            ],
            NAME_FIRST: [MessageHandler(Filters.text,
                                        name_first,
                                        pass_user_data = True),
            ],
            NAME_LAST: [MessageHandler(Filters.text,
                                        name_last,
                                        pass_user_data = True),
            ],
            EMAIL: [MessageHandler(Filters.text,
                                        email,
                                        pass_user_data = True),
            ],
            MOBILE: [MessageHandler(Filters.text,
                                        mobile,
                                        pass_user_data = True),
            ],
            GRADE: [MessageHandler(Filters.text,
                                        grade,
                                        pass_user_data = True),
            ],
            NAME_TEACHER: [MessageHandler(Filters.text,
                                        name_teacher,
                                        pass_user_data = True),
            ],
            DONE: [MessageHandler(Filters.text,
                                        done,
                                        pass_user_data = True),
            ],
        },

        fallbacks=[RegexHandler('^$', done, pass_user_data=True)]
    )

    dispatcher.add_handler(conv_handler)

    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
