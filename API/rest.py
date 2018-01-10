
from flask import Flask, request
from ErrorCodes import codes
from mysqlWrapper import mysqlClient
app = Flask(__name__)


db = mysqlClient.mysqlDB(host = 'localhost', user='root', password='root123', db="Trello")


@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.login(request.get_json())

@app.route('/register', methods = ['POST'])
def register():
    if request.method == 'GET':
        return codes.invalidRequestMethod()
    else:
        return db.register(request.get_json())



if __name__ == "__main__":
    app.run()