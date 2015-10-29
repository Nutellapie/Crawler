#!./bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import html
import urlparse
import collections
import datetime
from lxml import etree
from lxml.etree import fromstring
import baza_de_date
import datetime

class obiect (object):

    def __init__(self, c1, c2, c3, c4, c5):
        self.denumire = c1
        self.prescurtare = c2
        self.valuta = c3
        self.sucursala = c4
        self.timp = c5


STARTING_URL = 'http://www.bnr.ro/Cursul-de-schimb-524.aspx'

# CRAWLER PENTRU CURS VALUTAR


def main():
    page = requests.get('http://www.bnr.ro/Cursul-de-schimb-524.aspx')
    tree = html.fromstring(page.text)

    tot = tree.xpath('//td/text()')  # Ia tot continutul
    list_obj = []

    contor = 0

    while contor < len(tot):
        print tot[contor], tot[contor + 1], tot[contor + 6]
        obiect_1 = obiect(tot[contor], tot[contor + 1], tot[contor + 6], 'BNR',
                          '29.08.2015')
        contor = contor + 7
#        datainput.main(obiect_1.prescurtare, obiect_1.denumire,
#        obiect_1.valuta, obiect_1.sucursala, obiect_1.timp)

    print obiect_1
#    import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()
