from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!!</p>"

@app.route('/req/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/api', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return {
            "method": "POST",
            "status": 200,
            "message": f'post message is {request.form["message"]}',
        }
    else:
        return {
            "method": "GET",
            "status": 200,
            "message": "api is OK",
        }