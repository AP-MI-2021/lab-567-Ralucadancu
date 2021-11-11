
def validare(vanzare):
    """
    Functie care valideaza o datele pentru crearea unei vanzari.
    input:  vanzare
    output: raises exception if there are exceptions
    """
    ex = ''

    red = vanzare.getReducere()
    if (red != 'none' and red != 'silver' and red != 'gold'):
        ex += 'Tip reducere invalid!\n'

    if (ex != ''):
        raise Exception(ex)


def test_validare():
    van = vanzare.Vanzare('1', 'Ion', 'realism', 10.4, 'none')
    try:
        validare(van)
    except Exception as ex:
        assert False

    van = vanzare.Vanzare('2', 'Ion', 'realism', 10.4, '')
    try:
        validare(van)
        assert False
    except Exception as ex:
        assert (str(ex) == 'Tip reducere invalid!\n')

    van = vanzare.Vanzare('3', 'Ion', 'realism', 10.4, 'GOLD')
    try:
        validare(van)
        assert False
    except Exception as ex:
        assert (str(ex) == 'Tip reducere invalid!\n')


def adauga(list, vanzare):
    """
    Functie care adauga in lista 'list' vanzarea 'vanzare'
    input:  list - lista
            vanzare - Vanzare
    """
    list.append(vanzare)


def run(list):
    if (vanzare != None):
        adauga(list, vanzare)


def sterge(list, ID):
    """
    Functie care sterge din lista 'list' toate obiectele de tip Vanzare care au ID-ul 'ID'
    input:  list - lista de Vanzari
            ID - string
    output: -
    """
    for vanzare in list:
        if vanzare.getID() == ID:
            list.pop(list.index(vanzare))



def run(list):
    print("Introduceti ID-ul vanzarii pe care doriti sa o stergeti:")
    ID = input("ID > ")

    sterge(list, ID)

import vanzare


def modificaGen(list,titlu,gen):
    """
    Functie care modifica fiecare vanzare din 'list' care are titlul 'titlu', modificandu-i genul in 'gen'.
    input:  list - lista de vanzari
            titlu - string
            gen - string
    """
    for v in list:
        if v.getTitlu() == titlu:
            v.setGen(gen)


def run(list):
    print("Introduceti titlul si genul pe care doriti sa i-l dati:")
    titlu = input("titlu > ")
    gen = input("gen > ")
    modificaGen(list,titlu,gen)

def modifica(list, ID, titlu, gen, pret, reducere):
    """
    Functie care modifica vanzarea cu ID-ul 'ID' in functie de datele din parametrii.
    """
    for v in list:
        if v.getID() == ID:
            if (titlu != ''):
                v.setTitlu(titlu)
            if (gen != ''):
                v.setGen(gen)
            if (pret != -1):
                v.setPret(pret)
            if (reducere != ''):
                v.setReducere(reducere)
