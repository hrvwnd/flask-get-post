from flask import Flask
import requests

app =Flask(__name__)
@app.route('/',methods=['GET'])
def test():
    requests.post('http://localhost:5001', json={"name":"Bob"})
    return "ok \n"

if __name__ == '__main__':
    app.run(port=5001)
