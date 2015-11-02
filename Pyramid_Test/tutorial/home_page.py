from pyramid.response import Response
from pyramid.view import view_config
from pyramid import request
from crawl import main

# First view, available at http://localhost:6543/home

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return {'name': 'Home'}


def includeme(config):
    config.scan(__name__)
