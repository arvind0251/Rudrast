from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 21552265))
API_HASH = getenv("API_HASH", 1c971ae7e62cc416ca977e040e700d09)

BOT_TOKEN = getenv("BOT_TOKEN", 7133864474:AAFe2hkW6Xts85GLK9ZbQQdrRiHrtiNqbgM)
MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://bikash:bikash@bikash.3jkvhp7.mongodb.net/?retryWrites=true&w=majority)

OWNER_ID = int(getenv("OWNER_ID", 7408008545))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+ekvvqYVRa6c0YmI1")
