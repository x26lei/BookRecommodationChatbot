import requests

data = {
    'text': 'hi'
}

while(1):
    response = requests.post('http://127.0.0.1:5000/', data=data)

    response_data = response.json()

    print(response_data['text'])