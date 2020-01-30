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
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
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
  if data['name'].lower() == "jason everett":
		n = random()
			if n<=0.25:
				send_msg("cork it, space trash")
			elif n<=0.5:
				send_msg("the moon landing is fake and so is your personality")
			elif n<=0.75:
				send_msg("hey. hey jason. quiet.")
			else:
				send_msg("jason your face is the visual equivalent of the f-word")
		elif data['text'].lower() == "!test":
			send_msg("all set boss")



	
	
	

  return "ok", 200

