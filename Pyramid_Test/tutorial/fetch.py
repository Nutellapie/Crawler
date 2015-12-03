#!./bin/python
import datetime
from datainput import BazaDeDate, EntryDB

def main():
    db = BazaDeDate('./Data.fs')
    dbroot = db.dbroot
    data_de_azi = datetime.date.today()
    list_1 = []
    contor = 0
    for key in dbroot.keys():
        obj = dbroot[key]
        if isinstance(obj, EntryDB) and obj.Timp == data_de_azi:
            '''
            print 'Entry Nou :'
            print 'Id     :', obj.Id
            print 'Simbol :', obj.Simbol
            print 'Nume   :', obj.Nume
            print 'Curs Cumparare  :', obj.Curs_Cumparare
            print 'Curs Vanzare :', obj.Curs_Vanzare
            print 'Sucursala :', obj.Sucursala
            print 'Timp :', obj.Timp
            '''

            list_1.append(obj.Id)
            list_1.append(obj.Simbol)
            list_1.append(obj.Nume)
            list_1.append(obj.Curs_Cumparare)
            list_1.append(obj.Curs_Vanzare)
            list_1.append(obj.Sucursala)
            list_1.append(str(obj.Timp))
            contor = contor + 7
    db.close()
    return tuple(list_1)

if __name__ == "__main__":
    main()
