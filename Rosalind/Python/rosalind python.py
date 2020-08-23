# =============================================================================
#  ----- ejercicio 1, el poema de python -----
# =============================================================================
import this




#%%
# =============================================================================
#  ----- ejercicio 2, el cuadrado de la hipotenusa -----
# =============================================================================
import math
a2 = 57
b2 = 98
hip = (math.sqrt(a2**2 + b2**2))**2

#o mas limpio por simplificacion:
hip = a2**2 + b2**2
print (hip)




#%%
# =============================================================================
#  ----- ejercicio 3, cortar y unir strings -----
# =============================================================================
txt =   'V7HvsAcPffDTg8r2Eq0z5WFP24CZRhKZHw29cJBtw6tXc7bsHKjkv7F65zi87i8JY'\
        'AKHZxDSrFregilegusgJIChVWkKOty9UArtGFSB37xFqsbpr2a6eWvcgaDIqRyLpy'\
        'UJg8QfWnZvldsibiricaF4e87D20RE'
# un string con varias cadenas entre "" consecutivas se une en uno solo
# \ nos indica continuacin de linea, con ambas tecnicas el string queda como uno solo

a3 = 73
b3 = 82
c3 = 142
d3 = 149


final = "".join ([txt[a3:b3+1], " ", txt[c3:d3+1]])

print (final)




#%%
# =============================================================================
#  ----- ejercicio 4, suma de impares por condicionales -----
# =============================================================================

a4 = 4158 
b4 = 9075
tot4 = 0

for i in range((b4+1)-a4):
    if ((a4+i)%2 == 1):
        tot4 = tot4 + (a4+i)
        
print (tot4)


#o mas corto y elegante:

print (sum(range(a4|1, b4+1, 2))) 

# a4|1 es bitwise-or, asegura que arranque con un numero impar. b4+1 es el 
# tope no inclusivo y 2 es el salto, pej de 5 salta a 7, ignora el 6




#%%
# =============================================================================
#  ----- ejercicio 5, abrir, editar texto y exportar texto -----
# =============================================================================


f5 = open('/media/pulpo/SD/python/Rosalind/Python/rosalind_ini5.txt', "r")
g5 = open('/media/pulpo/SD/python/Rosalind/Python/output_ini5.txt', 'w') #evitas destruir original
for x in f5.readlines()[1::2]: #lee las lineas impares, arranca 1 y salta de a 2
    g5.write(x)
    
 



#%%   
# =============================================================================
#  ----- ejercicio 6, contador de palabras con diccionario -----
# =============================================================================

d6 = dict()
f6 = open('/media/pulpo/SD/python/Rosalind/Python/rosalind_ini6.txt').read().split()
#el .read() lo convierte a string y el split a lista de palabras

for word in f6:
    if word in d6:
        d6[word] = d6[word]+1
    else:
        d6[word] = 1

for key, value in d6.items():
    print (key, value)
