#!/usr/bin/env python3

# A simple chat client for matrix.
# This sample will allow you to connect to a room, and send/recieve messages.
# Args: host:port username room
# Error Codes:
# 1 - Unknown problem has occured
# 2 - Could not find the server.
# 3 - Bad URL Format.
# 4 - Bad username/password.
# 11 - Wrong room format.
# 12 - Couldn't find room.

from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema

from getpass import getpass

import sys

# Called when a message is recieved.
def on_message(event):
    if event['type'] == "m.room.member":
        if event['membership'] == "join":
            print("{0} joined".format(event['content']['displayname']))
    elif event['type'] == "m.room.message":
        if event['content']['msgtype'] == "m.text":
            print("{0}: {1}".format(event['sender'],event['content']['body']))
    else:
        print(event['type'])

host = "";
username = "";
room = "";

if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = input("Host (ex: http://localhost:8008 ): ")

client = MatrixClient(host)

if len(sys.argv) > 2:
    username = sys.argv[2]
else:
    username = input("Username: ")

password = getpass() #Hide user input

try:
    client.login_with_password(username,password)
except MatrixRequestError as e:
    if e.code == 403:
        print("Bad username or password.")
        sys.exit(4)
    else:
        print("Check your sever details are correct.")
        sys.exit(3)
    print(e)

except MissingSchema as e:
    print("Bad URL format.")
    print(e)
    sys.exit(2)


room = None

if len(sys.argv) > 3:
    room = sys.argv[3]
else:
    room = input("Room ID/Alias: ")

try:
    room = client.join_room(room)
except MatrixRequestError as e:
    if e.code == 400:
        print("Room ID/Alias in the wrong format")
        sys.exit(11)
    else:
        print("Couldn't find room.")
        sys.exit(12)

room.add_listener(on_message)
client.start_listener_thread()


shouldRun = True
while shouldRun:
    msg = input()
    if msg == "/quit":
        shouldRun = False
    else:
        room.send_text(msg)
