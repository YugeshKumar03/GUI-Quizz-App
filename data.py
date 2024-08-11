import requests
import json

PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

data = requests.get("https://opentdb.com/api.php", params=PARAMETERS).json()
question_data = data["results"]
