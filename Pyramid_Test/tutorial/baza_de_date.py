from persistent import Persistent
from pyramid_zodbconn import get_connection
from persistent.mapping import PersistentMapping
import ZODB
import ZODB.FileStorage
import transaction


class EntryDB (PersistentMapping):

    def __init__(self, Simbol, Nume, Curs, Sucursala, Timp):
        self.Simbol = Simbol
        self.Nume = Nume
        self.Curs = Curs
        self.Sucursala = Sucursala
        self.Timp = Timp


def root_factory(request):
    conn = get_connection(request)
    zodb_root = conn.root()
    if not 'app_root' in zodb_root:
        app_root = EntryDB()
        zodb_root['app_root'] = app_root
        transaction.commit()
    return zodb_root['app_root']

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

def main():
    db = BazaDeDate('./Data.fs')
    dbroot = db.dbroot

    entry_d = EntryDB(_presc, _denumire, _valuta, _sucursala, _timp)
#    import pdb; pdb.set_trace()
    dbroot[_presc] = entry_d
    transaction.commit()
    db.close()


if __name__ == "__main__":
    main()
