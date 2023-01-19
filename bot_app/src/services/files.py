import os
from datetime import datetime

from bot_app import settings


class FileWriter:

    def __init__(self, page_url: str, screenshot_format: str):
        self._page_url = page_url
        self._screenshot_format = screenshot_format
        self._save_path = settings.SAVE_PATH

    def write_file(self, bytes_file: bytes):
        filename = self._get_filename()
        full_path = self._get_file_path(filename)
        with open(full_path, 'wb') as file:
            file.write(bytes_file)

    def _get_filename(self) -> str:
        date_now = datetime.now()
        date_str = date_now.strftime('%Y-%m-%d_%H:%M')

        return f'{date_str}_{self._page_url}.{self._screenshot_format}'

    def _get_file_path(self, filename: str) -> str:
        return os.path.join(self._save_path, filename)
