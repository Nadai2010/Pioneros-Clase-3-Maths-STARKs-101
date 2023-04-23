# Se importan las funciones y clases necesarias
from field import FieldElement

a = [FieldElement(1), FieldElement(3141592)]
while len(a) < 1023:
    a.append(a[-2] * a[-2] + a[-1] * a[-1])
    
assert len(a) == 1023, 'La traza debe constar exactamente de 1023 elementos.'
assert a[0] == FieldElement(1), 'El primer elemento de la traza debe ser el elemento unitario.'
for i in range(2, 1023):
    assert a[i] == a[i - 1] * a[i - 1] + a[i - 2] * a[i - 2], f'La regla de recursión FibonacciSq no se aplica al índice {i}'
assert a[1022] == FieldElement(2338775057), 'Último elemento incorrecto!'
print('Éxito!')

# Generator:

g = FieldElement.generator() ** (3 * 2 ** 20)
G = [g ** i for i in range(1024)]

assert g.is_order(1024), 'El generador g es de orden incorrecto.'
b = FieldElement(1)
for i in range(1023):
    assert b == G[i], 'El lugar i-th de G no es igual a la potencia i-th de g.'
    b = b * g
    assert b != FieldElement(1), f'g es de orden {i + 1}'
    
if b * g == FieldElement(1): 
# Imprimir un mensaje de éxito si todas las pruebas pasan
    print('Éxito2!')
else:
    print('g es de orden > 1024')
    
# Poly:
    
from polynomial import X
# El polinomio 2x^2 + 1.
p = 2*X**2 + 1
# Evalua p at 2:
print(p(2))
# Escriba el nombre de un polinomio, solo, en la última línea de una celda para visualizarlo
p

from polynomial import interpolate_poly
# Interpolar un polinomio usando la lista G sin su último elemento y el valor a
f = interpolate_poly(G[:-1], a)
v = f(2)

assert v == FieldElement(1302089273)
# Imprimir un mensaje de éxito si todas las pruebas pasan
print('Éxito3!')

# Crear un nuevo generador de campo
w = FieldElement.generator()

# Calcular una constante para generar una lista de 8192 elementos usando el generador w
h = w ** ((2 ** 30 * 3) // 8192)

# Crear una lista de 8192 elementos elevando h a las potencias de 0 a 8191
H = [h ** i for i in range(8192)]

# Crear una lista de 8192 elementos multiplicando cada elemento de H por el generador w
eval_domain = [w * x for x in H]

from hashlib import sha256
# Verificar que no haya elementos duplicados en eval_domain
assert len(set(eval_domain)) == len(eval_domain)
w = FieldElement.generator()

# Calcular el inverso del generador de campo
w_inv = w.inverse()

# Verificar que el segundo elemento de la lista H sea el generador h
assert '55fe9505f35b6d77660537f6541d441ec1bd919d03901210384c6aa1da2682ce' == sha256(str(H[1]).encode()).hexdigest(),\
    'H la lista es incorrecta. H[1] debe ser h (i.e., el generador de H).'
for i in range(8192):

# Verificar que eval_domain se pueda reconstruir a partir de w_inv y el segundo elemento de eval_domain
    assert ((w_inv * eval_domain[1]) ** i) * w == eval_domain[i]

# Imprimir un mensaje de éxito si todas las pruebas pasan
print('Éxito4!')

# Coset:

f = interpolate_poly(G[:-1], a)
f_eval = [f(d) for d in eval_domain]

# Test against a precomputed hash.
from hashlib import sha256
from channel import serialize
assert '1d357f674c27194715d1440f6a166e30855550cb8cb8efeb72827f6a1bf9b5bb' == sha256(serialize(f_eval).encode()).hexdigest()
print('Éxito5!')

# Commitments:

from merkle import MerkleTree

# Creación del objeto MerkleTree para f_eval
f_merkle = MerkleTree(f_eval)

# Comprobación de que el hash del objeto f_eval coincide con un valor predefinido
assert f_merkle.root == '6c266a104eeaceae93c14ad799ce595ec8c2764359d7ad1b4b7c57a4da52be04'
print('Éxito6!')

# Channel:

from channel import Channel

# Creación de un objeto Channel
channel = Channel()

# Envío de la raíz del árbol Merkle a través del canal
channel.send(f_merkle.root)

# Impresión de la prueba de conocimiento cero del canal
print(channel.proof)
print("CHECK")

# Segunda Parte:

from polynomial import interpolate_poly, X, prod

# Impresión de variables importantes para la segunda parte del código
print("a es:", a)
print("g es:", g)
print("G es:", G)
print("h es:", h)
print("H es:", H)
print("eval_domain es:", eval_domain)
print("f es:", f)
print("f_eval es:", f_eval)
print("f_merkle es:", f_merkle)
print("channel es:", channel)
print("Todo está bien")

# First Constraint:

# Definición de las expresiones numéricas y algebraicas de la primera restricción
numer0 = f - 1
denom0 = X - 1

print(numer0) # Impresión de la expresión numérica de la primera restricción
print(denom0) # Impresión de la expresión algebraica de la primera restricción
print("Genial")

numer0 % denom0 # Cálculo del residuo de la división de numer0 entre denom0

p0 = numer0 / denom0 # Definición de la expresión algebraica de la primera restricción como un objeto polinomial

# Verificación de que el valor del objeto polinomial en x=2718 es igual a un valor predefinido
assert p0(2718) == 2509888982
print('Éxito7!')

# Second Constraint:

# Definición de las expresiones numéricas y algebraicas de la segunda restricción
numer1 = f - 2338775057
denom1 = X - g**1022
p1 = numer1 / denom1

# Verificación de que el valor del objeto polinomial en x=5772 es igual a un valor predefinido
assert p1(5772) == 232961446
print('Éxito8!')

# Third Constraint:

lst = [(X - g**i) for i in range(1024)]
prod(lst)

# Composing Polynomials:

# Definir dos polinomios q y r.
q = 2*X ** 2 + 1
r = X - 3

print("Excelente!")

# Componer q y r para obtener un nuevo polinomio cmp.
cmp = q(r)
cmp

# Back to Polynomial Constraints:

# Definir una nueva expresión numer2 que involucra el polinomio f, las variables g y X, y una resta y una potencia.
numer2 = f(g**2 * X) - f(g * X)**2 - f**2
print("Numerator at g^1020 is", numer2(g**1020))
print("Numerator at g^1021 is", numer2(g**1021))

# Definir una nueva expresión denom2 que involucra la variable X y tres valores de la lista g elevados a diferentes potencias.
denom2 = (X**1024 - 1) / ((X - g**1021) * (X - g**1022) * (X - g**1023))

# Definir un nuevo polinomio p2 como la división de numer2 y denom2.
p2 = numer2 / denom2

# Comprobar que el grado de p2 es igual a 1023 y que su valor evaluado en 31415 es igual a 2090051528.
assert p2.degree() == 1023, f'The degree of the third constraint is {p2.degree()} when it should be 1023.'
assert p2(31415) == 2090051528
print('Éxito9!')

# Imprimir los grados de los polinomios p0, p1 y p2.
print('deg p0 =', p0.degree())
print('deg p1 =', p1.degree())
print('deg p2 =', p2.degree())

# Step 4 - Composition Polynomial:

# Definir una nueva función get_CP() que recibe un canal y retorna un polinomio que es la combinación lineal de p0, p1 y p2 con coeficientes aleatorios recibidos a través del canal.
def get_CP(channel):
    alpha0 = channel.receive_random_field_element()
    alpha1 = channel.receive_random_field_element()
    alpha2 = channel.receive_random_field_element()
    return alpha0*p0 + alpha1*p1 + alpha2*p2

# Crear un nuevo canal de prueba y obtener un polinomio de prueba CP_test llamando a la función get_CP() con este canal.
test_channel = Channel()
CP_test = get_CP(test_channel)

# Comprobar que el grado de CP_test es igual a 1023 y que su valor evaluado en 2439804 es igual a 838767343.
assert CP_test.degree() == 1023, f'The degree of cp is {CP_test.degree()} when it should be 1023.'
assert CP_test(2439804) == 838767343, f'cp(2439804) = {CP_test(2439804)}, when it should be 838767343'
print('Éxito10!')

# Commit on the Composition Polynomial:

# Función que evalúa el polinomio de composición CP en cada uno de los elementos del dominio de evaluación
def CP_eval(channel):
    CP = get_CP(channel)
    return [CP(d) for d in eval_domain]

channel = Channel() # Se crea un canal de comunicación
CP_merkle = MerkleTree(CP_eval(channel)) # Se crea un árbol Merkle con los valores obtenidos al evaluar el polinomio de composición en cada elemento del dominio de evaluación
channel.send(CP_merkle.root) # Se envía al canal la raíz del árbol Merkle

# Se verifica que la raíz del árbol Merkle sea igual a un valor dado
assert CP_merkle.root == 'a8c87ef9764af3fa005a1a2cf3ec8db50e754ccb655be7597ead15ed4a9110f1', 'Merkle tree root is wrong.'
print('Éxito11!')
print("Excelente!")

# Parte 3:

# Se importan las funciones y clases necesarias
from polynomial import interpolate_poly, Polynomial
from tutorial_sessions import part1, part2

# Se obtienen los valores de la función CP, su evaluación en el dominio y el canal de comunicación creado en la parte 2
cp, cp_eval, cp_merkle, channel, eval_domain = part2()
print("Éxito12")

# FRI Folding:

# Generación del dominio:
print(eval_domain[100] ** 2)
half_domain_size = len(eval_domain) // 2
print(eval_domain[half_domain_size + 100] ** 2)

# Se define la función para obtener el siguiente dominio de evaluación
def next_fri_domain(fri_domain):
    return [x ** 2 for x in fri_domain[:len(fri_domain) // 2]]

# Test against a precomputed hash.
# Se realiza una prueba con un valor predefinido y se verifica que el resultado sea el esperado
from hashlib import sha256
next_domain = next_fri_domain(eval_domain)
assert '5446c90d6ed23ea961513d4ae38fc6585f6614a3d392cb087e837754bfd32797' == sha256(','.join([str(i) for i in next_domain]).encode()).hexdigest()
print('Éxito13!')

# FRI Folding Operator:

# Se define la función para obtener el siguiente polinomio en el proceso de FRI Folding
def next_fri_polynomial(poly,  beta):
    odd_coefficients = poly.poly[1::2]
    even_coefficients = poly.poly[::2]
    odd = beta * Polynomial(odd_coefficients)
    even = Polynomial(even_coefficients)
    return odd + even

# Se realiza una prueba con valores predefinidos y se verifica que el resultado sea el esperado
next_p = next_fri_polynomial(cp, FieldElement(987654321))
assert '6bff4c35e1aa9693f9ceb1599b6a484d7636612be65990e726e52a32452c2154' == sha256(','.join([str(i) for i in next_p.poly]).encode()).hexdigest()
print('Éxito14!')

# Obteniendo la siguiente capa FRI:

# Se define la función para obtener la siguiente capa de FRI a partir de un polinomio, un dominio y un valor beta
def next_fri_layer(poly, domain, beta):
    next_poly = next_fri_polynomial(poly, beta)
    next_domain = next_fri_domain(domain)
    next_layer = [next_poly(x) for x in next_domain]
    return next_poly, next_domain, next_layer

test_poly = Polynomial([FieldElement(2), FieldElement(3), FieldElement(0), FieldElement(1)]) # Creando un polinomio de prueba con coeficientes FieldElement
test_domain = [FieldElement(3), FieldElement(5)] # Definiendo el dominio de evaluación para el polinomio de prueba
beta = FieldElement(7) # Definiendo un valor beta (un elemento aleatorio en el cuerpo finito) para la siguiente capa FRI
next_p, next_d, next_l = next_fri_layer(test_poly, test_domain, beta) # Calculando la siguiente capa FRI del polinomio de prueba

# Comprobando que la siguiente capa FRI se calculó correctamente
assert next_p.poly == [FieldElement(23), FieldElement(7)]
assert next_d == [FieldElement(9)]
assert next_l == [FieldElement(86)]
print('Éxito15!')

# Generando compromisos FRI:

# Esta función toma un polinomio, un dominio de evaluación, los valores de evaluación del polinomio, una prueba de Merkle del polinomio, y un canal de comunicación como entrada. Luego genera y devuelve compromisos FRI para el polinomio utilizando el protocolo FRI.
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

# Creando un canal de comunicación de prueba
test_channel = Channel()

# Generando compromisos FRI para el polinomio de prueba utilizando el canal de prueba
fri_polys, fri_domains, fri_layers, fri_merkles = FriCommit(cp, eval_domain, cp_eval, cp_merkle, test_channel)

# Comprobando que se generaron correctamente los compromisos FRI
assert len(fri_layers) == 11, f'Expected number of FRI layers is 11, whereas it is actually {len(fri_layers)}.'
assert len(fri_layers[-1]) == 8, f'Expected last layer to contain exactly 8 elements, it contains {len(fri_layers[-1])}.'
assert all([x == FieldElement(-1138734538) for x in fri_layers[-1]]), f'Expected last layer to be constant.'
assert fri_polys[-1].degree() == 0, 'Expacted last polynomial to be constant (degree 0).'
assert fri_merkles[-1].root == '1c033312a4df82248bda518b319479c22ea87bd6e15a150db400eeff653ee2ee', 'Last layer Merkle root is wrong.'
assert test_channel.state == '61452c72d8f4279b86fa49e9fb0fdef0246b396a4230a2bfb24e2d5d6bf79c2e', 'The channel state is not as expected.'
print('Éxito16!')

fri_polys, fri_domains, fri_layers, fri_merkles = FriCommit(cp, eval_domain, cp_eval, cp_merkle, channel)
print(channel.proof)

# Part 4: Query Phase

# Importamos la función part3 del archivo tutorial_sessions.
from tutorial_sessions import part3

# Obtenemos los polinomios, dominios, capas y árboles de Merkle generados en la parte 3.
fri_polys, fri_domains, fri_layers, fri_merkles, _ = part3()

print('Éxito17!')

# Decommit on a Query

# Decommit on the FRI Layers

# Función que hace un descompromiso de los datos de una capa FRI en un índice específico.
def decommit_on_fri_layers(idx, channel):
    for layer, merkle in zip(fri_layers[:-1], fri_merkles[:-1]):
        length = len(layer)
        idx = idx % length
        sib_idx = (idx + length // 2) % length        
        channel.send(str(layer[idx]))
        channel.send(str(merkle.get_authentication_path(idx)))
        channel.send(str(layer[sib_idx]))
        channel.send(str(merkle.get_authentication_path(sib_idx)))       
    channel.send(str(fri_layers[-1][0]))
    
# Probamos la función de descompromiso en un hash precalculado.
test_channel = Channel()
for query in [7527, 8168, 1190, 2668, 1262, 1889, 3828, 5798, 396, 2518]:
    decommit_on_fri_layers(query, test_channel)
assert test_channel.state == 'ad4fe9aaee0fbbad0130ae0fda896393b879c5078bf57d6c705ec41ce240861b', 'State of channel is wrong.'
print('Éxito18!')

# Decommit on the Trace Polynomial

# Función que hace un descompromiso de los datos de una consulta específica en el polinomio de traza.
def decommit_on_query(idx, channel): 
    assert idx + 16 < len(f_eval), f'query index: {idx} is out of range. Length of layer: {len(f_eval)}.'
    channel.send(str(f_eval[idx])) # f(x).
    channel.send(str(f_merkle.get_authentication_path(idx))) # auth path for f(x).
    channel.send(str(f_eval[idx + 8])) # f(gx).
    channel.send(str(f_merkle.get_authentication_path(idx + 8))) # auth path for f(gx).
    channel.send(str(f_eval[idx + 16])) # f(g^2x).
    channel.send(str(f_merkle.get_authentication_path(idx + 16))) # auth path for f(g^2x).
    decommit_on_fri_layers(idx, channel)
    
# Probamos la función de descompromiso en un hash precalculado.
test_channel = Channel()
for query in [8134, 1110, 1134, 6106, 7149, 4796, 144, 4738, 957]:
    decommit_on_query(query, test_channel)
assert test_channel.state == '16a72acce8d10ffb318f8f5cd557930e38cdba236a40439c9cf04aaf650cfb96', 'State of channel is wrong.'
print('Éxito19!')

# Descompromiso sobre un conjunto de consultas:

# Función que hace un descompromiso de los datos de un conjunto de consultas en el polinomio de traza.
def decommit_fri(channel):
    for query in range(3):
        # Obtener un índice aleatorio del verificador y enviar el descompromiso correspondiente.
        decommit_on_query(channel.receive_random_int(0, 8191-16), channel)

# Probamos la función de descompromiso en un hash precalculado.        
test_channel = Channel()
decommit_fri(test_channel)
assert test_channel.state == 'eb96b3b77fe6cd48cfb388467c72440bdf035c51d0cfe8b4c003dd1e65e952fd', 'State of channel is wrong.' 
print('Éxito20!')

# ¡Hora de probar!

 # Importa la biblioteca time y tutorial session parte 1 y 3
import time
from tutorial_sessions import part1, part3 

start = time.time() # Inicializa el tiempo de inicio
start_all = start  # Guarda una copia del tiempo de inicio
print("Generación de la traza...")
_, _, _, _, _, _, _, f_eval, f_merkle, _ = part1()
print(f'{time.time() - start}s')
start = time.time()  # Reinicializa el tiempo de inicio
print("Generación del polinomio de composición y de las capas FRI...")
fri_polys, fri_domains, fri_layers, fri_merkles, channel = part3()
print(f'{time.time() - start}s')
start = time.time() # Reinicializa el tiempo de inicio
print("Generación de consultas y descompromisos...")
decommit_fri(channel)
print(f'{time.time() - start}s')
start = time.time()
print(channel.proof)
print(f'Tiempo total: {time.time() - start_all}s')
print(f'Longitud de la prueba sin comprimir en caracteres:{len(str(channel.proof))}')

import sys

dibujo = """\ Ha creado su primera prueba STARKs de Pioneros 101, FELICIDADES
 
                           %%%%%%%%%%%%%%%%%%%%%%%%
                      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/(%%%%%%%%%%%%
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#  %%%%%%%%%%%%%
     %%%%%%%%%%%%%%%#/**,*/(%%%%%%%%%%%%%%%%%%%%%%%%%%(.      ./%%%%%%%%%%
    %%%%%%%%%%,                   ,#%%%%%%%%%%%%%%%%%%%%/    /%%%%%%%%%%%%%%
   %%%%%%%(                            #%%%%%%%%%%%%%%%%%%  %%%%%%%%%%%%%%%%
  %%%%%%*                                 /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%%%                                      *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
  %%%(          ...                             ,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%   /(((((((((((((((.                           #%%%%%%%%%%%%%%%%%%%%%%/%%%
 %%%%%%%#((((((((((((((((((,                            #%%%%%%%%%%%%,     %%%%
 %%%%%%%%%%%%((((((((((((((((/          101 Pioneros                      #%%%%
  %%%%%%%%%%%%%%#(((((((((((((((*                                        /%%%%%
  %%%%%%%%%%%%%%%%%%(((((((((((((((*       Stark Proof - Completada    .(%%%%%
  %%%%%%%%%%%%%%%%%%%%%((((((((((((((((                              .(#%%%%%
   %%%%%%%%%%%%%%%%%%%%%%#(((((((((((((((((,                      .(((%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%((((((((((((((((((((*.         .,((((((%%%%%%%%
     %%%%%%%%%%%*,#%%%%%%%%%%%%#((((((((((((((((((((((((((((((((%%%%%%%%%%
      %%%%%%%%%    %%%%%%%%%%%%%%%%%#(((((((((((((((((((((((%%%%%%%%%%%%
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(((((((##%%%%%%%%%%%%%%%%
          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
             %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
               %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                           %%%%%%%%%%%%%%%%%%%%%%%%%%%%

Ahora comienza el Juego, Bienvenido al ecosistema STARKs...                           
"""

# Imprimir el dibujo de ASCII en la terminal
sys.stdout.write(dibujo)

