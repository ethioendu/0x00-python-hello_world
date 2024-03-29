#!/usr/bin/python3
"""
python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
-You have to manage urllib.error.HTTPError exceptions and print:
You must use the packages urllib and sys
"""

import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]

        try:
            with urllib.request.urlopen(url) as response:
                response_body = response.read().decode('utf-8')
                print(response_body)
        except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
        except urllib.error.URLError as e:
            print(f"Error code: {e.reason}")
