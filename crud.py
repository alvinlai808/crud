from flask import Flask, request
from db import ShittyDb


db = ShittyDb()
app = Flask('my_app')

@app.route('/')
def home():
    return 'Hello world!'


"curl -X POST http://127.0.0.1:5000/user\?fname\=alvin\&lname\=lai"
"curl -X POST http://127.0.0.1:5000/user\?fname\=jennifer\&lname\=watanabe"
@app.route('/user', methods = ['POST'])
def create_user():
    fname = request.args.get('fname')
    lname = request.args.get('lname')

    db.create(fname, lname)
    print(db.data)
    return f'{fname} {lname}'


"curl -X GET http://127.0.0.1:5000/user\?fname\=alvin"
"curl -X GET http://127.0.0.1:5000/user\?fname\=jennifer"
@app.route('/user', methods = ['GET'])
def get_user():
    fname = request.args.get('fname')

    db.read(fname)
    print(db.data[fname])
    return f'{fname}'


"curl -X PATCH http://127.0.0.1:5000/user\?fname\=alvin\&lname\=watanabe"
"curl -X PATCH http://127.0.0.1:5000/user\?fname\=jennifer\&lname\=lai"
@app.route('/user', methods = ['PATCH'])
def update_user():
    fname = request.args.get('fname')
    lname = request.args.get('lname')

    print(f"old user: {fname} {db.data[fname]}")
    db.update(fname, lname)
    print(f"updated user: {fname} {lname}")
    return f'{fname} {lname}'


"curl -X DELETE http://127.0.0.1:5000/user\?fname\=alvin"
@app.route('/user', methods = ['DELETE'])
def delete_user():
    fname = request.args.get('fname')

    print(f"deleting user: {fname} {db.data[fname]}")
    db.delete(fname)
    return f'{fname}'


app.run()
