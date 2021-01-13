import requests
print(requests.__version__)

r = requests.get('http://www.google.com/')
# r.json()
print(r.text)