# Parte 1: La Traza y la Extensión de Bajo Grado (Low-Degree Extension)

'''
Tomamos dos números, el 1 y X, y elaboraremos una secuencia de los Cuadrados de Fibonacci sobre un finite field, donde el 1023avo número de dicha sucesión es 2338775057.
Al finalizar, este código producirá una prueba de que conocemos el valor de X.
'''

# La Base:

# Clase FieldElement:

'''
Utilizamos nuestra clase FieldElement para representar elementos del Field.
Todas las operaciones se realizan en módulo 3221225473 ((2**30) * 3 + 1).
'''

from field import FieldElement

# Traza de la secuencia de los Cuadrados de Fibonacci:

'''
Para empezar, construiremos una lista a de longitud 1023, donde los dos primeros elementos serán objetos FieldElement que representan al 1 y 3141592, respectivamente.
Los siguientes 1021 elementos se irán generando siguiendo la expresión matemática de los Cuadrados de Fibonacci.
Los dos valores descritos anteriormente inician la secuencia.
'''

a = [FieldElement(1), FieldElement(3141592)] # Acá están reflejados los dos primeros valores de la lista.
while len(a) < 1023:
    a.append(a[-2] * a[-2] + a[-1] * a[-1]) # Con esto se va calculando el siguiente elemento de la lista.
    
assert len(a) == 1023, 'La traza debe constar exactamente de 1023 elementos.'
assert a[0] == FieldElement(1), 'El primer elemento de la traza debe ser el 1.'
for i in range(2, 1023):
    assert a[i] == a[i - 1] * a[i - 1] + a[i - 2] * a[i - 2], f'La regla de recursión de los cuadrados de Fibonacci no se aplica al índice {i}'
assert a[1022] == FieldElement(2338775057), 'El último elemento es incorrecto!'
print('Éxito 1!')

# Pensando en polinomios:

'''
Ahora pensemos en la secuencia como la evaluación de un polinomio, todavía desconocido, de grado 1022.
Elegiremos como dominio algún subgrupo G contenido dentro de Fx, de tamaño 1024, por razones que quedarán claras más adelante.
En este caso, Fx es el grupo multiplicativo de F, que obtenemos a partir de F omitiendo al cero.
'''

# Encontrando un grupo de tamaño 1024:

'''
Si encontramos un elemento g perteneciente a F, cuyo orden (multiplicativo) es 1024, entonces g generará tal grupo.
'''

g = FieldElement.generator() ** (3 * 2 ** 20) # Generador.
G = [g ** i for i in range(1024)] # Dominio.

assert g.is_order(1024), 'El generador g es de orden incorrecto.'
b = FieldElement(1)
for i in range(1023):
    assert b == G[i], 'El lugar i-ésimo de G no es igual a la potencia i-ésima de g.'
    b = b * g
    assert b != FieldElement(1), f'g es de orden {i + 1}'
    
if b * g == FieldElement(1): 
# Imprimir un mensaje de éxito si todas las pruebas pasan
    print('Éxito 2!')
else:
    print('g es de orden > 1024')
    
# Clase Polynomial:

'''
Le proporcionamos una clase llamada Polynomial. Con ella es sencillo construir un Polinomio simplemente usando la variable X.
'''
    
from polynomial import X

# A continuación un ejemplo usando el polinomio 2x^2 + 1:

p = 2*X**2 + 1

print(p(2)) # Evaluando p en 2.

# Interpolando un Polinomio:

'''
Nuestro módulo polynomial proporciona una función de interpolación de Lagrange.
Supongamos que a contiene los valores de algún polinomio sobre G (excepto G[-1], ya que a es un elemento más corto).
Utilice interpolate_poly() para obtener f y obtener su valor en FieldElement(2).
'''

from polynomial import interpolate_poly

# Interpolando el polinomio usando la lista G (sin su último elemento) y el valor a:

f = interpolate_poly(G[:-1], a)
v = f(2)

assert v == FieldElement(1302089273)
# Imprimiendo un mensaje de éxito si pasa la prueba:
print('Éxito 3!')

# Evaluando en un dominio más grande:

'''
La traza, vista como evaluaciones de un polinomio f en G, puede ampliarse evaluando f en un dominio mayor.
Creando así un código de corrección de errores Reed-Solomon.
Trabajaremos con un dominio que sea 8 veces mayor que G.
'''

# Cosets:

# Generador de Fx:
w = FieldElement.generator()

# Generador de H:
h = w ** ((2 ** 30 * 3) // 8192)

# Creando una lista de 8192 elementos elevando h a diversas potencias (desde 0 hasta 8191):
H = [h ** i for i in range(8192)]

# Creando una lista de 8192 elementos multiplicando cada elemento de H por el generador w:
eval_domain = [w * x for x in H]

# Prueba de funcionamiento:

from hashlib import sha256

# Verificando que no hayan elementos duplicados en eval_domain:
assert len(set(eval_domain)) == len(eval_domain)

w = FieldElement.generator()
w_inv = w.inverse()

# Verificando que el segundo elemento de la lista H sea el generador h:
assert '55fe9505f35b6d77660537f6541d441ec1bd919d03901210384c6aa1da2682ce' == sha256(str(H[1]).encode()).hexdigest(),\
    'H la lista es incorrecta. H[1] debe ser h (el generador de H).'

for i in range(8192):
    assert ((w_inv * eval_domain[1]) ** i) * w == eval_domain[i]

# Imprimir un mensaje de éxito si todas las pruebas pasan:
print('Éxito 4!')

# Evaluar en un Coset:

f = interpolate_poly(G[:-1], a)
f_eval = [f(d) for d in eval_domain]

# Prueba usando un hash previamente calculado:

from hashlib import sha256
from channel import serialize
assert '1d357f674c27194715d1440f6a166e30855550cb8cb8efeb72827f6a1bf9b5bb' == sha256(serialize(f_eval).encode()).hexdigest()
print('Éxito 5!')

# Commitments:

'''
Utilizaremos árboles de Merkle basados en Sha256 como esquema de compromiso:
'''

from merkle import MerkleTree
f_merkle = MerkleTree(f_eval)
assert f_merkle.root == '6c266a104eeaceae93c14ad799ce595ec8c2764359d7ad1b4b7c57a4da52be04'
print('Éxito 6!')

# Channel:

'''
Teóricamente, un sistema de prueba STARK es un protocolo de interacción entre dos partes: un probador y un verificador.
En la práctica, convertimos este protocolo interactivo en una prueba no interactiva utilizando la Heurística Fiat-Shamir.
En este tutorial se utilizará la clase Channel, que implementa esta transformación.
Este channel reemplaza al verificador en el sentido de que el probador enviará datos, y recibirá números aleatorios o instancias aleatorias de FieldElement.
Este simple trozo de código instanciará un channel object y enviará la raíz de su Árbol de Merkle.
Luego, el channel object puede ser llamado para proporcionar números aleatorios o elementos aleatorios del field.
'''

from channel import Channel
channel = Channel()
channel.send(f_merkle.root)
print(channel.proof)
print("Parte 1 Completada!")
