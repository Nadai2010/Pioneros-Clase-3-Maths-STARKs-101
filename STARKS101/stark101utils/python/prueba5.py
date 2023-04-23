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
f_merkle = MerkleTree(f_eval)
assert f_merkle.root == '6c266a104eeaceae93c14ad799ce595ec8c2764359d7ad1b4b7c57a4da52be04'
print('Éxito6!')

# Channel:

from channel import Channel
channel = Channel()
channel.send(f_merkle.root)

print(channel.proof)
print("CHECK")

# Second Part:

from polynomial import interpolate_poly, X, prod

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

numer0 = f - 1
denom0 = X - 1

print(numer0)
print(denom0)
print("Genial")

numer0 % denom0

p0 = numer0 / denom0

assert p0(2718) == 2509888982
print('Éxito7!')

# Second Constraint:

numer1 = f - 2338775057
denom1 = X - g**1022
p1 = numer1 / denom1

assert p1(5772) == 232961446
print('Éxito8!')

# Third Constraint:

lst = [(X - g**i) for i in range(1024)]
prod(lst)

# Composing Polynomials:

q = 2*X ** 2 + 1
r = X - 3

print("Excelente!")

cmp = q(r)
cmp

# Back to Polynomial Constraints:

numer2 = f(g**2 * X) - f(g * X)**2 - f**2
print("Numerator at g^1020 is", numer2(g**1020))
print("Numerator at g^1021 is", numer2(g**1021))
denom2 = (X**1024 - 1) / ((X - g**1021) * (X - g**1022) * (X - g**1023))

p2 = numer2 / denom2

assert p2.degree() == 1023, f'The degree of the third constraint is {p2.degree()} when it should be 1023.'
assert p2(31415) == 2090051528
print('Success!')

print('deg p0 =', p0.degree())
print('deg p1 =', p1.degree())
print('deg p2 =', p2.degree())

# Step 4 - Composition Polynomial:

def get_CP(channel):
    alpha0 = channel.receive_random_field_element()
    alpha1 = channel.receive_random_field_element()
    alpha2 = channel.receive_random_field_element()
    return alpha0*p0 + alpha1*p1 + alpha2*p2

test_channel = Channel()
CP_test = get_CP(test_channel)
assert CP_test.degree() == 1023, f'The degree of cp is {CP_test.degree()} when it should be 1023.'
assert CP_test(2439804) == 838767343, f'cp(2439804) = {CP_test(2439804)}, when it should be 838767343'
print('Success!')

# Commit on the Composition Polynomial:

def CP_eval(channel):
    CP = get_CP(channel)
    return [CP(d) for d in eval_domain]

channel = Channel()
CP_merkle = MerkleTree(CP_eval(channel))
channel.send(CP_merkle.root)

assert CP_merkle.root == 'a8c87ef9764af3fa005a1a2cf3ec8db50e754ccb655be7597ead15ed4a9110f1', 'Merkle tree root is wrong.'
print('Success!')
print("Excelente!")

import io
import sys

dibujo = """\
 
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
"""

# Imprimir el dibujo de ASCII en la terminal
sys.stdout.write(dibujo)

