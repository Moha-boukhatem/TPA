import timeit

def operation(n):
    
    a=""
    
    for i in range(n) : 
        i=n
        while i < n : 
            a+="a"
            i = i/2

start = timeit.default_timer()
operation(500000)
end = timeit.default_timer()
print("temps : ",end-start)