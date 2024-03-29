#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter, and finally displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    try:
        response = requests.post(url, data={'email': email})
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
