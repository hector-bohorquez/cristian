def conocer_edad():
    ac=0
    an=0 
    res=0

    ac=int(input("favor digitar el año actual: "))
    an=int(input("favor digitar el año de nacimiento: "))

    res= ac-an

    return res

edad=conocer_edad()

print(f"la edad es {edad}")


