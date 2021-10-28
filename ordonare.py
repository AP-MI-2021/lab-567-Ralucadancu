import vanzare


def sort(list):
    """
    Functie care sorteaza crescator lista 'list' in functie de pretul vanzarii.
    input:  list - lista de vanzari
    output: -
    """
    list.sort(key=lambda x: x.getPret())


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


def run(list):
    sort(list)

def teste():
    test_sort()
