from flask import Flask
app = Flask(__name__)

@app.route('/hello/<num>')

def hello(num):
    return "Hello" + str(num)