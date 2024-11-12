from flask import Flask, request, jsonify, render_template_string
import json

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username in users and users[username] == password:
        return jsonify(message=f"Welcome, {username}!"), 200
    else:
        return jsonify(message="Invalid credentials, please try again."), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
