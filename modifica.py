import vanzare
import adauga


def modificaUI(list):
    """
    Functie care modifica vanzarea cu id-ul ID.
    input:  list - lista de Vanzari
            ID - string
    """
    print("Introduceti ID-ul vanzarii pe care doriti sa o modificati:")
    ID = input("ID > ")

    index = -1
    for v in list:
        if v.getID() == ID:
            index = list.index(v)

    if(index == -1):
        print('Nu exista vanzare cu acest ID!')
        return

    print("Introduceti noile date sau lasati liber daca nu doriti sa modificati:")
    titlu = input("Titlu > ")
    gen = input("Gen > ")
    pretString = input("Pret > ")
    if(pretString != ''): pret = float(pretString)
    else: pret = -1

    reducere = input("Reducere > ")
    if(reducere == ''): reducere = list[index].getReducere()

    validareVanz = vanzare.Vanzare('NO', titlu, gen, pret, reducere)
    try:
        adauga.validare(validareVanz)
    except Exception as ex:
        print(str(ex))
        return

    modifica(list, ID, titlu, gen, pret, reducere)


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


def test_modifica():
    van1 = vanzare.Vanzare(1, 1, 1, 1, 'none')
    van2 = vanzare.Vanzare(2, 2, 2, 2, 'none')
    van3 = vanzare.Vanzare(3, 3, 3, 3, 'none')
    van22 = vanzare.Vanzare(2, 22, 22, 22, 'none')
    list = [van1, van2, van3]

    # vanzare.printList(list)

    modifica(list, 2, 22, 22, 22, 'none')
    assert vanzare.matchList(list, [van1, van22, van3])

    modifica(list, 4, 'ion', 'real', 34.5, 'silver')
    assert vanzare.matchList(list, [van1, van22, van3])

    modifica(list, 1, 'mara', 'real', 5, 'none')
    vanMara = vanzare.Vanzare(1, 'mara', 'real', 5, 'none')
    assert vanzare.matchList(list, [vanMara, van22, van3])


def run(list):
    modificaUI(list)


def teste():
    test_modifica()
