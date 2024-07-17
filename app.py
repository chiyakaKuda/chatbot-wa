from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)
@app.route('/bot',methods =['POST'])
def bot():
    incoming_message =request.values.get('Body',''.lower)
    resp =MessagingResponse()
    msg =resp.message()

    if "news" in incoming_message:
        U =('https://newsapi.org/v2/top-headlines?'
            'sources=techcrunch&'
            'apiKey=efa134ebe84e45828eefc26a3cd61f07')
        r = requests.get(U)
        response_dict =r.json()
        for x in response_dict:
            if x == 'articles':
                response_list =response_dict[x]
        for i in response_list:
            news =f'{i["title"]} ({i["urlToImage"]}) ({i["publishedAt"]}) ({i["content"]}) ({i["url"]})'
    else:
        new  ="Sorry, i could not fetch any news for you!"
    msg.body(news)
    return str(resp)
