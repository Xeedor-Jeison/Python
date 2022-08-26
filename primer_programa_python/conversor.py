pesos = float(input("Cuantos pesos colombianos tienes?: "))
valor_dolar = 4393
 
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

print("Tienes $" + dolares + " dolares")