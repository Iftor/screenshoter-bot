from bot_app.src.services.web import Requester, LinkModifier


class TestRequester:

    def setup_method(self):
        self.test_requester = Requester('test_url', 'jpeg')

    def test_get_request_url(self):
        self.test_requester._splash_port = '8888'
        assert self.test_requester._get_request_url() == f'http://localhost:8888/render.json'

    def test_get_request_params(self):
        params = {
            'history': 1,
            'jpeg': 1,
            'url': 'test_url',
            'wait': 1,
            'render_all': '1',
        }
        assert self.test_requester._get_request_params() == params


class TestLinkModifier:

    def test_check_scheme_presence(self):
        assert LinkModifier.check_scheme_presence('https://qq.com') is True
        assert LinkModifier.check_scheme_presence('qq.com') is False

    def test_add_scheme(self):
        assert LinkModifier.add_scheme('qq.com') == 'http://qq.com'

    def test_remove_scheme(self):
        assert LinkModifier.remove_scheme('http://qq.com') == 'qq.com'

    def test_cut_url(self):
        assert LinkModifier.cut_url('www.qq.com/home/tables', 20) == 'www.qq.com/home/tabl'
        assert LinkModifier.cut_url('www.qq.com/home/tables', 30) == 'www.qq.com/home/tables'
