from pyramid.response import Response
from pyramid.view import view_config
from pyramid import request
from crawl import main
from pyramid.view import view_defaults
from pyramid.response import Response


@view_config(route_name='test_2', renderer='templates/test_2.pt')
def home(request):
    return {'name': 'Test'}

'''
@view_defaults(route_name='test_2', renderer='templates/test_2.pt')
class Test_2_Views(object) :
    def __init__ (self,request):
        self.request = request

    @view_config(request_method='GET')
    def get(self):
        return Response('get')

    @view_config(request_method='POST')
    def post(self):
        return Response('post')
'''
def includeme(config):
    config.scan(__name__)
