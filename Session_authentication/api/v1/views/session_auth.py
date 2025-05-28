#!/usr/bin/env python3
""" Session Auth Module """
from api.v1.views import app_views
from flask import Flask, request, jsonify, abort


@app_views.route('/auth_session/login', methods=["POST"], strict_slashes=False):
    def session_authentication():
        email = request.form.get("email")
        password = request.form.get("password")
        if len(email) <= 0 or email is None:
            return jsonify({"error": "email missing"}), 400
        if len(password) <= 0 or password is None:
            return jsonify({"error": "password missing"}), 400
        searched_emails = User.search({"email": email})
        if searched_emails is None:
            return jsonify({"error": "no user found for this email"}), 400