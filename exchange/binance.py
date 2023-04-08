import requests
from typing import *

import logging
logger = logging.getLogger()
class BinanceClient:
    def __init__(self, futures = False):
        self._base_url = "https://api.binance.com"
        self.futures = futures

        if self.futures:
            self._base_url = "https://fapi.binance.com"
        else:
            self._base_url = "https://api.binance.com"

    def _make_request(self, endpoint : str , query_parameters : Dict):
        try:
            response = requests.get(self._base_url + endpoint, params=query_parameters)
        except Exception as e:
            logger.error("Connection error while making connection %s : %s ", endpoint, e)
        if response.status_code==200:
            return response.json()
        else:
            logger.error("Error while making requeust to %s : %s(status code = %s)", endpoint,
                         response.json(), response.status_code)
            return None