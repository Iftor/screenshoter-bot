from datetime import datetime
from unittest.mock import patch, Mock
from bot_app.src.services.files import FileWriter


class TestFileWriter:

    def setup_method(self):
        self.test_file_writer = FileWriter('test_url', 'jpeg')

    def test_get_filename(self):
        fake_now = datetime(year=2023, month=1, day=1, hour=0, minute=0)
        with patch('bot_app.src.services.files.datetime') as mock_datetime:
            mock_datetime.now = Mock(return_value=fake_now)
            assert self.test_file_writer._get_filename() == '2023-01-01_00.00_link.jpeg'

    def test_get_file_path(self):
        self.test_file_writer._save_path = './dir'
        assert self.test_file_writer._get_file_path('filename') == './dir/filename'
