# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", "34446649"))
    API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8369915876:AAH9wJ1yOotFTjdTrRzJlW2u480QNOoP9SQ")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1003475522251"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "7892805795"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/IDNCoderXRoot"
    TG_MAX_SIZE = 2040108421
