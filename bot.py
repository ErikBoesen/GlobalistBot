import os
import requests
import mebots

from flask import Flask, request

from website import Website

app = Flask(__name__)
bot = mebots.Bot('your_bot_shortname_here', os.env['BOT_TOKEN'])
website = Website()

PREFIX = '$'


# Endpoint
@app.route('/', methods=['POST'])
def receive():
    print('Incoming message:')
    print(data)

    # Prevent self-reply
    if data['sender_type'] != 'bot':
        if data['text'].startswith(PREFIX):
            args = data['text'].lstrip(PREFIX).split()
            command = args.pop(0)
            query = ' '.join(args)
            if command == 'search':
                send(website.search(query))

    return 'ok', 200


def send(message, group_id):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': bot.instance(group_id).id,
        'text': message,
    }
    r = requests.post(url, data=data)
