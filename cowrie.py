#!/usr/bin/python

import os
import time
import json
import socket
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from difflib import Differ

json_file = './var/log/cowrie/cowrie.json'
HOST = '192.168.206.133'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_content = 0

    def on_modified(self, event):
        if not event.is_directory and event.src_path=='./var/log/cowrie/cowrie.json':
            with open(event.src_path, "r") as f:
                i = 0
                for line in f:
                    i = i + 1
                    print(i)
                    if i > self.last_content:
                        self.last_content = i
                        try:
                            element = json.loads(line)
                            if element['eventid'] == 'cowrie.command.input':
                                print(element['input'])
                                s.send(element['input'].encode())
                                print("Send Command : ", element['input'])
                        except ValueError as e:
                            print('error')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='./var/log/cowrie/', recursive=False)
    observer.start()

    print('File monitor started')

    try:
        while True:
            time.sleep(100) #sleep seconds
    except KeyboardInterrupt:
        observer.stop()
    observer.join()