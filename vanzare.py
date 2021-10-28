
class Vanzare:
    """
    Clasa pentru reprezentarea ID, titlu, gen, pret si reducere unei vanzari dintr-o librarie
    """

    def __init__(self,ID,titlu,gen,pret,reducere):
        self.ID = ID
        self.titlu = titlu
        self.gen = gen
        self.pret = pret
        self.reducere = reducere

    def setID(self,ID):
        self.ID =ID
        
    def setTitlu(self,titlu):
        self.titlu = titlu
        
    def setGen(self,gen):
        self.gen = gen

    def setPret(self, pret):
        self.pret = pret
 
    def setReducere(self, reducere):
        self.reducere = reducere

    def getID(self):
        return self.ID
        
    def getTitlu(self):
        return self.titlu

    def getGen(self):
        return self.gen

    def getPret(self):
        return self.pret

    def getReducere(self):
        return self.reducere

    def matches(self,other):
        if(self.getID()!=other.getID()): return False
        if(self.getTitlu()!=other.getTitlu()): return False
        if(self.getGen()!=other.getGen()): return False
        if(self.getPret()!=other.getPret()): return False
        if(self.getReducere()!=other.getReducere()): return False
        return True

def printList(list):
    print()
    if(list == []):
        print('Lista este vida!')
        return
    for vanzare in list:
        print('[ID: "{0}", Titlu: "{1}", Gen: "{2}", Pret: {3}, Reducere: "{4}"] '.format(vanzare.getID(),vanzare.getTitlu(), vanzare.getGen(),vanzare.getPret(),vanzare.getReducere()))
    print()

def matchList(list1,list2):
    if(len(list1) != len(list2)):return False
    for i in range(0,len(list1)):
        if(not list1[i].matches(list2[i])): return False
    return True