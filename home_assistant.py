import requests
import config
import json


def get_headers():
    """
    Get RESTful API authentication headers.

    https://developers.home-assistant.io/docs/api/rest/
    """
    headers = {
        "Authorization": f"Bearer {config.token}",
        "content-type": "application/json",
    }
    return headers


def get_entity_state_list():
    """
    Get a list of entity states from the config file.
    """
    for entity in config.entities:
        entity_state = get_entity_state(entity[1])
        entity[1] = entity_state
    return config.entities


def get_entity_state(entity_id):
    """
    Get state of a given entity.
    """
    url = config.url + f"api/states/{entity_id}"
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        json_response = json.loads(response.text)
        print(json_response)
        if entity_id.startswith("climate"):
            return f"{json_response["attributes"]["current_temperature"]} °C"
        return json_response["state"]
    except requests.exceptions.RequestException as e:
        print(f"[{entity_id}] {e}\n")
        return "n/a"
