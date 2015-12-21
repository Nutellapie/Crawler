from pyramid.response import Response
from pyramid.view import view_config
from pyramid import request
from pyramid.view import view_defaults
import pyramid.view
import fetch
import crawl
import itertools
import operator

#crawl.main()
tuple_date = fetch.main()

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

date_lista = list(grouper(3,tuple_date))
lista_sortata = sorted(date_lista, key = operator.itemgetter(0))





@view_config(route_name='test_2', renderer='templates/test_2.pt')
def home(request):
    studentlist = [ {'nume':'alice', 'value':22},
                      {'nume':'bob', 'value' :11},
                      {'nume':'charlie', 'value':33} ]


    return {'obj': 'obj', 'name': 'Test', 'studentList' : studentlist,
            'date' : lista_sortata}

def includeme(config):
    config.scan(__name__)
