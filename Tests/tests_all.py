from Logic.Functionalitati import numarTitluriPeGen,pretMinimGen,sort,getDiscount
from Logic.crud import adauga,sterge,modificaGen,modifica

def test_adauga():
    list = []
    van = vanzare.Vanzare('1', 'Ion', 'umor', 40, 'silver')
    adauga(list,van)
    assert(list == [van])

    adauga(list,van)
    assert(list == [van, van])

def test_getDiscount():
    assert(getDiscount('silver') == 5/100)
    assert(getDiscount('gold') == 10/100)
    assert(getDiscount('none') == 0)
    assert(getDiscount('fdsj') == 0)
    assert(getDiscount('') == 0)

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

def test_modificaGen():
    van1 = vanzare.Vanzare(1, 'ion', 1, 10, 'none')
    van2 = vanzare.Vanzare(2, 'plumb', 2, 20, 'silver')
    van3 = vanzare.Vanzare(3, 'ion', 3, 30, 'gold')
    van4 = vanzare.Vanzare(4, '4', 4, 45, 'silver')
    list = [van1,van2,van3,van4]

    modificaGen(list,'ion', 'realism')
    van1R = vanzare.Vanzare(1, 'ion', 'realism', 10, 'none')
    van3R = vanzare.Vanzare(3, 'ion', 'realism', 30, 'gold')
    assert vanzare.matchList(list, [van1R, van2, van3R, van4])

    modificaGen(list,'plumb', 'simbolism')
    van2S = vanzare.Vanzare(2, 'plumb', 'simbolism', 20, 'silver')
    assert vanzare.matchList(list, [van1R, van2S, van3R, van4])

    modificaGen(list, 'nuEste', 'FALS')
    assert vanzare.matchList(list, [van1R, van2S, van3R, van4])

def test_numarTitluriPeGen():
    v1 = vanzare.Vanzare(1, 1, 1, 10, 'none')
    v11 = vanzare.Vanzare(11, 1, 1, 1, 'none')
    v2 = vanzare.Vanzare(2, 2, 2, 20, 'silver')
    v22 = vanzare.Vanzare(22, 22, 2, 2.2, 'silver')
    v3 = vanzare.Vanzare(3, 3, "3", 30, 'gold')
    v4 = vanzare.Vanzare(4, 4, 4, 40, 'silver')
    v41 = vanzare.Vanzare(41, 41, 4, 4.4, 'silver')
    v42 = vanzare.Vanzare(42, 42, 4, 0.4, 'silver')
    list = [v1, v11, v2, v22, v3, v4, v41, v42]

    dic = numarTitluriPeGen(list)
    assert(dic == {1: 1, 2: 2, "3": 1, 4: 3})

def test_sort():
    v1 = vanzare.Vanzare(1, 1, 1, 10, 'none')
    v11 = vanzare.Vanzare(11, 1, 1, 1, 'none')
    v2 = vanzare.Vanzare(2, 2, 2, 20, 'silver')
    v22 = vanzare.Vanzare(22, 2, 2, 2.2, 'silver')
    v3 = vanzare.Vanzare(3, 3, "3", 30, 'gold')
    v4 = vanzare.Vanzare(4, 4, 4, 40, 'silver')
    v41 = vanzare.Vanzare(41, 4, 4, 4.4, 'silver')
    v42 = vanzare.Vanzare(42, 4, 4, 0.4, 'silver')
    list = [v1, v11, v2, v22, v3, v4, v41, v42]

    sort(list)
    assert vanzare.matchList(list, [v42, v11, v22, v41, v1, v2, v3, v4])

    sort(list)
    assert vanzare.matchList(list, [v42, v11, v22, v41, v1, v2, v3, v4])

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


def test_sterge():
    van1 = vanzare.Vanzare(1, 1, 1, 1, 'none')
    van2 = vanzare.Vanzare(2, 2, 2, 2, 'none')
    van3 = vanzare.Vanzare(3, 3, 3, 3, 'none')

    list = [van1, van2, van3]

    sterge(list, van2.getID())
    assert (list == [van1, van3])

    sterge(list, van1.getID())
    assert (list == [van3])

    sterge(list, van3.getID())
    assert (list == [])

    sterge(list, van3.getID())
    assert (list == [])
