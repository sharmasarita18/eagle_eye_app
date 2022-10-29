from flask import Flask
app = Flask("data_provision_svc")


@app.route('/')
def hello_world():
    return 'I am a Data Provision Service'