import requests

url = 'http://127.0.0.1:5000/'

html = requests.get(url)

print(html) # <Response [200]>
print(html.text)