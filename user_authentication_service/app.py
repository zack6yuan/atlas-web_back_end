#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)


AUTH = auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    data = {
        "message": "Bienvenue"
    }
    return jsonify(data)

@app.route('/users', methods=['POST'], strict_slashes=False)
def users(email, password):
    payload = {
        "email": "{}".format(email),
        "message": "user created"
    }
    if not email or not password:
        return jsonify()
    
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
