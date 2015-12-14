from pyramid.response import Response
from pyramid.view import view_config
from pyramid import request
from crawl import main
from pyramid.view import view_defaults
import pyramid.view
import fetch

tuple_date = fetch.main()

@view_config(route_name='test_2', renderer='templates/test_2.pt')
def home(request):
    studentlist = [ {'nume':'alice', 'value':22},
                      {'nume':'bob', 'value' :11},
                      {'nume':'charlie', 'value':33} ]


    return {'obj': 'obj', 'name': 'Test', 'studentList' : studentlist, 'date' : tuple_date}

def includeme(config):
    config.scan(__name__)
