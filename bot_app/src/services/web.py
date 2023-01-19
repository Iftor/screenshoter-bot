from urllib.parse import urlparse

import requests

from bot_app import settings


class Requester:

    def __init__(self, page_url: str, screenshot_format: str):
        self._page_url = page_url
        self._screenshot_format = screenshot_format
        self._splash_port = settings.SPLASH_PORT
        self._full_page = settings.FULL_PAGE

    def make_request(self) -> bytes:
        request_url = self._get_request_url()
        params = self._get_request_params()
        response = requests.get(request_url, params=params)

        return response.content

    def _get_request_url(self) -> str:
        return f'http://splash:{self._splash_port}/render.json'

    def _get_request_params(self) -> dict:
        return {
            'history': 1,
            self._screenshot_format: 1,
            'url': self._page_url,
            'wait': 1,
            'render_all': self._full_page,
        }


class LinkModifier:

    @classmethod
    def adjust_url(cls, url: str) -> str:
        if cls.check_scheme_presence(url):
            return url

        return cls.add_scheme(url)

    @staticmethod
    def check_scheme_presence(url: str) -> bool:
        return not not urlparse(url).scheme

    @staticmethod
    def add_scheme(url: str) -> str:
        return 'http://' + url

    @staticmethod
    def remove_scheme(url: str) -> str:
        return url.split('://')[1]

    @staticmethod
    def cut_url(url: str, max_length: int) -> str:
        if len(url) > max_length:
            return url[:max_length]

        return url
