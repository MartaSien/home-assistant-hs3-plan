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

def get_entity_state(entity_id):
    """
    Get state of a given entity. Return it as a dict.
    """
    url = config.url + f'api/states/{entity_id}'
    
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        json_response = json.loads(response.text)
        return json_response
    else:
        print("")
        return None