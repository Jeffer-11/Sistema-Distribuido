

import numpy as np

a = np.array({1,2,3,4,5})
print (a.shape)

print('Extrative element of index 2')


b= np.array([[1,2,3],[11,22,33]])
print(b.shape)

print('Extrative element of fow 1 and colum 2: ' , b[1,2])

print (b)

print('ok')



d= np.zeros((3,4))

print(' the matrix  x is: ')
print(d)

e= np.ones((3,4))
print(' the matrix  y is: ')
print(e)

f= np.full((3,4),8)
print(' the matrix  z is: ')
print(f)


h= np.random.randint(1,11,size=(3,4))
print(' the matrix  h is: ')
print(h)

g= np.random.random((5,5))
print(' the matrix  g is: ')
print(g)

j= np.eye(20)
print(' the matrix  j is: ')
print(j)

print(' the submatrix  i is: ')
i= np.random.randint(1,21,size=(3,4))
print(i)

k = i[:2, :2]
print (' the submatrix  k is: ')
print(k)



print(' the submatrix  i is: ')
y= np.random.randint(1,100,size=(7,5))
print(y)

x = y[2:6, 1:4]
print (' the submatrix  x is: ')
print(x)





yx = np.random.randint(1, 100, size=(7, 5))
xz = yx[[0, 6, 6, 0], [0, 0, 4, 4]]

print('The matrix yx is:')
print(yx)
print('The submatrix xz is:')
print(xz)
print(xz.shape)
print(type(xz))
print(xz.ndim)


xd = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print('The matrix xd is:')
print(xd)

bx = np.array([0, 2, 0, 1])
print('The submatrix bx is:')
print(bx)

# Sumar 100 a todos los elementos de xd
n = xd + 100
print('The updated matrix xd is:')
print(n)



p=np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print('The matrix p is:')
print(p)
filter=(p>5)
print('The filter is:')
print(filter)
print(type(filter))
print(filter.ndim)
print(filter.shape)

px = p[filter]
print(type(px))
print(px.shape)
print(px.ndim)
print('The filtered matrix px is:')
print(px)


f=np.random.randint(1,101,size=(7,7))
print(f)
filter1=(f>40)
filter2=(f<60)
print('The filter1 is:')
print(filter1)
print('The filter2 is:')
print(filter2)
f[filter1 & filter2]=0
print('The filtered matrix f is:')
print(f)
print(f.shape)
print(type(f))

# Crear la matriz aleatoria
f = np.random.randint(1, 101, size=(15, 15))
print("Matriz original:")
print(f)

# Crear filtro para valores múltiplos de 10
filter_multiples_of_10 = (f % 10 == 0)

# Reemplazar esos valores por 200
f[filter_multiples_of_10] = 200

print("Matriz después de reemplazar múltiplos de 10 por 200:")
print(f)

# Mostrar forma y tipo de dato
print(f.shape)
print(type(f))


# Crear una matriz aleatoria entre 1 y 100 de tamaño 20x30
f = np.random.randint(1, 101, size=(7, 7))
print("Matriz original:")
print(f)

# Filtrar números impares
filter_impares = (f % 2 != 0)

# Elevar los impares al cuadrado
f[filter_impares] = f[filter_impares] ** 2

print("Matriz después de elevar al cuadrado los impares:")
print(f)

# Mostrar forma y tipo
print(f.shape)
print(type(f))



# Definimos las matrices
w = np.array([[9, 10]])
v = np.array([[12, 13]])
qa = np.array([[1, 2], [4, 5]])

# Suponemos z es la traspuesta de qa
z = qa.T
q = qa  # asumimos que q es igual a qa

# Producto punto entre w y z
tmp1 = np.dot(w, z)

# Producto punto entre v y q
tmp2 = np.dot(v, q)

print('The matrix tmp1 is:')
print(tmp1)
print(type(tmp1))
print(tmp1.shape)

print('The matrix tmp2 is:')
print(type(tmp2))
print(tmp2)
print(tmp2.shape)

# Producto punto de q y v (traspuesta de v para que coincidan las dimensiones)
tmp3 = q.dot(v.T)

print('The matrix tmp3 is:')
print(tmp3)
print(type(tmp3))
print(tmp3.shape)
print(tmp3.ndim)

print('The matrix q is:')
print(qa)

# Suma de matrices
print('The sum of matrix z is:', np.sum(qa))

f = np.random.randint(1, 101, size=(15, 15))
print("Matriz original:")
print(f)

suma_columnas = np.sum(f, axis=0)

print("\nSuma de cada columna:")
print(suma_columnas)
print('Total de elementos de la matriz:', len(suma_columnas))
print(suma_columnas.ndim)
print(suma_columnas.shape)
# Sumar elementos de cada fila
suma_filas = np.sum(f, axis=1)

print("\nSuma de cada fila:")
print(suma_filas)
print('Total de elementos de la matriz:', len(suma_filas))
print(suma_filas.ndim)
print(suma_filas.shape)


promedio_columnas = np.mean(f, axis=0)
promedio_redondeado = np.round(promedio_columnas, 1)
print('El promedio por columna es:',promedio_redondeado)

print('El promedio por fila es:', np.mean(f, axis=1))


#Matriz transpuesta
f = np.random.randint(1, 21, size=(4,4))
print("Matriz original:")
print(f)
print(f.T)

x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
print('The matrix x is:')
print(x)
print('The matrix v is:')
print(v)
resultado = np.empty_like(x)

for i in range(x.shape[0]):      # Recorre filas
    for j in range(x.shape[1]):  # Recorre columnas
        if v[j] == 1:
            resultado[i][j] = x[i][j] + 1
        else:
            resultado[i][j] = x[i][j]

print("La matriz resultante es:")
print(resultado)


vv=np.tile(v,(4,1))
print('The matrix vv is:')
print(vv)
print(x+vv)

print(x+v)

# hstack
a = np.random.randint(1, 8, size=(2,2))

b = np.random.randint(1, 8, size=(2,2))

resultado = np.hstack((a, b))

print("hstack:")
print(resultado)

#vstack

a = np.random.randint(8, 18, size=(2,2))

b = np.random.randint(1, 8, size=(2,2))


resultado = np.vstack((a, b))

print("vstack:")
print(resultado)

