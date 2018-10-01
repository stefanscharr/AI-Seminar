import requests, json

url = "https://jsonplaceholder.typicode.com/albums/"

myResponse = requests.get(url)

if (myResponse.ok):
  json_items = json.loads(myResponse.content.decode('utf-8'))
  print(json_items)
else:
  myResponse.raise_for_status()

#print ('finished')