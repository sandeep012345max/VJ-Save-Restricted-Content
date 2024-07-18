import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6170943113:AAFBbv_Ndl7RXPp-oGUhOomScCUUbB-AjAE")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22428240"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "844cef4b1899c4b2dd8a482e4b5e2835")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://greatravish2007:RoMTp5JNjMQtYjVb@cluster0.riexzpb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
