#!/usr/bin/python3
"""Takes your github credentials and uses the github
API to display your id
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    uname = argv[1]
    passwd = argv[2]

    res = requests.get("https://api.github.com/user", auth=(uname, passwd))
    res = res.json()
    print(res.get('id'))
