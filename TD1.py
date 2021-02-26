class table:

    def __init__ (Self,nb):
        Self.nb = nb
        Self.tab = []
        ind=0
        while ind < int(Self.nb):
            Self.tab.append(int(input("chiffre : ")))
            ind+=1

    
    def exo1(Self):
        print()
        print("le tableau : "+ str(Self.tab))
    
    def exo2(Self,find):
        print("il y'a "+str(Self.tab.count(find))+" elements du numero : "+str(find))
        print()

    def exo3(Self):
        tab1=Self.tab[:]
        tab1.sort()
        print("les deux plus grand elements :  "+str(tab1[-1])+" , "+str(tab1[-2]))
        print()
    
    def exo4(Self):
        tab1=Self.tab[:]
        tab1.sort()
        print("le plus grand element :  "+str(tab1[-1]))
        print("le plus petit element :  "+str(tab1[0]))
        print()


    def exo5(Self):            
        tab1= []
        for i in range(len(Self.tab)):
            if Self.tab[i] == 0 :
                tab1.append(i)
                
        print("les index des nombres null : ",end=" ")
        for i in tab1:
            print(""+str(i),end=" ")
        print()

    def exo6(Self):
        pair   = []
        impair = []

        for i in range(len(Self.tab)):
            if Self.tab[i] % 2 == 0:
                pair.append(Self.tab[i])
            else : impair.append(Self.tab[i])

        print("le tableau des pairs : ")
        print(pair)
        print("le tableau des impairs :")
        print(impair)
        print()


    def exo7(Self):
        print("********** ASCII & HEX **********")

        for i in range(len(Self.tab)):  
            print()
            print(Self.tab[i])
            print("ASCII : ",ord(str(Self.tab[i])))
            print("HEX   : ",hex(Self.tab[i]))
        
        print()

nb=input("nb : ")
t=table(nb)

t.exo1()

t.exo2(2)

t.exo3()

t.exo4()

t.exo5()

t.exo6()

t.exo7()




