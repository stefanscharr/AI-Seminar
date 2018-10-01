
# install Pillow module before running this script: 
# pip install Pillow --user

# change variable image_path

import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt #pip install matplotlib
from PIL import Image    
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "my_key_here"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the westcentralus region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.


#vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
vision_base_url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/"

analyze_url = vision_base_url + "analyze"

# Set image_path to the local path of an image that you want to analyze.
#image_path = "C:/Documents/ImageToAnalyze.jpg"
image_path = "./pics/moebel.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params     = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)

import json   # https://realpython.com/python-json/

try:
    decoded = json.loads(analysis)
    print (decoded[:10])
    # Access data
    #for x in decoded['categories']:
    #    name = x['name']  # + 'score = ' + x['score'])
 
except (ValueError, KeyError, TypeError):
    print ("JSON format error")

image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
plt.show()