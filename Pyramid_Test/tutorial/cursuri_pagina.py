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

tuple_date = fetch.main()

contor = 0
lista_simboluri = []
while contor < len(tuple_date):
    lista_simboluri.append(tuple_date[contor])
    contor = contor + 3

lista_simboluri = sorted(list(set(lista_simboluri)))

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

date_lista = list(grouper(3,tuple_date))
lista_sortata = sorted(date_lista, key = operator.itemgetter(0))

data_curenta = datetime.date.today()



'''
@view_config(route_name='detalii', renderer='templates/detalii.pt')
def detalii(request):
    return {'name': 'Cursuri Valutare', 'date_simboluri' : lista_simboluri}


def includeme(config):
    config.scan(__name__)
'''
