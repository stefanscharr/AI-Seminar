# create URL
#subscription_key = None
#assert subscription_key

# text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
text_analytics_base_url =  "https://westeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"
language_api_url        = text_analytics_base_url + "languages"
print(language_api_url)


# set documents
documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' },
    { 'id': '4', 'text': 'Ceci est une pièce ecrivé en francais.'}  
]}


# call the detection API
import requests
from pprint import pprint

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}


response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)

'''
# render JSON-Data as HTML-Table
from IPython.display import HTML  # pip install IPython --user
table = []
for document in languages["documents"]:
    text  = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]
    langs = ", ".join(["{0}({1})".format(lang["name"], lang["score"]) for lang in document["detectedLanguages"]])
    table.append("<tr><td>{0}</td><td>{1}</td>".format(text, langs))
HTML("<table><tr><th>Text</th><th>Detected languages(scores)</th></tr>{0}</table>".format("\n".join(table)))
'''



# Sentiment Analysis
sentiment_api_url = text_analytics_base_url + "sentiment"
print(sentiment_api_url)

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},  
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},  
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'},
  {'id': '5', 'language': 'de', 'text': 'Das cognitive API gefällt mir sehr und ist nützlich für mich.'},
  {'id': '6', 'language': 'de', 'text': 'Mir erscheint das cognitive API zu kompliziert.Ich würde es nicht einsetzen.'}
]}

#headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
print (documents)
pprint(sentiments)



# extract key phrases
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)

response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)