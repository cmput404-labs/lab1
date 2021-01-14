import requests

print("requests version: " + requests.__version__)

r = requests.get('https://raw.githubusercontent.com/cmput404-labs/lab1/main/script.py')

print(r.text)