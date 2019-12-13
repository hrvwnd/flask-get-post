from flask import Flask
import requests

app =Flask(__name__)
@app.route('/',methods=['GET'])
def test():
    requests.post('localhost:5000', json={"name":"Bob"})
    return "ok \n"

if __name__ = __main__:
    app.run("5001")