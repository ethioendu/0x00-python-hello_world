#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get(url)

        '''Raise an exception for 4xx or 5xx status codes.'''
        response.raise_for_status()

        '''Displaying the response body with tabulation.'''

        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.RequestException as e:
        print(f"Error: {e}")
