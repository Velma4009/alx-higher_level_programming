
#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]
    res = requests.get(url)

    if res.status_code < 400:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")
