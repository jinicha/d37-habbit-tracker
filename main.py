import requests
import datetime as dt
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
# response = requests.post(url=base_url, json=create_user_params)

# create a graph definition
create_graph_url = f'{base_url}/{username}/graphs'
request_header = {
    "X-USER-TOKEN": token
}
graph_id = "agraph"
create_graph_request_body = {
    "id": graph_id,
    "name": "drink water",
    "unit": "oz",
    "type": "int",
    "color": "sora"
}
# response = requests.post(url=create_graph_url, json=create_graph_request_body, headers=request_header)

# post value to the graph
post_value_url = f'{create_graph_url}/{graph_id}'
now = dt.datetime.now().strftime("%Y%m%d")
post_value_request_body = {
    "date": now,
    "quantity": input("How many cups of water did you drink today? ")
}
response = requests.post(url=post_value_url, json=post_value_request_body, headers=request_header)

# update unit from oz to cup
update_unit_request_body = {
    "unit": "cups"
}
# response = requests.put(url=post_value_url, headers=request_header, json=update_unit_request_body)

# print(response.text)
