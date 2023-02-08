import requests


def login(username, password):
    # Enter example 
    url = "index.html"

    # Request payload
    payload = {
        #Set username and password
        "username": username,
        "password": password
    }

    # Request headers
    headers = {
        "Content-Type": "application/json"
    }

    # POST request to the login URL
    response = requests.post(url, json=payload, headers=headers)

    # Check if the login was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the token from the response
        token = data["token"]
        # Return the token
        return token  
    else:
        # Return None if the login failed
        return None