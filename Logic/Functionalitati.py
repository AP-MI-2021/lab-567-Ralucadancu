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




def run(list):
    pretMinList = pretMinimGen(list)
    for key,value in pretMinList.items():
        print("Pretul minim pentru genul '{0}' este {1}.".format(key,value))


def sort(list):
    """
    Functie care sorteaza crescator lista 'list' in functie de pretul vanzarii.
    input:  list - lista de vanzari
    output: -
    """
    list.sort(key=lambda x: x.getPret())


def run(list):
    sort(list)




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

def run(list):
    nrTitluri = numarTitluriPeGen(list)
    for key, value in nrTitluri.items():
        print("Genul '{0}' are {1} titlu(ri) distincte.".format(key,value))

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



