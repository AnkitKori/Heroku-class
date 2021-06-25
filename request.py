import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':5, 'test_score':8, 'interview_score':7})

print(r.json())
