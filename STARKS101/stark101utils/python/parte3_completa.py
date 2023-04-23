# Parte 3 (Compromisos FRI):

from channel import Channel
from field import FieldElement
from merkle import MerkleTree
from polynomial import interpolate_poly, Polynomial
from tutorial_sessions import part1, part2

cp, cp_eval, cp_merkle, channel, eval_domain = part2()
print("Éxito 1")

# FRI Folding (Plegado FRI):

'''
Nuestro objetivo en esta parte es construir las capas FRI y comprometernos con ellas:
'''

# Generación de dominios:

'''
El primer dominio FRI es simplemente el eval_domain que ya se generó en la Parte 1.
Cada dominio FRI posterior se obtiene tomando la primera mitad del dominio FRI anterior (eliminando la segunda mitad)
y elevando al cuadrado cada uno de sus elementos.
Observe que si se toman los cuadrados de la segunda mitad de cada elemento en eval_domain,
se obtiene exactamente el mismo resultado que si se toman los cuadrados de la primera mitad.
Esto también es cierto para las capas siguientes. Por ejemplo:
'''
print(eval_domain[100] ** 2)
half_domain_size = len(eval_domain) // 2
print(eval_domain[half_domain_size + 100] ** 2)

# La siguiente función toma como argumento el dominio anterior y genera el siguiente.
def next_fri_domain(fri_domain):
    return [x ** 2 for x in fri_domain[:len(fri_domain) // 2]]

# Prueba usando un hash previamente calculado:
from hashlib import sha256
next_domain = next_fri_domain(eval_domain)
assert '5446c90d6ed23ea961513d4ae38fc6585f6614a3d392cb087e837754bfd32797' == sha256(','.join([str(i) for i in next_domain]).encode()).hexdigest()
print('Éxito 2!')

# FRI Folding Operator (Operador de Plegado FRI):

'''
La siguiente función toma como argumentos un polinomio y un elemento del field (beta),
y devuelve el siguiente polinomio "plegado".
'''
def next_fri_polynomial(poly,  beta):
    odd_coefficients = poly.poly[1::2]
    even_coefficients = poly.poly[::2]
    odd = beta * Polynomial(odd_coefficients)
    even = Polynomial(even_coefficients)
    return odd + even

# Prueba de funcionamiento:
next_p = next_fri_polynomial(cp, FieldElement(987654321))
assert '6bff4c35e1aa9693f9ceb1599b6a484d7636612be65990e726e52a32452c2154' == sha256(','.join([str(i) for i in next_p.poly]).encode()).hexdigest()
print('Éxito 3!')

# Juntándolo todo para conseguir la siguiente capa FRI:

'''
La siguiente función toma un polinomio, un dominio y un elemento de field (beta),
y devuelve el siguiente polinomio, el siguiente dominio y la evaluación de este siguiente polinomio en este siguiente dominio.
'''
def next_fri_layer(poly, domain, beta):
    next_poly = next_fri_polynomial(poly, beta)
    next_domain = next_fri_domain(domain)
    next_layer = [next_poly(x) for x in next_domain]
    return next_poly, next_domain, next_layer

# Prueba de funcionamiento:
test_poly = Polynomial([FieldElement(2), FieldElement(3), FieldElement(0), FieldElement(1)])
test_domain = [FieldElement(3), FieldElement(5)]
beta = FieldElement(7)
next_p, next_d, next_l = next_fri_layer(test_poly, test_domain, beta)
assert next_p.poly == [FieldElement(23), FieldElement(7)]
assert next_d == [FieldElement(9)]
assert next_l == [FieldElement(86)]
print('Éxito 4!')

# Generando Compromisos FRI:

'''
El método FRI Commit contiene el bucle principal de Compromiso FRI, retornando:
- Los polinomios FRI.
- Los dominios FRI.
- Las capas FRI.
- Los árboles de Merkle FRI.
'''
def FriCommit(cp, domain, cp_eval, cp_merkle, channel):    
    fri_polys = [cp]
    fri_domains = [domain]
    fri_layers = [cp_eval]
    fri_merkles = [cp_merkle]
    while fri_polys[-1].degree() > 0:
        beta = channel.receive_random_field_element()
        next_poly, next_domain, next_layer = next_fri_layer(fri_polys[-1], fri_domains[-1], beta)
        fri_polys.append(next_poly)
        fri_domains.append(next_domain)
        fri_layers.append(next_layer)
        fri_merkles.append(MerkleTree(next_layer))
        channel.send(fri_merkles[-1].root)   
    channel.send(str(fri_polys[-1].poly[0]))
    return fri_polys, fri_domains, fri_layers, fri_merkles

# Prueba de funcionamiento:
test_channel = Channel()
fri_polys, fri_domains, fri_layers, fri_merkles = FriCommit(cp, eval_domain, cp_eval, cp_merkle, test_channel)
assert len(fri_layers) == 11, f'Expected number of FRI layers is 11, whereas it is actually {len(fri_layers)}.'
assert len(fri_layers[-1]) == 8, f'Expected last layer to contain exactly 8 elements, it contains {len(fri_layers[-1])}.'
assert all([x == FieldElement(-1138734538) for x in fri_layers[-1]]), f'Expected last layer to be constant.'
assert fri_polys[-1].degree() == 0, 'Expacted last polynomial to be constant (degree 0).'
assert fri_merkles[-1].root == '1c033312a4df82248bda518b319479c22ea87bd6e15a150db400eeff653ee2ee', 'Last layer Merkle root is wrong.'
assert test_channel.state == '61452c72d8f4279b86fa49e9fb0fdef0246b396a4230a2bfb24e2d5d6bf79c2e', 'The channel state is not as expected.'
print('Éxito 5!')

# Ejecutando la función con tu objeto channel e imprimiendo la prueba hasta el momento:
fri_polys, fri_domains, fri_layers, fri_merkles = FriCommit(cp, eval_domain, cp_eval, cp_merkle, channel)
print(channel.proof)
print('Parte 3 Completada!')