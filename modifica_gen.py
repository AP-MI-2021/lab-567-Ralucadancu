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

def test_modificaGen():
    van1 = vanzare.Vanzare(1, 'ion', 1, 10, 'none')
    van2 = vanzare.Vanzare(2, 'plumb', 2, 20, 'silver')
    van3 = vanzare.Vanzare(3, 'ion', 3, 30, 'gold')
    van4 = vanzare.Vanzare(4, '4', 4, 45, 'silver')
    list = [van1,van2,van3,van4]

    modificaGen(list,'ion', 'realism')
    van1R = vanzare.Vanzare(1, 'ion', 'realism', 10, 'none')
    van3R = vanzare.Vanzare(3, 'ion', 'realism', 30, 'gold')
    assert vanzare.matchList(list, [van1R,van2,van3R,van4])

    modificaGen(list,'plumb', 'simbolism')
    van2S = vanzare.Vanzare(2, 'plumb', 'simbolism', 20, 'silver')
    assert vanzare.matchList(list, [van1R,van2S,van3R,van4])

    modificaGen(list, 'nuEste', 'FALS')
    assert vanzare.matchList(list, [van1R,van2S,van3R,van4])



def run(list):
    print("Introduceti titlul si genul pe care doriti sa i-l dati:")
    titlu = input("titlu > ")
    gen = input("gen > ")
    modificaGen(list,titlu,gen)

def teste():
    test_modificaGen()