from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from parser_feed_to_json_pyramid.parser import parser as parser_folder


class ParserView(object):

    def __init__(self, request):
        self.request = request
        self.default_username = 'admin'
        self.default_password = '1234admin'

    @view_config(route_name='login', request_method='GET',
                 renderer='templates/login.jinja2')
    def login_get(self):
        return {}

    @view_config(route_name='login', request_method='POST',
                 renderer='templates/login.jinja2')
    def login_post(self):
        data = dict(self.request.params)

        username = data.get('username', '')
        password = data.get('password', '')

        errors = []
        if username != self.default_username:
            errors.append('Invalid username')

        if password != self.default_password:
            errors.append('Invalid password')

        if errors:
            return {'errors': errors}
        else:
            return HTTPFound(self.request.route_url('home'))

    def is_authenticated(self):
        referer = self.request.referer or None
        login_url = self.request.route_url('login')
        return referer == login_url

    @view_config(route_name='home', renderer='json')
    def parser_view(self):

        if self.is_authenticated():
            parser = parser_folder.Parser()
            parser.parse_xml()
            return parser.json
        else:
            return HTTPFound(self.request.route_url('login'))


