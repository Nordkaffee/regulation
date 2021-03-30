""" Tasks to get weather information from remote location """

import os
import time
import json
import requests

from tasks import Task

CITY_TO_LAT_LON = {
    'Medellin': {'lat': 6.2518, 'lon': -75.5636}
}


class OpenWeatherMapApiClient:
    """TODO

    """

    url: str = 'https://api.openweathermap.org/data/2.5/onecall'
    env: str = 'OPEN_WEATHER_MAP_API_KEY'
    appid: str = os.getenv(env, None)

    def __init__(self, city: str):
        #
        if self.appid is None:
            raise RuntimeError(
                f'Environment variable {OpenWeatherMapApiClient.env} not found!'
            )

        #
        latlon = CITY_TO_LAT_LON.get(city, None)
        if latlon is None:
            raise KeyError(
                f'City {city} not found in lookup table {CITY_TO_LAT_LON}'
            )

        #
        self.params = latlon
        self.params['appid'] = OpenWeatherMapApiClient.appid

    def get_current_weather(self):
        """TODO

        """
        url = OpenWeatherMapApiClient.url
        return requests.request('GET', url, params=self.params)


class QueryOpenWeatherMapApiTask(Task):
    """TODO

    """

    def __init__(self, city: str):
        super(QueryOpenWeatherMapApiTask, self).__init__()
        self.client = OpenWeatherMapApiClient(city=city)

    def execute(self):
        """

        """
        
        # get current weather at location
        response = self.client.get_current_weather().json()
        if response.get('cod', 200) != 200:
            # TODO: something went wrong, handle
            pass

        # TODO: write to our database
        print(response['current'])


class QueryOpenWeatherMapApiTaskMedellin(QueryOpenWeatherMapApiTask):
    """TODO

    """

    def __init__(self):
        super(QueryOpenWeatherMapApiTaskMedellin, self).__init__('Medellin')