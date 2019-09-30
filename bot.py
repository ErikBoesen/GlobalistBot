import os
import requests
import mebots

from flask import Flask, request

from website import Website

app = Flask(__name__)
bot = mebots.Bot('your_bot_shortname_here', os.environ.get('BOT_TOKEN'))
website = Website()

PREFIX = '$'


# Endpoint
@app.route('/', methods=['POST'])
def receive():
    message = request.get_json()
    group_id = message["group_id"]
    print(message)

    # Prevent self-reply
    if message['sender_type'] != 'bot':
        if message['text'].startswith(PREFIX):
            args = message['text'].lstrip(PREFIX).split()
            command = args.pop(0)
            query = ' '.join(args)
            if command == 'search':
                send(website.search(query), group_id)

    return 'ok', 200


def send(text, group_id):
    url  = 'https://api.groupme.com/v3/bots/post'

    message = {
        'bot_id': bot.instance(group_id).id,
        'text': text,
    }
    r = requests.post(url, data=message)
