from flask import Flask
app = Flask("Authorization_svc")


@app.route('/')
def hello_world():
    return 'I am a Authorization Service'