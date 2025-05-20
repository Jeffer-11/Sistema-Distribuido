#!/usr/bin/env python3
# hello World

# mensaje = 'hola Mundo'
# b = 5
# a = 5
# suma = a + b
# vaiable=True
# print(mensaje, "La suma es:", suma)

# #listas
# list = [1,3,3,5,6,'Bone',True]
# print(list[2])
# print(list[3])
# #Dictionary
# dict = {'estudiante1':'Jefferson Bone','estudiante2':'Juan Mera' }
# print(dict['estudiante2'])

# vstring='3'
# v2int=[type(vstring)]
# vnint=[type(v2int)]
# print('-------------------------------------------------------------------------')
# edad= 30
# mes1= 'Usted es mayor'
# ms2 = 'usted es joven'

# if edad>=30:
#     print(mes1)
# else:
#     print(ms2)


# if edad>30:
#     print(mes1)
# elif edad<30:
#     print(ms2)
# elif edad==30:
#     print('Tienes la edad perfecta')


# print('-------------------------------------------------------------------------')

# for i in list:
#     print('Elementos de la lista:' ,i)


# print('-------------------------------------------------------------------------')
# for key  in dict:
#     print(dict[key])

# def mensaje():
#     print('Hola te eh hackeado')

# mensaje()

# for i in range (10):
#     mensaje()


# print('-------------------------------------------------------------------------')

# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))

# def mensaje1(nombre, edad):
#     print("Tú eres joven y guapo :)")
#     print(f'Tu nombre es: {nombre} y tu edad es: {edad}') 

# def mensaje2(nombre, edad):
#     print('Tú estás viejo y feo *_*')
#     print(f'Tu nombre es: {nombre} y tu edad es: {edad}') 

# if edad < 30:
#     mensaje1(nombre, edad)
# elif edad > 50:
#     mensaje2(nombre, edad)
# else:
#     print('Estás en la flor de la vida 😎')
#     print(f'Tu nombre es: {nombre} y tu edad es: {edad}')

# while True:
#     nombre = input('Ingrese su nombre: ')
    
#     try:
#         edad = int(input('Ingrese su edad: '))
#     except ValueError:
#         print("Por favor, ingrese una edad válida (número entero).")
#         continue

#     if edad < 30:
#         print("Tú eres joven y guapo :)")
#     elif edad > 50:
#         print("Tú estás viejo y sabio *_*")
#     else:
#         print("Estás en la flor de la vida 😎")

#     print(f'Tu nombre es: {nombre} y tu edad es: {edad}')

#     opcion = input("\n¿Deseas ingresar otro nombre y edad? (s/n): ").lower()
#     if opcion != 's':
#         print("Programa finalizado.")

#         break
# print('-------------------------------------------------------------------------')

# import math
# list = [1,2,3,4,5,6]
# listavacia= []

# for item in list:
#     listavacia.append(item**2)

# for item in listavacia:
#     print(item)

# listadenumero=[]

# for item in list:
#     listadenumero.append(math.sqrt(item))
    
# print ('SQUARE ROOT FROM MY LIST')

# for i in listadenumero:
#     print(i)

# print('-------------------------------------------------------------------------')

# def prediccion(edad):
#     edad = edad + 20
#     return edad

# def mensaje(nombre, edad_prediccion):
#     print(f'Tu nombre es {nombre} y tu edad dentro de 20 años será {edad_prediccion}')

# while True:
#     nombre = input('Ingrese su nombre: ')
#     edad = int(input('Ingrese su edad: '))
#     edad_prediccion = prediccion(edad)
#     mensaje(nombre, edad_prediccion)

# print('--------------------------------CONECTORES LIST-----------------------------------------')

# listanumero = list()

# listanumero.append(1)
# listanumero.append(2)
# listanumero.append(5)

# for intem in listanumero:
#     print(intem)

# print (listanumero[-1])
# print (listanumero[-2])


# listanumero[-2]='Jefferson'

# for intem in listanumero:
#     print(intem)

# print('--------------------------------CONECTORES LIST-----------------------------------------')
# listanumero.append('Nuevo')

# for intem in listanumero:
#     print(intem)

# print('--------------------------------CONECTORES LIST-----------------------------------------')

# lista2 = listanumero.pop()
# print ('lista: ', listanumero)
# print(lista2)

# print('--------------------------------CONECTORES LIST-----------------------------------------')

# listanueva = list(range(30))
# print(listanueva)
# print('--------------------------------CONECTORES LIST-----------------------------------------')
# itemseleccion = listanueva[10:21]
# print (itemseleccion)

# itemseleccion2 = list()

# for i in itemseleccion:
#     itemseleccion2.append(i +10)
#     print(itemseleccion2)

# itemseleccion2 [10:21]=itemseleccion2
# print(itemseleccion2)

# print('--------------------------------CONECTORES LIST-----------------------------------------')
# itemseleccion2 = list()

# for i in itemseleccion:
#     itemseleccion2.append(i +10)
#     print(itemseleccion2)

# itemseleccion2 [10:21]=itemseleccion2
# print(itemseleccion2)

print('--------------------------------CONECTORES LIST-----------------------------------------')

# lista base de 0 a 19
itemseleccion = list(range(20))

# 1) cada elemento + 10
itemseleccion2 = [i + 10 for i in itemseleccion]

# 2) duplicar la lista (si realmente la necesitas dos veces)
itemseleccion2 = itemseleccion2 + itemseleccion2

# 3) crear una lista nueva con el cuadrado de cada elemento de la original
itemseleccion_cuadrado = [i**2 for i in itemseleccion]

print("Original       :", itemseleccion)
print("Más 10 y duplicada :", itemseleccion2)
print("Elevado al cuadrado:", itemseleccion_cuadrado)

