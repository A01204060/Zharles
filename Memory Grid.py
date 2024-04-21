import random
def printString(message):
""" funcion simple de string para que el jugador escriba su nombre """
    for i in range(0, len(message)):
        print(message[i], end=" ")
    print()
    
def numberList():
""" Funcion donde se listan los numeros posible a escoger con sus pares que aparecen en la matriz """
    lista = []
    for i in range(1,17):
        lista.append(i)
    print ("Numeros Posibles: ",lista)
    return lista

def createMatrix():
""" funcion donde se define la matriz y se llena de numeros aleatorios (¡aun no esta terminado) """
    matrix = []
    for i in range (4):
        matrix.append([])
        for j in range (4):
            matrix[i].append("_")
    
    
    return matrix

def createboard():
""" funcion donde se crea la tabla del memorama """c
    board = [["_","_","_","_"],["_","_","_","_"],["_","_","_","_"],["_","_","_","_"]]
    for i in board:
        for j in i:
            print(j," ",end="")
        print()
    return board

    
def main():
    message = str(input("Ingresa nombre de jugador: "))
    printString(message)
    print("-------------------------")
    numberList()
    print("-------------------------")
    createMatrix()
    print("-------------------------")
    createboard()
        
main()
    
    
    
    
    
