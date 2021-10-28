import vanzare


def pretMinimGen(list):
    """
    Functie care creeaza un dictionar din lista 'list', in care cheia este genul unuei vanzari din lista, iar valoarea este vanzarea cu pret minim al acelui gen.
    input:  list - lista de vanzari
    output: listaPretMin - dictionar
    """
    listPretMin = {}

    for a in list:
        if a.getGen() not in listPretMin:
            pMin = a.getPret()
            for b in list:
                if(b.getGen() == a.getGen() and b.getPret() < pMin):
                    pMin = b.getPret()
            listPretMin[a.getGen()] = pMin

    return listPretMin


def test_pretMinimGem():
    v1 = vanzare.Vanzare(1, 1, 1, 10, 'none')
    v11 = vanzare.Vanzare(11, 1, 1, 1, 'none')
    v2 = vanzare.Vanzare(2, 2, 2, 20, 'silver')
    v22 = vanzare.Vanzare(22, 2, 2, 2.2, 'silver')
    v3 = vanzare.Vanzare(3, 3, "3", 30, 'gold')
    v4 = vanzare.Vanzare(4, 4, 4, 40, 'silver')
    v41 = vanzare.Vanzare(41, 4, 4, 4.4, 'silver')
    v42 = vanzare.Vanzare(42, 4, 4, 0.4, 'silver')
    list = [v1, v11, v2, v22, v3, v4, v41, v42]

    listaMin = pretMinimGen(list)
    assert listaMin == {1: 1, 2: 2.2, "3": 30, 4: 0.4}


def run(list):
    pretMinList = pretMinimGen(list)
    for key,value in pretMinList.items():
        print("Pretul minim pentru genul '{0}' este {1}.".format(key,value))


def teste():
    test_pretMinimGem()
