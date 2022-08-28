menu = """
Bienvenid@  a nuestro sistema de conversion de monedas activo ⚡
Que proceso desea realizar hoy?

1- Convertir de pesos Colombianos a Dolares
2- Convertir de pesos Argentinos a Dolares
3- Convertir de pesos Mexicanos a Dolares
4- Convertir de Dolares a pesos Colombianos
5- Convertir de Dolares a pesos Argentinos
6- Convertir de Dolares a pesos Mexicanos

Elige una opcion:  """
opcion = input(menu)
if opcion == "1":
    pesos = int(input("""Por favor la cantidad sin puntos ni comas

    Cuantos pesos colombianos tienes?: """))
    valor_dolar = 4393
    dolares = pesos / valor_dolar
    pesos = str(pesos)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + pesos + " pesos Colombianos, que equivalen a $" + dolares + " dolares")
elif opcion == "2":
    pesos = int(input("""Por favor la cantidad sin puntos ni comas

    Cuantos pesos colombianos tienes?: """))
    valor_dolar = 137
    dolares = pesos / valor_dolar
    pesos = str(pesos)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + pesos + " pesos Argentinos, que equivalen a $" + dolares + " dolares")
elif opcion == "3":
    pesos = int(input("""Por favor la cantidad sin puntos ni comas
    
    Cuantos pesos colombianos tienes?: """))
    valor_dolar = 20
    dolares = pesos / valor_dolar
    pesos = str(pesos)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + pesos + " pesos Mexicanos, que equivalen a $" + dolares + " dolares")
elif opcion == "4":
    dolar = float(input("Cuantos Dolares tienes?: "))
    valor_pesos_colombiano = 4393.93
    pesos_colombianos = dolar * valor_pesos_colombiano
    dolar = str(dolar)
    pesos_colombianos = round(pesos_colombianos,2)
    pesos_colombianos = str(pesos_colombianos)
    print("Tienes $" + dolar + " dolares, que equivalen a " + pesos_colombianos + " Pesos Colombianos")
elif opcion == "5":
    dolar = float(input("Cuantos Dolares tienes?: "))
    valor_pesos_argentinos = 137.87
    pesos_argentinos = dolar * valor_pesos_argentinos
    dolar = str(dolar)
    pesos_argentinos = round(pesos_argentinos,2)
    pesos_argentinos = str(pesos_argentinos)
    print("Tienes $" + dolar + " dolares, que equivalen a " + pesos_argentinos + " Pesos Argentinos")
elif opcion == "6":
    dolar = float(input("Cuantos Dolares tienes?: "))
    valor_pesos_mexicanos = 20
    pesos_mexicanos = dolar * valor_pesos_mexicanos
    dolar = str(dolar)
    pesos_mexicanos = round(pesos_mexicanos,2)
    pesos_mexicanos = str(pesos_mexicanos)
    print("Tienes $" + dolar + " dolares, que equivalen a " + pesos_mexicanos + " Pesos Mexicanos")
else:
    print("Selecciona una opcion valida, por favor")
