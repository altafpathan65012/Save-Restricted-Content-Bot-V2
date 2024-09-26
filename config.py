# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23031620"))
API_HASH = getenv("API_HASH", "31cb00c1cbe580394778b43105864bca")
BOT_TOKEN = getenv("BOT_TOKEN", "7286824722:AAGvvSK-ydnLhi-GPnHjv2U5rpX2ff_Ew4U")
OWNER_ID = list(map(int, getenv("OWNER_ID", "502980590").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002155787742")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002415828562"))
