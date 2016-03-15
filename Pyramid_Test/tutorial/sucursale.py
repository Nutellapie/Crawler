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

nume_banci_lista = ['OTP','RAIF','ING']
locatie_banci_lista = ['STRADA Z','STRADA X']


@view_config(route_name='sucursale', renderer='templates/banci.pt')
def sucursale(request):
    return {'name': 'Sucursale', 'nume_banci' : nume_banci_lista,
            'locatie_banci' : locatie_banci_lista}

def includeme(config):
    config.scan(__name__)
