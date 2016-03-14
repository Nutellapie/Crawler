#!./bin/python
# -*- coding: utf-8 -*-

#from lxml.cssselect import CSSSelector
import requests
from lxml import html
import urlparse
import collections
import datetime
from lxml import etree
import pdb
import datainput
import re
from xml.etree.ElementTree import fromstring


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

'''
def volksbank():

    STARTING_URL = 'http://www.volksbank.ro/ro/AfisareCursValutar'

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    # print (etree.tostring(tree,encoding = unicode, pretty_print = True))
    e = tree.xpath('//tr/td/span/text()')  # 33 - 71 CURS

    contor = 33

    while(contor < 72):
        if contor == 49:
            contor = 51
        import pdb; pdb.set_trace()

        valoare = re.sub(r"[^A-Za-z]+", ' ', str(e[contor]))

        if valoare[0] == ' ':
            datainput.main(valoare[1:4], valoare[1:4], str(
                e[contor + 1]), str(e[contor + 2]), 'VolksBank', data_de_azi)
#            print valoare[1:4],e[contor+1],e[contor+2]
        else:
            datainput.main(valoare[0:3], valoare[0:3], str(
                e[contor + 1]), str(e[contor + 2]), 'VolksBank', data_de_azi)
#            print valoare[0:3],e[contor+1],e[contor+2]


        if contor < 43:
            contor = contor + 5
        elif contor >= 43 and contor < 49:
            contor = contor + 3
        else:
            contor = contor + 3

#    pdb.set_trace()

'''
def alphabank():
    STARTING_URL = 'https://www.alphabank.ro/ro/rate/rate_si_dobanzi.php'
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)

    # print (etree.tostring(tree,encoding = unicode, pretty_print = True))
    e = tree.xpath('//tr[@height="18"]/td[@class="stilTd1"]/text()')
    z = tree.xpath('//tr[@height="18"]/td[@class="stilTd2"]/text()')

    contor = 0

    while contor < len(e):
        valoare = re.sub(r"[^A-Za-z]+", ' ', str(e[contor]))
        valoare_1 = re.sub(r"[^A-Za-z]+", ' ', str(z[contor]))

        datainput.main(valoare[(len(valoare) - 4):(len(valoare) - 1)], valoare[0:(len(
            valoare) - 4)], str(e[contor + 2]), str(e[contor + 3]), 'AlphaBank', data_de_azi)

        datainput.main(valoare_1[(len(valoare_1) - 4):(len(valoare_1) - 1)], valoare_1[0:(
            len(valoare_1) - 4)], str(z[contor + 2]), str(z[contor + 3]), 'AlphaBank', data_de_azi)

#        print valoare[(len(valoare) - 4):(len(valoare) - 1)], valoare[0:(len(
#            valoare) - 4)], str(e[contor + 2]), str(e[contor + 3]), 'AlphaBank', data_de_azi
#        print valoare_1[(len(valoare_1) - 4):(len(valoare_1) - 1)], valoare_1[0:(
#            len(valoare_1) - 4)], str(z[contor + 2]), str(z[contor + 3]), 'AlphaBank', data_de_azi


        contor = contor + 6
#    pdb.set_trace()


def bcr():
    STARTING_URL = 'http://www.bcr.ro/ro/curs-valutar'

    e = fromstring(requests.get("https://www.bcr.ro/ro/curs-valutar",
                                headers={'User-Agent': 'Something'}).text)
    z = e.xpath('//table[@class="overview glaze fullsize"]/tr/td/text()')
    contor = 1

    while contor < len(z):
        print z[contor], z[contor + 1], z[contor + 2], 'BCR', data_de_azi
        contor = contor + 4

    pdb.set_trace()


def raiffeisen():
    STARTING_URL = "https://www.raiffeisen.ro/persoane-fizice/curs-valutar/"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//table/tr/td/text()')

    contor = 4
    import pdb; pdb.set_trace()

    while contor < 122 :
        if(int(float(z[contor+3])) > 0 or int(float(z[contor+4])) > 0):
            datainput.main(str(z[contor + 1]), str(z[contor]), str(z[contor + 3]),
                       str(z[contor + 4]), 'Raiffeisen', data_de_azi)
#            print z[contor+1], z[contor], z[contor + 3], z[contor + 4], 'Raiffeisen', data_de_azi

        contor = contor + 7

#    pdb.set_trace()


def garantibank():
    STARTING_URL = "https://ebank.garantibank.ro/isube/yatirimislemleri/doviz/dovizkur"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/text()')

    contor = 6
    while contor < len(z):
        datainput.main(str(z[contor]), str(z[contor]), str(z[contor + 2]),
                       str(z[contor + 5]), 'GarantiBank', data_de_azi)
#        print z[contor], z[contor + 2], z[contor + 5]
        contor = contor + 7
#    pdb.set_trace()


def piraeus():
    STARTING_URL = "http://www.piraeusbank.ro/Banca/Unelte/curs_ghiseu.html"

    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/span/text()')

    contor = 10
    while (contor < 25):
        valoare_1 = re.sub(r"[^0-9-,-.]+", '', str(z[contor + 1]))
        valoare_2 = re.sub(r"[^0-9-,-.]+", '', str(z[contor + 2]))
        valoare = re.sub(r"[^A-Za-z]+", ' ', str(z[contor]))
        valoare = valoare.strip()
        datainput.main(valoare, valoare, valoare_1, valoare_2,
                        'PiraeusBank', data_de_azi)
#        print valoare, valoare_1, valoare_2
        contor = contor + 3
#    pdb.set_trace()

def bancpost():
    STARTING_URL = "https://www.bancpost.ro/Bancpost/Financiare/Istoric-Curs-Valutar"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//table[@class="forex"]/tbody/tr/td/text()')


    contor = 0
    for i in z:
#        j = re.sub(r'\s+', '', str(i))
        j = "".join(str(i).split())
        print j, contor
        contor = contor + 1

    contor = 2
    while(contor < 54):
        numar, nume = str(z[contor]).split()
#        datainput.main(nume,nume,str(z[contor+2]),str(z[contor+3]),'BancPost',data_de_azi)
        print numar,nume
        contor = contor + 6
#        print nume, nume, z[contor + 2], z[contor + 3],'BancPost',data_de_azi
        pdb.set_trace()

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
        if contor >= 93 :
            break
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
        datainput.main(str(z[contor]), str(z[contor + 1]).strip(), str(z[contor + 3]),
                       str(z[contor + 4]), 'BancaTransilvania', data_de_azi)
        contor = contor + 7
        if contor >= 90:
            break
#        print z[contor], z[contor + 1].strip(), z[contor + 3], z[contor + 4]
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
        datainput.main(str(z[contor]), str(z[contor]), str(
            z[contor + 5]), str(z[contor + 6]), 'BancaRomaneasca', data_de_azi)
#        print z[contor], z[contor + 5], z[contor + 6]
        contor = contor + 7

#    pdb.set_trace()


# PROBLEME LA JPY
def crediteuropebank():
    STARTING_URL = "http://www.crediteurope.ro/dobanzi-cotatii-si-cursuri/cursuri/"
    page = requests.get(STARTING_URL)
    tree = html.fromstring(page.text)
    z = tree.xpath('//tr/td/text()')

    contor = 0
    marire = 0
    prescurtari = ['EUR', 'CHF', 'USD', 'GBP', 'JPY', 'SEK']
    list_contor = 0

    while contor < 25:
        if contor == 16:
            marire = 1
        else:
            marire = 0

        datainput.main(prescurtari[list_contor], str(z[contor]), str(
            z[contor + 2 + marire]), str(z[contor + 3 + marire]), 'CreditEuropeBank', data_de_azi)
#        print prescurtari[list_contor], z[contor], z[contor + 2 + marire], z[contor + 3 + marire]
        contor = contor + 4 + marire
        list_contor = list_contor + 1

#    pdb.set_trace()


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
            z[contor + 1]).strip(), str(z[contor + 2]).strip(), 'CarpaticaBank', data_de_azi)
#        print nume, nume, z[contor + 1].strip(), z[contor + 2].strip(), 'CarpaticaBank', data_de_azi
        contor = contor + 3
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
#        print nume, nume,z[contor+1],z[contor+2],data_de_azi,'LibraBank'
        contor = contor + 3


#    pdb.set_trace()

def otpbank():
    STARTING_URL = "https://www.otpbank.ro/curs-valutar"
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


def apelare() :
    otpbank()    #  EROARE CAUTARE
#    volksbank()
    alphabank()
#    raiffeisen()   EROARE CAUTARE
    garantibank()
    piraeus()
    brdbank()
    bancatransilvania()
    bancaromaneasca()
    crediteuropebank()
    carpaticabank()
    librabank()

def main():
    apelare()

if __name__ == "__main__":
    main()
