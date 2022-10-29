from flask import Flask
app = Flask("core_svc")


@app.route('/')
def hello_world():
    return 'I am a Core Service'