#!./bin/python

from datainput import BazaDeDate, EntryDB

def main () :
    db = BazaDeDate('./Data.fs')
    dbroot = db.dbroot

    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj,EntryDB) :
            print 'Entry Nou :'
            print 'Id     :', obj.Id
            print 'Simbol :', obj.Simbol
            print 'Nume   :', obj.Nume
            print 'Curs Cumparare  :', obj.Curs_Cumparare
            print 'Curs Vanzare :', obj.Curs_Vanzare
            print 'Sucursala :', obj.Sucursala
            print 'Timp :', obj.Timp
    db.close()


if __name__ == "__main__":
    main()
