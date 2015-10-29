#!./bin/python

import ZODB
import ZODB.FileStorage
import transaction
from persistent import Persistent


class BazaDeDate (object):

    def __init__(self, path):
        self.storage = ZODB.FileStorage.FileStorage(path)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()


class EntryDB (Persistent):

    def __init__(self, Simbol, Nume, Curs, Sucursala, Timp):
        self.Simbol = Simbol
        self.Nume = Nume
        self.Curs = Curs
        self.Sucursala = Sucursala
        self.Timp = Timp


def main(_presc, _denumire, _valuta, _sucursala, _timp):
    db = BazaDeDate('./Data.fs')
    dbroot = db.dbroot

    entry_d = EntryDB(_presc, _denumire, _valuta, _sucursala, _timp)
#    import pdb; pdb.set_trace()
    dbroot[_presc] = entry_d
    transaction.commit()
    db.close()

if __name__ == "__main__":
    main()
