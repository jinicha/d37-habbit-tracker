import requests
import config

# create a user account
token = config.token
username = config.username
base_url = "https://pixe.la/v1/users"
create_user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create a graph definition
create_graph_url = f'{base_url}/{username}/graphs'
request_header = {
    "X-USER-TOKEN": token
}
request_body = {
    "id": "agraph",
    "name": "drink water",
    "unit": "oz",
    "type": "int",
    "color": "sora"
}

response = requests.post(url=create_graph_url, json=request_body, headers=request_header)
print(response.text)
