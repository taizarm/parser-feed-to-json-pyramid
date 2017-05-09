import unittest
from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from parser_feed_to_json_pyramid.view import views
        request = testing.DummyRequest()
        views.ParserView(request)


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from parser_feed_to_json_pyramid import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        self.testapp.get('/', status=302)
