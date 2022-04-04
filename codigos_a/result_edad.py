def result_edad():
    ac=0
    an=0 
    res=0

    ac=int(input("favor digitar el año actual: "))
    an=int(input("favor digitar el año de nacimiento: "))

    res= ac-an
    
    print("su edad es", res)

result_edad()
