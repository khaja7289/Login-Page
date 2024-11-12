from flask import Flask, request, jsonify
import boto3
import json

app = Flask(__name__)

# AWS S3 configuration
s3 = boto3.client('s3')
BUCKET_NAME = 'your-bucket-name'

def get_users():
    try:
        obj = s3.get_object(Bucket=BUCKET_NAME, Key='users.json')
        users = json.loads(obj['Body'].read().decode('utf-8'))
    except s3.exceptions.NoSuchKey:
        users = {}
    return users

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    users = get_users()
    if username in users and users[username] == password:
        return jsonify(message=f"Welcome, {username}!"), 200
    else:
        return jsonify(message="Invalid credentials, please try again. If you are a new user, please register."), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
