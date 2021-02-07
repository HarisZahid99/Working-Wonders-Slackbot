import slack
import os
import random
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
  os.environ['SIGNING_SECRET'], '/slack/events',app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID  = client.api_call("auth.test")['user_id']

#SETTING UP GAMES FEATURE
@app.route('/game-help', methods=['POST'])
def game_help():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="*Here's a list of commands to access the games you can play! :slightly_smiling_face:*:\n>:pencil2:`/game-skribbl`: To play skribble online\n>:chess_pawn:`/game-chess`: To play chess online\n>:jigsaw:`/game-codenames`: To play codenames online\n>:people_holding_hands:`/game-uno`: To play UNO online\n>:game_die:`/game-monopoly`: To play a COVID-19 version of monopoly online")
  return Response(), 200

@app.route('/game-skribbl', methods=['POST'])
def game_skribbl():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="https://skribbl.io/")
  return Response(), 200

@app.route('/game-chess', methods=['POST'])
def game_chess():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="https://www.chess.com/play/computer")
  return Response(), 200

@app.route('/game-codenames', methods=['POST'])
def game_codenames():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="https://codenames.game/")
  return Response(), 200

@app.route('/game-uno', methods=['POST'])
def game_uno():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="https://www.letsplayuno.com/")
  return Response(), 200

@app.route('/game-monopoly', methods=['POST'])
def game_monopoly():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="https://www.covidopoly.io/")
  return Response(), 200

#SETTING UP VIRTUAL ESCAPE FEATURE
@app.route('/virtual-escape', methods=['POST'])
def virtual_escape():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  num = random.randint(0,3)

  if num==0:
    image_url = "https://scontent.fykz1-2.fna.fbcdn.net/v/t1.15752-9/147414100_721242725259623_6626121967961489710_n.jpg?_nc_cat=109&ccb=2&_nc_sid=ae9488&_nc_ohc=MmdNStE4r5QAX_wIOk8&_nc_ht=scontent.fykz1-2.fna&oh=491a630cbbd0a6fcbadef69b470f09e6&oe=6043E5BD"
    attachments = [{"title": "", "image_url": image_url}]
    client.chat_postMessage(channel=channel_id, text="*Enjoy a virtual escape for a short break with a colleague!*:palm_tree:\nYou can discuss some amazing pieces of art, have nice coversations while staring\n at the Eiffel Tower, or enjoy some peace and quiet while sharing a view!\n`Take out your camera and scan the QR code`"
    ,attachments=attachments)
    return Response(), 200
  elif num==1:
    image_url = "https://scontent.fykz1-1.fna.fbcdn.net/v/t1.15752-9/147229699_794419434614973_2823874976672882709_n.png?_nc_cat=100&ccb=2&_nc_sid=ae9488&_nc_ohc=FiRd4R7OHOQAX_tJ_DH&_nc_ht=scontent.fykz1-1.fna&oh=e378bd164468918f4374c18b759fa0e7&oe=604552B0"
    attachments = [{"title": "", "image_url": image_url}]
    client.chat_postMessage(channel=channel_id, text="*Enjoy a virtual escape for a short break with a colleague!*:palm_tree:\nYou can discuss some amazing pieces of art, have nice coversations while staring\n at the Eiffel Tower, or enjoy some peace and quiet while sharing a view!\n`Take out your camera and scan the QR code`"
    ,attachments=attachments)
    return Response(), 200
  elif num==2:
    image_url = "https://scontent.fykz1-2.fna.fbcdn.net/v/t1.15752-9/147780110_421175092452174_5778537366714801516_n.png?_nc_cat=101&ccb=2&_nc_sid=ae9488&_nc_ohc=W5Xy5OaAE2wAX9wrCWN&_nc_ht=scontent.fykz1-2.fna&oh=eb76ad925639927b8b479da61bdf022d&oe=6046C79A"
    attachments = [{"title": "", "image_url": image_url}]
    client.chat_postMessage(channel=channel_id, text="*Enjoy a virtual escape for a short break with a colleague!*:palm_tree:\nYou can discuss some amazing pieces of art, have nice coversations while staring\n at the Eiffel Tower, or enjoy some peace and quiet while sharing a view!\n`Take out your camera and scan the QR code`"
    ,attachments=attachments)
    return Response(), 200

#SETTING UP MEMES FEATURE
@app.route('/memes', methods=['POST'])
def memes():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  num2 = random.randint(0,3)

  if num2==0:
    image_url = "https://scontent.fykz1-1.fna.fbcdn.net/v/t1.15752-9/138184556_691364454839524_8246955282551550151_n.jpg?_nc_cat=106&ccb=2&_nc_sid=ae9488&_nc_ohc=Zl-ElvkCvJsAX9XUKep&_nc_ht=scontent.fykz1-1.fna&oh=c3abf0e9f75356b426a8821ad146a8a5&oe=6020C93C"
    attachments = [{"title": "", "image_url": image_url}]
    client.chat_postMessage(channel=channel_id, text="",attachments=attachments)
    return Response(), 200
  elif num2==1:
    image_url = "https://scontent.fykz1-2.fna.fbcdn.net/v/t1.15752-9/138318225_1809168312572978_6671121374801948714_n.jpg?_nc_cat=111&ccb=2&_nc_sid=ae9488&_nc_ohc=bSO1Kb1WdTUAX8alPZg&_nc_ht=scontent.fykz1-2.fna&oh=35554bbd4671a61efb04ac9119dd4da1&oe=60209954"
    attachments = [{"title": "", "image_url": image_url}]
    client.chat_postMessage(channel=channel_id, text="",attachments=attachments)
    return Response(), 200
  elif num2==2:
    image_url = "https://scontent.fykz1-1.fna.fbcdn.net/v/t1.15752-9/141506587_419849155880575_1679078364976179459_n.jpg?_nc_cat=103&ccb=2&_nc_sid=ae9488&_nc_ohc=JUdgIASlLfgAX-GF_xJ&_nc_oc=AQm3F1mJXyxsbn_rnG6PcA0is56WMOxwwidv3fJRfHpvD96zYKHG-BWycipdFOuaGxy83rU4Olxih57bAq8c5O-8&_nc_ht=scontent.fykz1-1.fna&oh=89614aa0b527b5dab1da3ec5c99b8238&oe=6020D6D8"
    attachments = [{"title": "", "image_url": image_url}]
    client.chat_postMessage(channel=channel_id, text="",attachments=attachments)   
    return Response(), 200

#SETTING UP SCHEDULED MESSAGES (BIRTHDAY AND MYSTERY)
SCHEDULED_MESSAGES1 = [
  {'text': ':thinking_face:This months thought provoking mystery. How did she survive?:thinking_face::thinking_face:*\n *:heavy_dollar_sign:Answer correctly for a chance to win a 10$ Amazon gift card.:heavy_dollar_sign: \n\n Two girls order iced tea with free refills. One girl drinks four glasses in the time it takes the other to drink just one. The girl who drank the single glass dies, but the other lives. All the drinks were poisoned. How did the girl who drank the most iced tea survive?', 'post_at':(datetime.now()+timedelta(seconds=30)).timestamp(), 'channel':'C01M5H2HZ0D'},
]

image_url = "https://www.kidscanfly.ca/wp-content/uploads/2020/08/happy-birthday.jpeg"

attachments = [{"title": "Happy Birthday", "image_url": image_url}]

SCHEDULED_MESSAGES2 = [
  {'text': ':tada:*HAPPY BIRTHDAY ISHA!!!!!*:cake::balloon:\n', 'post_at':(datetime.now()+timedelta(seconds=45)).timestamp(), 'channel':'C01M5H2HZ0D', 'attachments': attachments},
]

ids =[]
def schedule_messages1(messages):
  for msg in messages:
    response = client.chat_scheduleMessage(channel=msg['channel'], text=msg['text'], post_at=msg['post_at'])
    id_ = response.get('id')
    ids.append(id_)
    return ids

def schedule_messages2(messages):
  for msg in messages:
    response = client.chat_scheduleMessage(channel=msg['channel'], text=msg['text'], post_at=msg['post_at'], attachments=msg['attachments'])
    id_ = response.get('id')
    ids.append(id_)
    return ids

#SETTING UP HELP FEATURE
@app.route('/help', methods=['POST'])
def help():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="*Use the following commands for help using the bot!*\n> `/help` :To get help\n> `/game-help` :To display a variety of virtual lunchtime games\n> `/memes` :For a short laugh\n> `/virtual-escape` :Allows user to see art, monuments, museums, etc through augmented reality \n> `/mystery` :Displays the Mystery of the Month")
  return Response(), 200

#SETTING UP MYSTERY FEATURE
@app.route('/mystery', methods=['POST'])
def mystery():
  data = request.form
  user_id = data.get('user_id')
  channel_id = data.get('channel_id')
  client.chat_postMessage(channel=channel_id, text="*Here is the Mystery of the Month*\n`Two girls order iced tea with free refills. One girl drinks four glasses in the time it takes the other to drink just one. The girl who drank the single glass dies, but the other lives. All the drinks were poisoned. How did the girl who drank the most iced tea survive?`")
  return Response(), 200

if __name__ == "__main__":
  schedule_messages1(SCHEDULED_MESSAGES1)
  schedule_messages2(SCHEDULED_MESSAGES2)
  app.run(debug=True)
