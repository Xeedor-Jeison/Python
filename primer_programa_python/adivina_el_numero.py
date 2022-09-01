import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("""
    Bienvenido a nuestro juego de adivina el numero 
    Le explicare brevemente la mecanica del juego
    Nuestro sistema colocara un numero aleatorio el cual tendra que adivinar 
    Para darle mas emocion usted cuenta con: 5 vidas 
    Asi que empecemos, elija un numero del 1 al 100: """))
    vidas = 5
    while numero_elegido != numero_aleatorio:
        if vidas == 0:
            print('GAME OVER')
            break
        if numero_elegido < numero_aleatorio:
            vidas -= 1
            print('Busca un numero mas grande, te quedan ' + str(vidas) + " vidas" )
        elif numero_elegido > numero_aleatorio:
            vidas -=1
            print('Busca un numero mas pequeño, te quedan ' + str(vidas) + ' vidas')
        
        numero_elegido = int(input('Elige otro numero: '))
    if numero_aleatorio == numero_elegido:
        print (' GANASTE')



if __name__ == '__main__':
    run()