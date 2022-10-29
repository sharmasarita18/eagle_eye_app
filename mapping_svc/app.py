from flask import Flask
app = Flask("Mapping_svc")


@app.route('/')
def hello_world():
    return 'I am a Mapping Service'