import stergere
import vanzare
import adauga
import modifica
import discount
import modifica_gen
import pret_minim_gen
import ordonare
import numar_titluri
import copy


def runTeste():
    adauga.teste()
    stergere.teste()
    modifica.teste()
    discount.teste()
    modifica_gen.teste()
    pret_minim_gen.teste()
    ordonare.teste()
    numar_titluri.teste()

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


def run():

    L = [[]]

    while True:
        printMenu()
        cmd = input(">>>")

        if(cmd==''):
            continue
        
        elif(cmd=='-1'):
            for i,l in enumerate(L):
                print('\nV',i)
                vanzare.printList(l)

        elif(cmd=='0'):
            list = L[-1]
            vanzare.printList(list)

        elif(cmd == '1'):
            list = copy.deepcopy(L[-1])
            L.append(list)
            adauga.run(list)

        elif(cmd == '2'):
            list = copy.deepcopy(L[-1])
            L.append(list)
            stergere.run(list)

        elif(cmd == '3'):
            list = copy.deepcopy(L[-1])
            L.append(list)
            modifica.run(list)

        elif(cmd == '4'):
            list = copy.deepcopy(L[-1])
            discount.run(list)
            L.append(list)

        elif(cmd == '5'):
            list = copy.deepcopy(L[-1])
            L.append(list)
            modifica_gen.run(list)

        elif(cmd == '6'):
            list = L[-1]
            pret_minim_gen.run(list)

        elif(cmd == '7'):
            list = copy.deepcopy(L[-1])
            L.append(list)
            ordonare.run(list)

        elif(cmd == '8'):
            list = L[-1]
            numar_titluri.run(list)

        elif(cmd == '9'):
            if(len(L)>1):
                L.pop()

        elif(cmd == 'exit'):
            break

        else:
            print('\nComanda necunoscuta!\n')


def main():
    runTeste()
    run()
    

main()
