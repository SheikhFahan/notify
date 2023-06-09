import requests


endpoint = "http://127.0.0.1:8000/pdfs/create/"

data = {
    'name': 'Module2', 'prof_name': 'DemoProf', 'sub_code': '18CS61', 'ideal_index': 3, 'upload_date': '2023-06-01'
}
response = requests.post(endpoint, json= data)

print(response.reason)


