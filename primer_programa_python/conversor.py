def conversor_pesos_a_dolar(tipo_pesos, valor_dolar):
    pesos = int(input("""Por favor la cantidad sin puntos ni comas

    Cuantos pesos """ + tipo_pesos+ """ colombianos tienes?: """))
    dolares = pesos / valor_dolar
    pesos = str(pesos)
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + pesos + " pesos Colombianos, que equivalen a $" + dolares + " dolares")

def conversor_dolar_a_pesos(costo_pesos, tipos_pesos):
    dolar = float(input("Cuantos Dolares tienes?: "))
    valor_pesos = dolar * costo_pesos
    dolar = str(dolar)
    valor_pesos = round(valor_pesos,2)
    valor_pesos = str(valor_pesos)
    print("Tienes $" + dolar + " dolares, que equivalen a " + valor_pesos + tipos_pesos)



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
    conversor_pesos_a_dolar("Colombianos", 4417)
elif opcion == "2":
    conversor_pesos_a_dolar("Argentinos", 137)
elif opcion == "3":
    conversor_pesos_a_dolar("Mexicanos", 20)
elif opcion == "4":
    conversor_dolar_a_pesos(4417," pesos Colombianos")
elif opcion == "5":
    conversor_dolar_a_pesos(137," pesos Argentinos")
elif opcion == "6":
    conversor_dolar_a_pesos(20, " pesos Mexicanos")
else:
    print("Selecciona una opcion valida, por favor")
