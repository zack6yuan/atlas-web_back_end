#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request
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
def users():
    """ Users Function """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        payload = {
            "email": email,
            "message": "user created"
        }
        return jsonify(payload), 200
    except Exception:
        rejected = {
            "message": "email already registered"
        }
        return jsonify(rejected), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
