import vanzare

def sterge(list,ID):
    """
    Functie care sterge din lista 'list' toate obiectele de tip Vanzare care au ID-ul 'ID'
    input:  list - lista de Vanzari
            ID - string
    output: -
    """
    for vanzare in list:
        if vanzare.getID() == ID:
            list.pop(list.index(vanzare))

def test_sterge():
    van1 = vanzare.Vanzare(1,1,1,1,'none')
    van2 = vanzare.Vanzare(2,2,2,2,'none')
    van3 = vanzare.Vanzare(3,3,3,3,'none')

    list = [van1,van2,van3]
    
    sterge(list,van2.getID())
    assert(list == [van1,van3])

    sterge(list,van1.getID())
    assert(list == [van3])

    sterge(list,van3.getID())
    assert(list == [])

    sterge(list,van3.getID())
    assert(list == [])

def run(list):
    print("Introduceti ID-ul vanzarii pe care doriti sa o stergeti:")
    ID = input("ID > ")

    sterge(list,ID)


def teste():
    test_sterge()