#!./bin/python

from datainput import BazaDeDate, EntryDB


def main():
    db = BazaDeDate('./Data.fs')
    dbroot = db.dbroot

    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, EntryDB):
            print 'Simbol :', obj.Simbol
            print 'Nume : ',  obj.Nume
            print 'Curs : ', obj.Curs
    db.close()


if __name__ == "__main__":
    main()
