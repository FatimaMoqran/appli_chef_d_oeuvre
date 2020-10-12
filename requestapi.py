import requests

response = requests.post("http://23.251.133.90/predict",json = {"text":"Dear collegues First I would like to thank you for your efforts starting up our EMEA virtual teams."} )
print(response)
print(response.text)

