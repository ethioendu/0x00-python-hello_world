#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status.
"""

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read()

            '''Displaying the response body with tabulation.'''
            print("Body response:")
            print("\t- type: {}".format(type(response_body)))
            print("\t- content: {}".format(response_body))
            print("\t- utf8 content: {}".format(response_body.decode('utf-8')))
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
