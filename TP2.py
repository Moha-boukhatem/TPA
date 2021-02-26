#python3 version : 3.9.1

import numpy as np

def triangle_generator(number):
    print("\n********** TRIANGLE **********\n")


    plus = "+"
    number =int(number)

    for i in range(number):
        
        space = (number-i-1)*" "
        print(space+""+plus)
        plus+=" +"

def damier_generator(number):
    print("\n********** DAMIER **********\n")


    number =int(number)
    k = number // 2

    for i in range(number):
        print()
        if i % 2 == 0 :
            for j in range(k) :
                plus="+"
                print(plus,end=" ")
                plus="*"
                print(plus,end=" ")

        else : 
            for j in range(k) :
                plus="*"
                print(plus,end=" ")
                plus="+"
                print(plus,end=" ")
    print()

def pascal_pyramid_generator(number):
    print("\n********** PASCAL PYRAMID **********\n")

    number = int(number)
    matrice = np.zeros(shape=(number,number),dtype =int)     
    i = 0
    
    while i < number :
        j=0

        while j < number :
            
            if j == 0 or i == j :
                matrice[i,j]=1
            else : matrice[i,j] = matrice[i-1,j-1] + matrice[i-1,j]
    
            j+=1
        i+=1

    for i in range(len(matrice)):

    

        for j in range(len(matrice)):

            if matrice [i,j] != 0 : 
                print(matrice [i,j]," ",end="")
                
        print()
    print()
    

if __name__=='__main__' :
    
    nb = input("donnez le nombre : ")
    
    triangle_generator(nb)
    
    damier_generator(nb)

    pascal_pyramid_generator(nb)