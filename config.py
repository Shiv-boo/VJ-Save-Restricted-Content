import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21678417"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed58f7fa0568567f72b3e973db446876")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://akshayverma903626:<db_password>@cluster0.7mibe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
