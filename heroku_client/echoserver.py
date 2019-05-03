from flask import Flask, request
import json
import requests
from echobot import answerQuestion
from deeppavlov import configs, train_model
from deeppavlov import evaluate_model, build_model

app = Flask(__name__)

global model

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAfnNhtpG70BAA4kZAhZBZBXDapmMsEFF81ZBJUCg7gPe9ZAARVw5B7TfIW4fA8N8JfEcqfRGMQZA0csGa7yQpC9ZBqyvSg8ZCS4SG1NgAd4UeoN0s6xBZCqX0XZBFM4VnUQYhljZCMj9Pt6JwN3v2CRkiodIl53TZCB5gFfvHyPSy8fmQZDZD'

@app.route('/', methods=['GET'])
def handle_verification():
  print("Handling Verification.")
  if request.args.get('hub.verify_token', '') == 'my_voice_is_my_password_verify_me':
    print("Verification successful!")
    return request.args.get('hub.challenge', '')
  else:
    print("Verification failed!")
    return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print("Handling Messages")
  model = build_model('faq.json')
  payload = request.get_data()
  print(payload)
  for sender, message in messaging_events(payload):
    print("Incoming from %s: %s" % (sender, message))
    send_message(PAT, sender, message, model)
  return "ok"

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
    else:
      yield event["sender"]["id"], "I can't echo this"

def send_message(token, recipient, text, model):
  """Send the message text to recipient with id recipient.
  """
  #print(text)
  r = requests.post("https://graph.facebook.com/v3.2/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": model([text.decode('unicode_escape')])[0]}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print(r.text)

if __name__ == '__main__':
  app.run()