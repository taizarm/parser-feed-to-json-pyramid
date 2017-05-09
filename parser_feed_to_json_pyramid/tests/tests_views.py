import pytest
from pyramid import testing
from mock import Mock

from parser_feed_to_json_pyramid.view import views
from parser_feed_to_json_pyramid.tests import test_scenarios


class TestParser():

    def setup_method(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)
        self.config.add_route('home', '/')
        self.config.add_route('login', '/login')

    def test_login_get(self):
        parser_view = views.ParserView(self.request)
        res = parser_view.login_get()
        assert res == {}

    def test_login_post(self):
        parser_view = views.ParserView(self.request)

        post_data = {
            'username': parser_view.default_username,
            'password': parser_view.default_password
        }
        self.request.params = post_data

        res = parser_view.login_post()
        assert res.code == 302

    def test_login_post_invalid_login(self):
        parser_view = views.ParserView(self.request)

        post_data = {
            'username': 'invalid',
            'password': 'invalid'
        }
        self.request.params = post_data

        res = parser_view.login_post()
        assert 'Invalid password' in res['errors']
        assert 'Invalid username' in res['errors']

    # @pytest.mark.parametrize('referer, is_authenticated',
    #                          test_scenarios.test_scenarios_is_authenticated)
    # def test_is_authenticated(self, referer, is_authenticated):
    #     self.request.referer = referer
    #     parser_view = views.ParserView(self.request)
    #
    #     res = parser_view.is_authenticated()
    #
    #     assert res == is_authenticated

    def test_parser_view_authenticated(self):
        parser_view = views.ParserView(self.request)

        parser_view.is_authenticated = Mock(return_value=True)
        res = parser_view.parser_view()
        assert type(res) is dict

    def test_parser_view_not_authenticated(self):
        parser_view = views.ParserView(self.request)

        parser_view.is_authenticated = Mock(return_value=False)
        res = parser_view.parser_view()
        assert res.code == 302
