from Logic.crud import adauga,modificaGen,modifica,sterge,validare
from Logic.Functionalitati import numarTitluriPeGen,pretMinimGen,getDiscount,sort
from Domain.vanzare import vanzare


def run():
    L = [[]]

    while True:
        printMenu()
        cmd = input(">>>")

        if (cmd == ''):
            continue

        elif (cmd == '-1'):
            for i, l in enumerate(L):
                print('\nV', i)
                vanzare.printList(l)

        elif (cmd == '0'):

            vanzare.printList(list)

        elif (cmd == '1'):

            L.append(list)
            adauga.run(list)

        elif (cmd == '2'):

            L.append(list)
            stergere.run(list)

        elif (cmd == '3'):

            L.append(list)
            modifica.run(list)

        elif (cmd == '4'):

            discount.run(list)
            L.append(list)

        elif (cmd == '5'):

            L.append(list)
            modifica_gen.run(list)

        elif (cmd == '6'):

            pret_minim_gen.run(list)

        elif (cmd == '7'):

            L.append(list)
            ordonare.run(list)

        elif (cmd == '8'):

            numar_titluri.run(list)

        elif (cmd == '9'):
            if (len(L) > 1):
                L.pop()

        elif (cmd == 'exit'):
            break

        else:
            print('\nComanda necunoscuta!\n')

def printMenu():
    print()
    print('0. Afiseaza lista')
    print('1. Adauga vanzare')
    print('2. Sterge vanzare')
    print('3. Modifica vanzare')
    print('4. Aplica discount')
    print('5. Modifica genul pentru un titlu dat')
    print('6. Determina pretului minim pentru fiecare gen')
    print('7. Ordonarea vanzarilor crescatoare dupa pret')
    print('8. Afisarea numarului de titluri distincte pentru fiecare gen')
    print('9. Undo')
    print('Tasteaza "exit" ca sa iesi din aplicatie')
    print()

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