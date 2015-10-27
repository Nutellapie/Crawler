#!./bin/python
# -*- coding: utf-8 -*-
from lxml.cssselect import CSSSelector
import requests
from lxml import html
import urlparse
import collections
import datetime
from lxml import etree
import pdb
import datainput
import re

'''
class obiect (object):

    def __init__(self, c1, c2, c3, c4, c5, c6):
        self.prescurtare = c1
        self.denumire = c2
        self.valuta_cumparare = c3
        self.valuta_vanzare = c4
        self.sucursala = c5
        self.timp = c6
'''

data_de_azi = datetime.date.today()


def bnr():       # MERGE -  DATABASE OBJECT

    STARTING_URL = 'http://www.bnr.ro/Cursul-de-schimb-524.aspx'

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)

    tot = tree.xpath('//td/text()')  # Ia tot continutul
    list_obj = []

    contor = 0

    while contor < len(tot):
        print tot[contor], tot[contor + 1], tot[contor + 6]
        obiect_1 = obiect(tot[contor], tot[contor + 1], tot[contor + 6], 'BNR',
                          data_de_azi)
        contor = contor + 7
        list_obj.append(obiect_1)
    return list_obj


def volksbank():      # MAI TREBUIE LUCRAT /s  - DATABASE OBJECT

    STARTING_URL = 'http://www.volksbank.ro/ro/AfisareCursValutar'

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    # print (etree.tostring(tree,encoding = unicode, pretty_print = True))
    e = tree.xpath('//tr/td/span/text()')  # 33 - 71 CURS

    '''
    contor = 33
    list_obj = []
    while(contor < 72):dd
        if e[contor] != None:
            list_obj.append(e[contor])
        contor = contor + 1
    '''
    pdb.set_trace()


def alphabank():  # DATABASE OBJECT
    STARTING_URL = 'https://www.alphabank.ro/ro/rate/rate_si_dobanzi.php'
    tree = html.fromstring(page.text)

    page = requests.get(STARTING_URL)
    # print (etree.tostring(tree,encoding = unicode, pretty_print = True))
    e = tree.xpath('//tr[@height="18"]/td[@class="stilTd1"]/text()')
    z = tree.xpath('//tr[@height="18"]/td[@class="stilTd2"]/text()')

    list_obj = []

    contor = 0

    while contor < len(e):
        obiect_1 = obiect(e[contor], e[contor + 2], e[contor + 3], 'AlphaBank',
                          data_de_azi)
        print e[contor], e[contor + 2], e[contor + 3], 'AlphaBank', data_de_azi
        contor = contor + 6
        list_obj.append(obiect_1)

    pdb.set_trace()


def bcr():
    STARTING_URL = 'http://www.bcr.ro/ro/curs-valutar'

    e = fromstring(r.get("https://www.bcr.ro/ro/curs-valutar",
                         headers={'User-Agent': 'Something'}).text)
    z = e.xpath('//table[@class="overview glaze fullsize"]/tr/td')

    print z[1].text

    contor = 1
    list_obj = []
    while contor < len(z):
        obiect_1 = obiect(z[contor].text, z[contor + 1].text, z[contor + 2].text,
                          'BCR', data_de_azi)
        print z[contor].text, z[contor + 1].text, z[contor + 2].text, 'BCR', data_de_azi
        contor = contor + 4

        list_obj.append(obiect_1)
    pdb.set_trace()


def raiffeisen():
    STARTING_URL = "http://www.raiffeisen.ro/curs-valutar"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//table/tr/td')

    contor = 4

    while contor < 122:
        print z[contor].text, z[contor + 1].text, z[contor + 3].text, z[contor + 4].text, 'Raiffeisen', data_de_azi
        obiect_1 = obiect(z[contor].text, z[contor + 1].text, z[contor + 3].text,
                          'Raiffeisen', data_de_azi)
        contor = contor + 7

    pdb.set_trace()


def garantibank():
    STARTING_URL = "https://ebank.garantibank.ro/isube/yatirimislemleri/doviz/dovizkur"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/text()')

    contor = 6
    while contor < len(z):
        print z[contor], z[contor + 2], z[contor + 3], z[contor + 5], z[contor + 6]
        contor = contor + 7
    pdb.set_trace()


def piraeus():
    STARTING_URL = "http://www.piraeusbank.ro/Banca/Unelte/curs_ghiseu.html"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/span')

    contor = 11
    while (contor < 26):
        print z[contor].text, z[contor + 1].text, z[contor + 2].text
        contor = contor + 3
    pdb.set_trace()


def cecbank():
    STARTING_URL = "https://www.cec.ro/curs-valutar"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tbody/tr/td/text()')

    contor = 2
    while contor < 30:
        valoare = re.sub(r"[^A-Za-z]+", ' ',str(z[contor]))
        valoare_1 = re.sub(r"[^0-9-.]+", '', str(z[contor+2]))
        valoare_2 = re.sub(r"[^0-9-.]+", '', str(z[contor+3]))
        datainput.main(valoare)
        print valoare, valoare_1, valoare_2

        contor = contor + 8
    pdb.set_trace()


def bancpost():
    STARTING_URL = "https://www.bancpost.ro/Bancpost/Financiare/Istoric-Curs-Valutar"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//table[@class="forex"]/tbody/tr/td/text()')

    '''
    index = 0
    for m in z :
        print m, index
        index = index + 1
    '''

    contor = 2
    while(contor < 54):
        numar, nume = str(z[contor]).split()
#        datainput.main(nume,nume,str(z[contor+2]),str(z[contor+3]),'BancPost',data_de_azi)
        contor = contor + 6
        pdb.set_trace()
#        print nume, nume, z[contor + 2], z[contor + 3],'BancPost',data_de_azi

#    pdb.set_trace()


def brdbank():
    STARTING_URL = "https://www.brd.ro/instrumente-utile/curs-valutar-si-dobanzi-de-referinta"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/text()')

    contor = 12
    while contor < 100:
        datainput.main(str(z[contor + 1]), str(z[contor]),
                       str(z[contor + 5]), str(z[contor + 6]), 'BRD', data_de_azi)
        contor = contor + 9
#        print z[contor], z[contor + 1], z[contor + 5], z[contor + 6]
#        pdb.set_trace()


def bancatransilvania():
    STARTING_URL = "https://www.bancatransilvania.ro/curs-valutar-spot/"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td//text()')

    contor = 6
    while contor < 95:
        datainput.main(str(z[contor]), str(z[contor + 1]), str(z[contor + 3]),
                       str(z[contor + 4]), 'BancaTransilvania', data_de_azi)
        contor = contor + 7
#        print z[contor], z[contor + 1], z[contor + 3], z[contor + 4]
#        pdb.set_trace()


def milenium():
    pass


def bancaromaneasca():
    STARTING_URL = "https://www.banca-romaneasca.ro/instrumente-utile/curs-valutar/"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/text()')

    contor = 0
    while contor < len(z):
        print z[contor], z[contor + 5], z[contor + 6]
        contor = contor + 7

    pdb.set_trace()

# PROBLEME LA JPY


def crediteuropebank():
    STARTING_URL = "http://www.crediteurope.ro/dobanzi-cotatii-si-cursuri/cursuri/"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/text()')

    index = 0
    for m in z:
        print m, index
        index = index + 1

    contor = 0
    marire = 0
    while contor < 25:
        if contor == 16:
            marire = 1
        print z[contor], z[contor + 2 + marire], z[contor + 3 + marire]
        contor = contor + 4 + marire

    pdb.set_trace()


def carpaticabank():
    STARTING_URL = "https://www.carpatica.ro/curs-valutar/"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath(
        '//tr[position()<7 and position()>2]/td[position()<5]/text()')

    contor = 0
    while contor < len(z):
        numar, nume = str(z[contor]).split()
        datainput.main(nume, nume, str(
            z[contor + 1]), str(z[contor + 2]), 'CarpaticaBank', data_de_azi)
        contor = contor + 3
#        print nume, nume, z[contor + 1], z[contor + 2], 'CarpaticaBank', data_de_azi
#        pdb.set_trace()


def librabank():
    STARTING_URL = "http://www.librabank.ro/Curs_valutar/"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)

    z = tree.xpath(
        '//table[@class="curs_tabel_1"]/tr[position()>1 and position()<14]/td/span/text()')

    contor = 0
    while contor < 33:
        numar, nume = str(z[contor]).split()
        datainput.main(nume, nume, str(
            z[contor + 1]), str(z[contor + 2]), 'LibraBank', data_de_azi)
        contor = contor + 3
    #        print z[contor],z[contor+1],z[contor+2],data_de_azi,'LibraBank'


#    pdb.set_trace()

def otpbank():
    STARTING_URL = "https://persoanefizice.otpbank.ro/ro/curs-valutar"
    page = requests.get(STARTING_URL)

    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td[position()<5]/text()')

    contor = 0
    while contor < len(z):
        pres = str(z[contor])
        nume = str(z[contor + 1])
        val_c = str(z[contor + 2])
        val_v = str(z[contor + 3])

        datainput.main(pres, nume, val_c, val_v, 'OTP', data_de_azi)

#        pdb.set_trace()
#        print z[contor],z[contor+1],z[contor+2],z[contor+3],data_de_azi,'OTP'
        contor = contor + 4


def main():
    cecbank()

if __name__ == "__main__":
    main()
