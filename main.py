import requests
import config

# create a user account
token = config.token
username = config.username
base_url = "https://pixe.la/v1/users"
params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=base_url, json=params)
print(response.text)
