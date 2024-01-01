from flask import Flask
import requests

#create flask instance
app = Flask(__name__)

@ app.route("/")
def hello():
    return "Hello, World"

@app.route('/atg')
def atg_world():
    response = requests.get('https://atg.world')
    return response.text 

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)    
    
