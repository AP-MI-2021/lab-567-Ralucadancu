import vanzare


def create():
    """
    Functie care creeaza un obiect de tip Vanzare in functie de datele introduse de user.
    input: -
    outpu: vanzare - obiect de tip Vanzare
    """
    print("Introduceti datele pentru vanzare:")
    ID = input("ID > ")
    titlu = input("Titlu > ")
    gen = input("Gen > ")
    pret = float(input("Pret > "))
    reducere = input("Reducere > ")

    vanzareNoua = vanzare.Vanzare(ID, titlu, gen, pret, reducere)
    try:    
        validare(vanzareNoua)
    except Exception as ex:
        print(str(ex))
        return

    return vanzare.Vanzare(ID, titlu, gen, pret, reducere)


def validare(vanzare):
    """
    Functie care valideaza o datele pentru crearea unei vanzari.
    input:  vanzare
    output: raises exception if there are exceptions
    """
    ex =''

    red = vanzare.getReducere()
    if(red != 'none' and red != 'silver' and red != 'gold'):
        ex += 'Tip reducere invalid!\n'
    
    if(ex!=''):
        raise Exception(ex)

def test_validare():
    
    van = vanzare.Vanzare('1','Ion', 'realism', 10.4, 'none')
    try:
        validare(van)
    except Exception as ex:
        assert False

    van = vanzare.Vanzare('2','Ion', 'realism', 10.4, '')
    try:
        validare(van)
        assert False
    except Exception as ex:
        assert (str(ex)=='Tip reducere invalid!\n')

    van = vanzare.Vanzare('3','Ion', 'realism', 10.4, 'GOLD')
    try:
        validare(van)
        assert False
    except Exception as ex:
        assert (str(ex)=='Tip reducere invalid!\n')



def adauga(list, vanzare):
    """
    Functie care adauga in lista 'list' vanzarea 'vanzare'
    input:  list - lista
            vanzare - Vanzare
    """
    list.append(vanzare)


def test_adauga():
    list = []
    van = vanzare.Vanzare('1','Ion','umor',40,'silver')
    adauga(list,van)
    assert(list == [van])

    adauga(list,van)
    assert(list == [van, van])



def run(list):
    vanzare = create()
    if(vanzare != None):
        adauga(list, vanzare)


def teste():
    test_validare()
    test_adauga()