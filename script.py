import requests

print("requests version: " + requests.__version__)

 r = requests.get('http://www.google.com/')

 print(r.text)