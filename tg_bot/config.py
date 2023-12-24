from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 5332414680   # my telegram ID
    OWNER_USERNAME = "Armaan512"  # my telegram username
    API_KEY = "6536934928:AAGz2-ARFY6CkU8MD1kcWccbu7TWAV9TZLw"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://kvbtopvx:rn5dFC0Q9FYOrf9koHbpEaPu9HFuA4cz@cornelius.db.elephantsql.com/kvbtopvx'  # sample db credentials
    MESSAGE_DUMP = '-1001932566732' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1103636187, 6260714402]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
