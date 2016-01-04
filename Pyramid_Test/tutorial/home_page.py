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

#crawl.main()
tuple_date = fetch.main()

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

date_lista = list(grouper(3,tuple_date))
lista_sortata = sorted(date_lista, key = operator.itemgetter(0))

data_curenta = datetime.date.today()

primul_entry = lista_sortata[0]
curs_minim = 4444
curs_maxim = 0

lista_noua = []

for i in lista_sortata :
    if i[0] == primul_entry[0] :
        if primul_entry[1] > curs_maxim :
            curs_maxim = primul_entry[1]

        newstring = primul_entry[2].replace("," , ".")
        newstring = newstring.strip()
        if float(newstring) < curs_minim :
            curs_minim = float(newstring)

    if primul_entry[0] != i[0] :
        lista_noua.append(primul_entry[0])
        lista_noua.append(curs_maxim)
        lista_noua.append(curs_minim)
        curs_maxim = 0
        curs_minim = 4444
    primul_entry = i

#import pdb; pdb.set_trace()

lista_noua = list(grouper(3,lista_noua))

# First view, available at http://localhost:6543/home

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    return {'name': 'Home','data_astazi' : data_curenta
              ,'lista' : lista_noua}


def includeme(config):
    config.scan(__name__)
