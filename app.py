from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def chatbot():
    if request.method == 'POST':
        # print("hi")
        user_input = request.form['text']

        response = process_user_input(user_input)
        #
        return json.dumps({'text': response})
        # return json.dumps({'text': 'valid request method.'})
    return json.dumps({'text': 'Invalid request method.'})

def process_user_input(user_input):
    # TODO: Add the chatbot logic here
    return 'Hello, I am a Chatbot!'

if __name__ == '__main__':
    app.debug = True
    app.run()


