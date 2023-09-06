import requests


class BoredAPIWrapper:
    def __init__(self):
        self.base_url = 'https://www.boredapi.com/api/activity'

    def get_random_activity(self, **kwargs):
        params = {
            'type': kwargs.get('type'),
            'participants': kwargs.get('participants'),
            'minprice': kwargs.get('minprice'),
            'maxprice': kwargs.get('maxprice'),
            'price': kwargs.get('price'),
            'accessibility': kwargs.get('accessibility'),
            'minaccessibility': kwargs.get('minaccessibility'),
            'maxaccessibility': kwargs.get('maxaccessibility'),
        }

        response = requests.get(self.base_url, params=params)
        return response.json()