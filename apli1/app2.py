
# pairs key and the other valuer

myDictionary= {'cat':'cute', 'dog': 'friend', 'Donkey': 'hard-word'}

print (myDictionary['Donkey'])

print('cat' in myDictionary)

myDictionary['fish']='wet'

for key in myDictionary:
    value=myDictionary[key]
    print('The %s is %s'%(key,value))


for key, value in myDictionary.items():
    print('the %s is %s '%(key,value))




print('#################################################################')
cuadrados = {x: x**2 for x in range(1, 20)}
print(cuadrados)



print('#################################################################')

animals= {'cat','dog','chicken','hen','monkey'}
print ('fhish' in animals)
animals.add('fhish')
animals.add('Loren')
print(animals)

numerforelement=len(animals)
print(numerforelement)


animals.remove('dog')
print(type(animals))
print(animals)



print('#################################################################')

kiupol = ("perro", "gato", "conejo")

# Convertir a lista
lista_temporal = list(kiupol)
lista_temporal.append("loro")
lista_temporal.remove("gato")

# Volver a tupla
kiupol = tuple(lista_temporal)

print(kiupol)
