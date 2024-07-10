# Se tiene N temperaturas. Se desea calcular su media y
# determinar entre todas ellas cuantas son superiores o iguales a
# esa media

temp = [20.5,10,15,22,5]

media = sum(temp)/len(temp)
sup = []

for e in temp:
    if e >= media:
        sup.append(e)

print("los siguientes valores son superiores o iguales a la media ", sup)


# Escriba el código que dado un vector (máximo
# 200 elementos) ordenado de enteros y con posibles
# repeticiones de valores, obtenga como salida una lista de
# los números ordenados, pero sin repeticiones

vec = [10,12,15,12,7,11,18,15,17,7,21,10,10,19,11]
print(list(set(vec.sort())))



#  Escribir un algoritmo que invierta el orden de los caracteres mostrándolo por
# pantalla. La inversión se hará sin utilizar otro vector auxiliar
vec1 = ["c","a","r","p","e","t","i","t","a","s"]
print(vec[::-1])



# Elaborar un algoritmo que ordene descendentemente un
# vector.

vec2 = [5, 35, 15, 8, 2, 21, 40, 30]
print(vec2.sort(reverse=True))



# Cargar un vector de 10 posiciones con numero enteros, a
# partir de este crear 2 vectores; uno con los números pares y el
# otro con los numero impares, además decir de los vectores
# cual es más grande y el número de elementos en cada vector.

vec3 = [23, 4, 6, 13, 78, 96, 25, 18, 32, 48]
new1_vec3 = []
new2_vec3 = []

for e in vec3:
    if (e % 2) == 0:
        new1_vec3.append(e)
    else:
        new2_vec3.append(e)

print("numeros pares ", new1_vec3)
print("cant de números pares ", len(new1_vec3))

print("numeros impares ", new2_vec3)
print("cant de números impares ", len(new2_vec3))


# Dada una matriz cuadrada A, construya un diagrama de flujo
# que permita determinar si dicha matriz es simétrica. Se
# considera a una matriz simétrica si A (i , j) = A (j , i) y esto se
# cumple para todos los elementos i , j de la matriz.
# A: [[1, 2, 3], [2, 5, 0], [3, 0, 5]]
# B: [[1, 2, 3], [2, 5, 0], [3, 5, 0]]

matriz = [[1, 2, 3], [2, 5, 0], [3, 5, 0]]

sim = True

for e in range(3):
    for i in range(3):
        if matriz[e][i] != matriz[i][e]:
            sim = False