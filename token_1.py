import random
import pathlib
import pandas as pd
import shutil
import time
import sys
import pyinotify
# from pyinotify import IN_MODIFY
import os
class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        if event.pathname == os.getcwd() + "/NODE1/encrypted_file.txt":
            print("Encryption activity detected on file: %s" % event.pathname)

wm = pyinotify.WatchManager()
# mask = 

handler = MyEventHandler()
notifier = pyinotify.Notifier(wm, handler)

wm.add_watch(os.getcwd() + "/NODE1/encrypted_file.txt", 0x00000002, rec=False)

notifier.loop()
# token = map(str, sys.argv[1:])
# token = list(token)
# print(token)


