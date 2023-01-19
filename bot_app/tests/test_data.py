import json

import pytest

from bot_app.src.services.data import DataParser


class TestDataParser:

    def setup_method(self):
        self.test_data_parser = DataParser('jpeg')

    def test_check_error(self):
        self.test_data_parser._data = {'error': 502}
        assert self.test_data_parser._check_error() is True

        self.test_data_parser._data = {'xxx': 'yyy'}
        assert self.test_data_parser._check_error() is False

    def test_get_status_code(self):
        self.test_data_parser._data = {'history': [{'response': {'status': 200}}]}
        assert self.test_data_parser._get_status_code() == 200

    def test_get_screenshot_bytes(self):
        test_bytes = b'/9gA'
        self.test_data_parser._data = {'jpeg': test_bytes}
        assert self.test_data_parser._get_screenshot_bytes() == b'\xff\xd8\x00'

    def test_parse_data_raise_error(self):
        json_data = json.dumps({'error': 502, 'info': {'url': 'incorrect_url'}}).encode()
        with pytest.raises(NameError):
            self.test_data_parser.parse_data(json_data)
