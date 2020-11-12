import requests, json 

def classify(text_input):
    url = "http://23.251.133.90/predict"
    headers = {'Content-Type':'application/json'}
    body = {'text':text_input}
    response = requests.post(url,json=body, headers=headers)
    return response.json()

