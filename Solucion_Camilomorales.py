from random import random
from timeit import default_timer
import sys

# FUNCIONES
def imprimir_v(vector):
    print("El tamaño de la lista es: ", len(vector))
    print("Los elementos son: ")
    for k in vector:
        print(k, end=" - ")

# Leer manualmente los datos de un vector        
def leer_datos(vector, num):
    for i in range(num):
        x = int(input("Deme un valor?: "))
        vector.append(x)  #Insertar un elemento en la lista
# genera un vector con una muestra aleatoria de tamaño num 
def generar_datos(vector, num):
    for i in range(num):
        x=int(random()*1000) + 1 # Genera un número entre 1 y 100 
        vector.append(x)  #Insertar un elemento en la lista
#Leer los datos de un archivo de texto
def leer_archivo(vector, archivo):
    file=open(archivo, 'r') #Abrir el archivo
    for l in file:
        valor=int(l.strip()) #Remueve espacios en blanco
        vector.append(valor)
    file.close()  #Cierro el archivo

def Leertxt(vector, archivo):
    NombreArchivo=str(input())
    with open(NombreArchivo)as file:
        for line in file:
             valor=int(l.strip()) #Remueve espacios en blanco
             vector.append(valor)
    file.close()  #Cierro el archivo

def promedio(vector):
    suma =0    
    for i in vector:
        suma +=i
    prom = suma/(len(vector))
    return(prom)


"""
Ordena el vector utilizando el algoritmo de la burbuja 
 y muestra por pantalla el tiempo de ejecución 
"""

def algBurbuja(v):
    print("****** Algoritmo de Ordenacion BURBUJA")                 
    print('\n')                                             
    cont=0                                                  #1
    for i in range(0, len(v)-1):                            #4
        for j in range(len(v)-1,i, -1):                     #6
            if (v[j]<v[j-1]):                               #4
                temp=v[j]                                   #2
                v[j]=v[j-1]                                 #4
                v[j-1]=temp                                 #3
                cont+=1                                     #1
    imprimir_v(v)
    print('\n')
    print("***************** Listo Ordenada la lista *******************...")
    print('\n')
    print("La cantidad de Operaciones Elementales son: ",cont)
               
        #print("Ronda: ", i+1)
        #print(v)
        #input(".. Esperar ..")
                
                
def ord_burbuja_mej(v):
    i=0
    sw=False
    while((i<len(v)-1) and not (sw)):
        sw=True
        for j in range(len(v)-1,i, -1):
            #print("J=",j)
            if (v[j]<v[j-1]):
                temp=v[j]
                v[j]=v[j-1]
                v[j-1]=temp
                sw=False
        #print("Ronda: ", i+1)
        #print(v)
        #input(".. Esperar ..")
        i=i+1

"""
Ordena el vector utilizando el algoritmo de selección 
y muestra por pantalla el tiempo de ejecución 
"""
def algSeleccion(v):
    print("****** Algoritmo de Ordenacion POR SELECCION")
    cont=0
    
    # i indica cuántos elementos se ordenaron   
    for i in range(len(v)-1):                                   #3
        # Para encontrar el valor mínimo del segmento sin clasificar
        # Primero asumimos que el primer elemento es el más bajo
        menor = i                                               #2
        # Luego usamos j para recorrer los elementos restantes
        for j in range(i+1, len(v)-1):                          #5
            # Actualice el menor si el elemento en j es más bajo que él
            if v[j] < v[menor]:                                 #3
                menor = j                                       #2
                cont+=1
        # Después de encontrar el elemento más bajo de las regiones sin clasificar, intercambie con el primer elemento sin clasificar
        v[i], v[menor] = v[menor], v[i]                         #5
        cont+=1
    imprimir_v(v)
    print('\n')
    print("***************** Listo Ordenada la lista *******************...")
    print('\n')
    print("La cantidad de Operaciones Elementales son: ",cont)


"""    
Ordena el vector utilizando el algoritmo de inserción 
y muestra por pantalla el tiempo de ejecución 
"""
def algInsercion(v):
    cont=0
    print("****** Algoritmo de Ordenacion POR INSERCION")
      # Recorrer a través de 1 a len(arr)
    for i in range(1, len(v)):                 #3                   
        Lista = v[i]                           #2
        # Mueve elementos de v[0..i-1], que son
        # mayor que clave, a una posición por delante
        # de su posición actual
        j = i-1                                #2
        cont+=1  
        while j >= 0 and Lista < v[j] :        #5
                v[j + 1] = v[j]                #4
                j -= 1                         #2
                cont+=1
        v[j + 1] = Lista                       #2
    #cont+=1
    imprimir_v(v)
    print('\n')
    print("***************** Listo Ordenada la lista *******************...")
    print('\n')
    print("La cantidad de Operaciones Elementales son: ",cont)

      
"""
Ordena el vector utilizando el algoritmo mergesort 
y muestra por pantalla el tiempo de ejecución 
"""

def algMergeSort(v):

    cont=0
        
    if len(v) > 1:
    # Encontrar la mitad de la matriz
        mid = len(v)//2
  
       # Dividiendo los elementos del arreglo
        L = v[:mid]
        R = v[mid:]
  
        # Ordenando la primera mitad
        algMergeSort(L)
        algMergeSort(R)
  
        i=0
        j=0
        k=0

        cont+=1
  
       #Copiar datos a matrices temporales i,j
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                v[k] = L[i]
                i += 1
            else:
                v[k] = R[j]
                j += 1
            k += 1

            cont+=1
  
        # Comprobando si quedó algún elemento
        while i < len(L):
            v[k] = L[i]
            i += 1
            k += 1

            cont+=1
  
        while j < len(R):
            v[k] = R[j]
            j += 1
            k += 1

            cont+=1

    #print("La cantidad de Operaciones Elementales son: ",cont)
    #print('\n')
        
"""
Ordena el vector utilizando el algoritmo quicksort 
y muestra por pantalla el tiempo de ejecución 
"""

def particion(v, izquierda, derecha):
    
    cont=0

    pivote = v[izquierda]
    
    cont+=1

    while True:
        # Mientras cada elemento desde la izquierda esté en orden (sea menor que el
        # pivote) continúa avanzando el índice
        while v[izquierda] < pivote:
            izquierda += 1

            cont+=1

        # Mientras cada elemento desde la derecha esté en orden (sea mayor que el
        # pivote) continúa disminuyendo el índice
        while v[derecha] > pivote:
            derecha -= 1
        if izquierda >= derecha:
            return derecha
        else:
            v[izquierda], v[derecha] = v[derecha], v[izquierda]
            izquierda += 1
            derecha -= 1
            
            cont+=1

            #print("La cantidad de Operaciones Elementales son: ",cont)
           # print('\n')


def algQuickSort(v, izquierda, derecha):

    cont=0

    if izquierda < derecha:
        indiceParticion = particion(v, izquierda, derecha)
        algQuickSort(v, izquierda, indiceParticion)
        algQuickSort(v, indiceParticion + 1, derecha)

        cont+=1
        
    #print('\n')
    #print("La cantidad de Operaciones Elementales son: ",cont)
    #print('\n')
            
# Código del programa
print("** BIENVENIDO **")
Timeinicio = default_timer()

# Código a medir
# -------------

v=[]  #declaro una lista vacia
#print(type(v))
#num = int(input("Número de elementos?: "))
#print(type(num))
#Leer datos manualmente
#leer_datos(v,num)
#Generar datos randomicamente
#generar_datos(v,num)
#Leer datos de un archivo
#leertxt(v, archivo)
print('\n')
OpA='Entrada-800.txt'
OpB='Entrada-8000.txt'
OpC='Entrada-80000.txt'

print("Menu Seleccion Archivo")
print("A, Archivo Lista de 800 Elementos")
print("B, Archivo Lista de 8000 Elementos")
print("C, Archivo Lista de 80000 Elementos")

Opc=input("Seleccione la Opcion de Archivo: ")

if Opc == "A":
    leer_archivo(v, OpA)   
elif Opc == "B":
    leer_archivo(v, OpB)
elif Opc == "C":
    leer_archivo(v, OpC)
else:
    print("El valor no es valido")
    
#generar_datos(v, 10)
imprimir_v(v)

print('\n')

Alg1=algBurbuja
Alg2=algSeleccion
Alg3=algInsercion
Alg4=algMergeSort
Alg5=algQuickSort

print("Menu Seleccion Archivo")
print('\n')
print("1, Metodo Ordenacion BURBUJA")
print("2, Metodo Ordenacion SELECCION")
print("3, Metodo Ordenacion INSERCION")
print("4, Metodo Ordenacion MERGE SORT")
print("5, Metodo Ordenacion QUICK SORT")
print('\n')
OpcAlg=input("Seleccione una Opcion de Algoritmo de Selecion: ")
print('\n')
if OpcAlg == "1":
    Alg1(v)
elif OpcAlg == "2":
    Alg2(v)
elif OpcAlg == "3":
    Alg3(v)
elif OpcAlg == "4":
    cont=+1
    print("****** Algoritmo de Ordenacion MERGE SORT")
    print('\n')
    Alg4(v)
    print('\n')
    imprimir_v(v)
    
elif OpcAlg == "5":
    print("****** Algoritmo de Ordenacion QUICK SORT")
    print('\n')
    Alg5(v, 0, len(v) - 1)
    print('\n')
    imprimir_v(v)
    
else:
    print("El valor no es valido")

#algBurbuja(v)
#ord_burbuja_mej(v)
#algSeleccion(v)
#algInsercion(v)
#algMergeSort(v)
#algQuickSort(v, 0, len(v) - 1)
#Imprimir datos ordenados

print('\n')
#imprimir_v(v)
#print("Promedio de los valores es {0:,.2f}".format(promedio(v)))
Timefin = default_timer()
print("Tiempo de Ejecucion: ", [Timefin-Timeinicio])
print("DESARROLLADO POR: JOSE ARMANDO BENAVIDES CANCHALA Y JUAN CAMILO MORALES LOPEZ.")
a=input()


