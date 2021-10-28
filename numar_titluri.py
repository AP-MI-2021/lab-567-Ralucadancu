import vanzare


def numarTitluriPeGen(list):
    """
    Functie care returneaza numarul de titluri distincte pentru fiecare gen.
    input:  list - lista de vanzari
    output: dicNrTitluri - dictionar
    """
    dicNrTitluri = {}

    for i,v in enumerate(list):
        if v.getGen() not in dicNrTitluri:
            # daca nu exista genul in dictionar il adaug si setez val = 1
            dicNrTitluri[v.getGen()] = 1
        else:
            # daca deja exista genul in dictionar
            if not any(x.getTitlu() == v.getTitlu() for x in list[0:i]):
                # daca nu exista acest titlu
                dicNrTitluri[v.getGen()] += 1
    return dicNrTitluri


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


def run(list):
    nrTitluri = numarTitluriPeGen(list)
    for key, value in nrTitluri.items():
        print("Genul '{0}' are {1} titlu(ri) distincte.".format(key,value))


def teste():
    test_numarTitluriPeGen()
