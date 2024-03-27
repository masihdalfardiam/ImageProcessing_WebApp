import requests
from typing import Dict, List, Union
from decouple import config

class APIRequest:
    url = config('CORE_URL')
    token = config('CORE_TOKEN')

    @staticmethod
    def get(path: str, params: Union[None, Dict[str, any]] = None) -> Union[Dict[str, any], None]:
        try:
            response = requests.get(f"{APIRequest.url}/{path}", params=params, headers={"token": APIRequest.token})
            response.raise_for_status()  # Raise an exception if the response is not successful
            return response.json()
        except requests.exceptions.RequestException as e:
            for error in response.json()["errors"]:
                print(f"POST request to Core failed: {error}")
            return response.json()

    @staticmethod
    def post(path: str, data: Union[None, Dict[str, any]] = None) -> Union[Dict[str, any], None]:
        try:
            response = requests.post(f"{APIRequest.url}/{path}", json=data, headers={"token": APIRequest.token})
            response.raise_for_status()  # Raise an exception if the response is not successful
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle any request-related exceptions here
            for error in response.json()["errors"]:
                print(f"POST request to Core failed: {error}")
            return response.json()
