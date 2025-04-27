"""Sending requests to Home Assistant REST API"""
import json
import requests
import config


def get_headers() -> dict:
    """
    Get RESTful API authentication headers.

    https://developers.home-assistant.io/docs/api/rest/
    """
    headers = {
        "Authorization": f"Bearer {config.token}",
        "content-type": "application/json",
    }
    return headers


def get_entity_state_list() -> list:
    """
    Get a list of entity states from the config file.
    """
    for entity in config.entities:
        entity_state = get_entity_state(entity[1])
        entity[1] = entity_state
    return config.entities


def get_entity_state(entity_id: str) -> str:
    """
    Get state of a given entity.
    """
    url = config.url + f"api/states/{entity_id}"
    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        response.raise_for_status()
        json_response = json.loads(response.text)
        print(json_response)
        if entity_id.startswith("climate"):
            return str(json_response["attributes"]["current_temperature"]) + " °C"
        return str(json_response["state"])
    except requests.exceptions.RequestException as e:
        print(f"[{entity_id}] {e}\n")
        return "n/a"
