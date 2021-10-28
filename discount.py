import vanzare


def getDiscount(reducere):
    """
    Functie care returneaza valoarea discountului in functie de tipul 'reducerii'.
    input:  reducere - string
    output  5/100 - daca reducere == 'silver'
            10/100 - daca reducere == 'gold'
            0 - otherwise
    """
    if(reducere == 'silver'):
        return 5/100
    if(reducere == 'gold'):
        return 10/100
    return 0


def test_getDiscount():
    assert(getDiscount('silver') == 5/100)
    assert(getDiscount('gold') == 10/100)
    assert(getDiscount('none') == 0)
    assert(getDiscount('fdsj') == 0)
    assert(getDiscount('') == 0)


def aplicaDiscount(list):
    """
    Functie care reduce pretul vanzarilor din lista list in functie de tipul reducerii fiecarei vanzari.
    input:  list - lista de vanzari
    output: -
    """
    for v in list:
        oldPret = v.getPret()
        newPret = oldPret * (1 - getDiscount(v.getReducere()))
        v.setPret(newPret)


def test_aplicaDiscount():
    van1 = vanzare.Vanzare(1, 1, 1, 10, 'none')
    van2 = vanzare.Vanzare(2, 2, 2, 20, 'silver')
    van3 = vanzare.Vanzare(3, 3, 3, 30, 'gold')
    van4 = vanzare.Vanzare(4, 4, 4, 45, 'silver')
    list = [van1, van2, van3, van4]

    
    aplicaDiscount(list)
    van1 = vanzare.Vanzare(1, 1, 1, 10, 'none')
    van2 = vanzare.Vanzare(2, 2, 2, 19, 'silver')
    van3 = vanzare.Vanzare(3, 3, 3, 27, 'gold')
    van4 = vanzare.Vanzare(4, 4, 4, 42.75, 'silver')
    assert vanzare.matchList(list, [van1,van2,van3,van4])

    
    aplicaDiscount(list)
    van1 = vanzare.Vanzare(1, 1, 1, 10, 'none')
    van2 = vanzare.Vanzare(2, 2, 2, 18.05, 'silver')
    van3 = vanzare.Vanzare(3, 3, 3, 24.3, 'gold')
    van4 = vanzare.Vanzare(4, 4, 4, 40.6125, 'silver')
    assert vanzare.matchList(list, [van1,van2,van3,van4])


def run(list):
    aplicaDiscount(list)


def teste():
    test_getDiscount()
    test_aplicaDiscount()
