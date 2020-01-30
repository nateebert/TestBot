#imports
import os
import sys
import json
import requests
from flask import Flask, request
from random import random

#define our flask app
app = Flask(__name__)

#logging function to help debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()

#Sends a message to the chat that the bot originates from
def send_msg(msg):

  url  = 'https://api.groupme.com/v3/bots/post'
  
  data ={
  'bot_id' : os.getenv(55362208),
  'text'   : msg
  }
        
  request = requests.post(url=url, data=data)

#Method will automatically execute when our endpoint receives a POST call
@app.route('/', methods=['POST'])
def msg_received_from_group():
  #Format the data we receive as a JSON
  data = request.get_json()
  log('{}'.format(data))
  
  #Check the text of the message sent to the chat to see if it matches our command word
  if data['name'].lower() == "nate ebert" or data['user_id'] == '40743743':
    n = random()
    if n<=0.25:
      send_msg("stfu you bitch")
    elif n<=0.5:
      send_msg("go to hell skank")
    elif n<=0.75:
      send_msg("eat shit and die")
    else:
      send_msg("go. fuck. yourself.")



	
	
	

  return "ok", 200

