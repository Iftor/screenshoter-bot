from typing import Tuple

from bot_app.src.services.data import DataParser
from bot_app.src.services.files import FileWriter
from bot_app.src.services.web import Requester, LinkModifier


class ScreenshotMaker:

    class _ImageFormats:
        JPEG = 'jpeg'
        PNG = 'png'

    def __init__(self, message_text: str):
        self._message_text = message_text
        self._screenshot_format = self._ImageFormats.JPEG
        self._page_url_full = None
        self._page_url_short = None
        self._page_url_for_filename = None
        self._requester = None
        self._data_parser = None
        self._screenshot_saver = None

    def run(self) -> Tuple[int, bytes]:
        self._init_page_url_types()
        self._init_services()
        json_data = self._requester.make_request()
        status_code, screenshot_bytes = self._data_parser.parse_data(json_data)
        self._screenshot_saver.write_file(screenshot_bytes)

        return status_code, screenshot_bytes

    def _init_page_url_types(self):
        self._page_url_full = LinkModifier.adjust_url(self._message_text)
        self._page_url_short = LinkModifier.remove_scheme(self._page_url_full)
        self._page_url_for_filename = LinkModifier.replace_slashes(LinkModifier.cut_url(self._page_url_short, 40))

    def _init_services(self):
        self._requester = Requester(self._page_url_full, self._screenshot_format)
        self._data_parser = DataParser(self._screenshot_format)
        self._screenshot_saver = FileWriter(self._page_url_for_filename, self._screenshot_format)
