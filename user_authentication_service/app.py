#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify
from auth import Auth


app = Flask(__name__)


AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def main():
    data = {
        "message": "Bienvenue"
    }
    return jsonify(data)

@app.route('/users', methods=['POST'], strict_slashes=False)
def users(email, password):
    try:
        payload = {
            "email": email,
            "message", "user created"
        }
        return jsonify(payload)
    except Exception as e:
        error_message = {
            "message": "email already registered"
        }
        return jsonify(error_message), 400
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
