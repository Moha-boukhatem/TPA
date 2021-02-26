
################### BRUTE FORCE ##################
import timeit

start = timeit.default_timer()

class turing ():
    
    def __init__ (self , text ) : 

        self.text = text

    def find (self , pattern ):
        
        i = 0
        tab = []
        pattern = pattern.lower()
        text = self.text.lower()
                   
        while i < len(text)-len(pattern) :

            if pattern == text [i:i+len(pattern)] : 
                tab.append(i)
            i+=1
        

        print("pattern trouver "+str(len(tab))+" fois dans :")        
        for i in tab :   
            print(" la position",i)

Texte = turing("123456789")#input("Passez le Texte : "))
Texte.find("5")#input("Passez la chaine a Rechercher : "))

stop = timeit.default_timer()

print('Time: ', stop - start) 