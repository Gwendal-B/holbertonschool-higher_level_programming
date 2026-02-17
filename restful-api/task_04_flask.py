#!/usr/bin/python3
"""
Simple Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# IMPORTANT: dictionnaire VIDE pour le checker
users = {}


# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Return all usernames
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


# Status endpoint
@app.route('/status')
def status():
    return "OK"


# Get specific user
@app.route('/users/<username>')
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


# Add user endpoint
@app.route('/add_user', methods=['POST'])
def add_user():

    # Check JSON valid
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # Check username exists in JSON
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
