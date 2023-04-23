# Parte 2 (Restricciones):

from channel import Channel
from field import FieldElement
from merkle import MerkleTree
from polynomial import interpolate_poly, X, prod
from tutorial_sessions import part1

a, g, G, h, H, eval_domain, f, f_eval, f_merkle, channel = part1()
print('Éxito 1!')

# Primera restricción:

numer0 = f - 1
denom0 = X - 1

# El hecho de que f(x) - 1 tenga una raíz en 1 implica que es divisible entre (x - 1):
comprobar_div = numer0 % denom0
print(comprobar_div)

# Construcción de p0. El polinomio que representa la primera restricción:
p0 = numer0 / denom0

assert p0(2718) == 2509888982
print('Éxito 2!')

# Segunda restricción:

numer1 = f - 2338775057
denom1 = X - g**1022

# Construcción de p1. El polinomio que representa la segunda restricción:
p1 = numer1 / denom1

assert p1(5772) == 232961446
print('Éxito 3!')

# Tercera restricción:

'''
La función racional de la última restricción es algo más complicada.
Sin embargo, su denominador puede reescribirse, de modo que toda la expresión sea más fácil de calcular:
'''
lst = [(X - g**i) for i in range(1024)]
print(prod(lst))

# Composición de polinomios:

# Creando dos polinomios:
q = 2*X ** 2 + 1
r = X - 3

# Al componer q sobre r se obtiene un nuevo polinomio:
cmp = q(r)
print(cmp)

# Volviendo a las restricciones polinómicas:

numer2 = f(g**2 * X) - f(g * X)**2 - f**2
print("Numerator at g^1020 is", numer2(g**1020))
print("Numerator at g^1021 is", numer2(g**1021))
denom2 = (X**1024 - 1) / ((X - g**1021) * (X - g**1022) * (X - g**1023))

# Construcción de p2. El polinomio que representa la tercera restricción:
p2 = numer2 / denom2

assert p2.degree() == 1023, f'El grado de la tercera restricción es {p2.degree()} cuando debería ser 1023.'
assert p2(31415) == 2090051528
print('Éxito 4!')

'''
Observe que los grados de las restricciones polinómicas son todos menores a 1024.
Esto será importante en la siguiente parte:
'''
print('deg p0 =', p0.degree())
print('deg p1 =', p1.degree())
print('deg p2 =', p2.degree())

# Paso 4 - Composición Polinómica:

'''
Tomamos una combinación lineal aleatoria de p0, p1 y p2, denominada composición polinomial (abreviado CP).
alpha0, alpha1 y alpha2 son elementos del field aleatorios obtenidos del verificador, o en nuestro caso, de channel.
Probar que la CP es un polinomio garantiza, con alta probabilidad, que p0, p1, p2 son, a su vez, polinomios.
Vamos a crear CP usando Channel.receive_random_field_element para obtener cada alpha:
'''
def get_CP(channel):
    alpha0 = channel.receive_random_field_element()
    alpha1 = channel.receive_random_field_element()
    alpha2 = channel.receive_random_field_element()
    return alpha0*p0 + alpha1*p1 + alpha2*p2

# Prueba de funcionamiento:
test_channel = Channel()
CP_test = get_CP(test_channel)
assert CP_test.degree() == 1023, f'El grado de la cp es {CP_test.degree()} cuando debería ser 1023.'
assert CP_test(2439804) == 838767343, f'cp(2439804) = {CP_test(2439804)}, cuando debería ser 838767343'
print('Éxito 5!')

# Compromiso sobre la Composición Polinomial:

# Por último, evaluamos cp sobre el dominio de evaluación (eval_domain):
def CP_eval(channel):
    CP = get_CP(channel)
    return [CP(d) for d in eval_domain]

# Construcción de un árbol de Merkle y enviamos su raíz:

channel = Channel()
CP_merkle = MerkleTree(CP_eval(channel))
channel.send(CP_merkle.root)

assert CP_merkle.root == 'a8c87ef9764af3fa005a1a2cf3ec8db50e754ccb655be7597ead15ed4a9110f1', 'La raíz del árbol de Merkle está mal.'
print('Éxito 6!')
print('Parte 2 Completada!')