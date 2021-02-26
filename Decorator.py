def f(func):
    
    def ha(*args , **kwargs) : 
        print("begin")
        func()
        print("end")
    return func

@f
def f1(a=10,b=9) : 
    print(a)
    print(b)


f1()
