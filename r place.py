import requests
import time

# Insert your Reddit API credentials here
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
app_id = "YOUR_APP_ID"
app_secret = "YOUR_APP_SECRET"

# Logging in to the API
auth = requests.auth.HTTPBasicAuth(app_id, app_secret)
data = {
    "grant_type": "password",
    "username": username,
    "password": password
}
headers = {"User-Agent": "MyAPI/0.0.1"}

response = requests.post("https://www.reddit.com/api/v1/access_token", 
                         auth=auth, 
                         data=data, 
                         headers=headers)

TOKEN = response.json()["access_token"]
headers["Authorization"] = f"bearer {TOKEN}"

# r/Place API URL
url = "https://www.reddit.com/api/place/draw.json"

# Drawing details
pixels = [
    {"x": 50, "y": 50, "color": 1},  # Pixels with coordinates and colors
    # ...
]

for pixel in pixels:
    data = {
        "x": pixel["x"],
        "y": pixel["y"],
        "color": pixel["color"],
    }
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print(f"Pixel ({pixel['x']}, {pixel['y']}) placed successfully.")
    else:
        print(f"Failed to place pixel ({pixel['x']}, {pixel['y']}): {response.content}")

    # Waiting because of API limitations
    time.sleep(5)
