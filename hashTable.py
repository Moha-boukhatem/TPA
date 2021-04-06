class hashTable : 

    def __init__(self , size) : 

        self.tab = [None]*size
        self.size = size

    def insert_tab(self,nom,matricule) : 

        nom=nom.lower()
        hash = hash_func(nom)
        a = False
        value = []
        value.append(nom)
        value.append(matricule)
        i = 0

        while i < 50 :
            if self.tab[hash] is None :
                self.tab.insert(hash,value)
                a = True
                break
            hash+=1
            hash = hash % self.size
            i += 1

        if a != True :
            print("aucun espace disponible pour ",nom," avec matricule ",matricule)
        else : print("bien enregistrer pour ",nom," avec matricule ",matricule)
        
    def print_table(self) : 
        print(self.tab)    

    def print_element(self,nom) :

        nb,i= 0,0
        nom=nom.lower()

        for element in self.tab :

            if element == None : 
                
                continue    
        
            elif element[0] == nom : 
                nb+=1
                ele = element
                if nb > 1 : 
                    break 

        if nb == 0 :
            print("indisponible")

        elif nb == 1 :


            if ele[0] == nom : 
                print(ele[0]," ",ele[1])

        elif nb > 1 : 
            print("collision")

def hash_func(nom):

    somme = 0
    for i in nom :
        somme += ord(i) 
    somme = somme % 50
    return somme   

table = hashTable(50)

table.insert_tab("mohamed",12)
table.insert_tab("f",12)
table.insert_tab("B",31)
table.insert_tab("f",1)
table.insert_tab("amine",4)



table.print_table()
table.print_element("f")