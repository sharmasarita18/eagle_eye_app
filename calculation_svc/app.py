from flask import Flask
app = Flask("calculation_svc")


@app.route('/')
def hello_world():
    return 'I am a calculation Service'