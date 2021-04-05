# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 10:36:06 2021

@author: Jbeltrant
"""

# TALLER DE VECTORES
# EJERCICIO 1 - TALLER DE VECTORES


def funciones(v):
    import numpy as np
    Sumatoria = int(sum(v))
    Productoria = int(np.prod(v))
    Max_num = int(max(v))
    Min_num = int(min(v))

    return Sumatoria, Productoria, Max_num, Min_num


tam = input("Digíte el tamaño del vector: ")
v = []
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    v.append(elemento)

Sumatoria, Productoria, Max_num, Min_num = funciones(v)

print(f'Sumatoria del vector es: {Sumatoria}')
print(f'Productoria del vector es: {Productoria}')
print(f'Mayor elemento del vector es: {Max_num}')
print(f'Menor elemento del vector es: {Min_num}')


# EJERCICIO 2 - TALLER DE VECTORES
def funciones(v):
    pares, impares, primos = 0, 0, 0
    for elemento in v:
        if elemento % 2 == 0:
            pares += 1
        else:
            impares += 1
        if all(elemento % i != 0 for i in range(2, elemento)):
            primos += 1
    return pares, impares, primos


tam = input("digíte el tamaño del vector: ")
v = []
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    v.append(elemento)

pares, impares, primos = funciones(v)

print(f'{pares} pares, {impares} impares y {primos} primos')


# EJERCICIO 3 - TALLER DE VECTORES
def funciones(a, b):
    import numpy as np
    if len(a) != len(b):
        return 'No son iguales'
    else:
        suma = np.array(a) + np.array(b)
        resta = np.array(a) - np.array(b)
        return suma,  resta


va = []
vb = []
tam = input("Digíte el tamaño del vector 1: ")
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    va.append(elemento)
tamm = input("Digíte el tamaño del vector 2: ")
for i in range(int(tamm)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    vb.append(elemento)

suma, resta = funciones(va, vb)
print(f' {va} + {vb} = {suma}')
print(f' {va} - {vb} = {resta}')


# EJERCICIO 4 - TALLER DE VECTORES
def funcion_repetidos(v):
    r = []
    for x in range(len(v)):
        coun = 0
        for element in v:
            if v[x] == element:
                coun = coun + 1
        r.append(coun)
    max_repetido = r.index(max(r))
    return(v[max_repetido])


tam = input("digíte el tamaño del vector: ")
v = []
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    v.append(elemento)
r = funcion_repetidos(v)
print(f'EL que más se repite es: {r}')

# EJERCICIO 5 - TALLER DE VECTORES


def funcion(v):
    p = 1
    s = 0
    if len(v) % 2 == 0:
        for x in range(len(v)):
            if x < int(len(v) / 2):
                p = p * v[x]
            else:
                s = s + v[x]
    else:
        print("El Vector no es par")
    return p, s


tam = input("Digíte el tamaño del vector: ")
v = []
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    v.append(elemento)
productoria, sumatoria = funcion(v)
print(f'Productoria primera mitad: {productoria}')
print(f'Sumatoria segunda mitad: {productoria}')


# EJERCICIO 6 - TALLER DE VECTORES


def funcion(v):
    if len(v) % 2 == 0:
        i = 1
        for x in range(int(len(v) / 2)):
            if v[x] == v[len(v)-i]:
                i += 1
                s = True
            else:
                s = False
                break
    else:
        v = list(v)
        v.pop(v[int(len(v) / 2)-1])
        v = tuple(v)
        if len(v) % 2 == 0:
            i = 1
            for x in range(int(len(v) / 2)):
                if v[x] == v[len(v)-i]:
                    i += 1
                    s = True
                else:
                    s = False
                    break
    return s


tam = input("digíte el tamaño del vector: ")
v = []
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    v.append(elemento)

simetrico = funcion(v)

if simetrico:
    print('Simetrico')
else:
    print('No Es Simetrico')


# EJERCICIO 7 - TALLER DE VECTORES


def operaciones(va, vb):
    va = set(va)
    vb = set(vb)
    union = va | vb
    interseccion = va & vb
    diferen_A = va - vb
    diferen_B = vb - va

    return union, interseccion, diferen_A,  diferen_B


va = []
vb = []
tam = input("digíte el tamaño del vector 1: ")
for i in range(int(tam)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    va.append(elemento)
tamm = input("digíte el tamaño del vector 2: ")
for i in range(int(tamm)):
    elemento = int(input(f"Elemento  {i+1} del vector: "))
    vb.append(elemento)

union, interseccion, diferen_A,  diferen_B = operaciones(va, vb)
print(f'''
Unión: {union}
Intersección: {interseccion}
Diferencia A y B : {diferen_A}
Diferencia B y A: {diferen_B}
''')

# JABT
