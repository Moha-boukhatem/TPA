################### NaiveStringMatching ##################

import timeit



class Naive ():
    
    def __init__ ( self , text ) : 

        self.text = text

    def find ( self,pattern ):
        
        i = 0
        
        tab = []
        pattern = pattern.lower()
        text = self.text.lower()

        start = timeit.default_timer()             
        while i < len(text)-len(pattern):
            
            j = 0

            while j < len(pattern) : 
            
                if text [i+j] != pattern [j] :
                    break

                j+=1
                
                if j == len(pattern):
                    print("position : ",i)
                    
            i+=1
        stop = timeit.default_timer()
        print('Time: ', stop - start)

Texte = Naive("123456789")#input("Passez le Texte : "))


Texte.find("8")#input("Passez la chaine a Rechercher : "))


