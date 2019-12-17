from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_test():
    return {"name": "Bob"}


@app.route('/post_test', methods=['POST'])
def post_test():
    print (request.json)
    return "ok \n"


if __name__ == '__main__':
    app.run()




