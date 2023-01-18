import base64
import json
from typing import Tuple


class DataParser:

    def __init__(self, screenshot_format: str):
        self._screenshot_format = screenshot_format
        self._data = None

    def parse_data(self, json_data: bytes) -> Tuple[int, bytes]:
        self._data = json.loads(json_data)
        if self._check_error():
            raise NameError(f'incorrect url: {self._data["info"]["url"]}')
        status_code = self._get_status_code()
        screenshot_bytes = self._get_screenshot_bytes()

        return status_code, screenshot_bytes

    def _check_error(self) -> bool:
        return 'error' in self._data

    def _get_status_code(self) -> int:
        return self._data['history'][0]['response']['status']

    def _get_screenshot_bytes(self) -> bytes:
        return base64.b64decode(self._data[self._screenshot_format])
