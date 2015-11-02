#!./bin/python

import ZODB, ZODB.FileStorage
import transaction
from persistent import Persistent
import zope.interface

class BazaDeDate (object):
    def __init__(self,path):
        self.storage = ZODB.FileStorage.FileStorage(path)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()
    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()

class EntryDB (Persistent) :
    def __init__(self, Simbol, Nume, Curs_Vanzare, Curs_Cumparare, Sucursala, Timp) :
        self.Id = str(Sucursala) + '-' + str(Simbol) + '-' + str(Timp)
        self.Simbol = Simbol
        self.Nume = Nume
        self.Curs_Cumparare = Curs_Cumparare
        self.Curs_Vanzare = Curs_Vanzare
        self.Sucursala = Sucursala
        self.Timp = Timp

def main (_presc , _denumire , _valuta_cumparare, _valuta_vanzare , _sucursala , _timp) :
    db = BazaDeDate('./Data.fs')
    dbroot = db.dbroot

    item = EntryDB(_presc, _denumire , _valuta_cumparare, _valuta_vanzare , _sucursala , _timp)
#    import pdb; pdb.set_trace()
    dbroot[item.Id] = item
    transaction.commit()
    db.close()

if __name__ == "__main__":
    main()
