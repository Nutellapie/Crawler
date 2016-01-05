from pyramid.response import Response
from pyramid.view import view_config
from pyramid import request
from pyramid.view import view_defaults
import pyramid.view
import fetch
import crawl
import itertools
import operator
import datetime





dictionar_banci = {'OTP' : 'Strada x', 'Cec' : 'Strada z'}


@view_config(route_name='sucursale', renderer='templates/banci.pt')
def sucursale(request):
    return {'name': 'Sucursale', 'date_banca' : dictionar_banci}

def includeme(config):
    config.scan(__name__)
