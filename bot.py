import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0")

API_ID = int(os.environ.get("API_ID", "3335796"))

API_HASH = os.environ.get("API_HASH", "138b992a0e672e8346d8439c3f42ea78")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
