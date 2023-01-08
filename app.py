#Importing Libraries
from chatbot import chatbot
from flask import Flask, render_template, request
 
# giving path to folder contain style
app = Flask(__name__)
app.static_folder = 'static'

# giving path to file contain body of chatbot
@app.route("/")
def home():
    return render_template("index.html")

#for getting response
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

#built in method to run app.
if __name__ == "__main__":
    app.run() 