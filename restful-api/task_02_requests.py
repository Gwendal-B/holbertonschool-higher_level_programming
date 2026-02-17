#!/usr/bin/python3
"""
Module to fetch and process posts from JSONPlaceholder API
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts and print status code and titles
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:

        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save id, title, body into posts.csv
    """

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:

        posts = response.json()

        data = []

        for post in posts:

            data.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", mode="w", newline="") as file:

            writer = csv.DictWriter(file,
                                    fieldnames=["id", "title", "body"])

            writer.writeheader()

            writer.writerows(data)
