import requests

response = requests.post("http://23.251.133.90/predict",json = {"text":"api ne fonctionne pas les clients sont furieux."} )
print(response)
print(response.text)

