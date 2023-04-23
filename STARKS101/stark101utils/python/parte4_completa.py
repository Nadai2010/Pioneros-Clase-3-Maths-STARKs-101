# Part 4: Query Phase (Fase de Consulta):

from channel import Channel
from tutorial_sessions import part1, part3 

_, _, _, _, _, _, _, f_eval, f_merkle, _ = part1()
fri_polys, fri_domains, fri_layers, fri_merkles, _ = part3()

print('Éxito 1!')

# Decommit en una consulta:

'''
Nuestro objetivo en esta parte es generar toda la información necesaria para verificar los compromisos de las tres partes anteriores.
En esta parte escribimos dos funciones: decommit_on_fri_layers y decommit_on_query.
'''

# Decommit on the FRI Layers:

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

# Prueba usando un hash previamente calculado:
test_channel = Channel()
for query in [7527, 8168, 1190, 2668, 1262, 1889, 3828, 5798, 396, 2518]:
    decommit_on_fri_layers(query, test_channel)
assert test_channel.state == 'ad4fe9aaee0fbbad0130ae0fda896393b879c5078bf57d6c705ec41ce240861b', 'El estado de channel es incorrecto.'
print('Éxito 2!')

# Decommit en el polinomio de traza:

'''
Para probar que efectivamente las capas FRI sobre las que nos descomprometemos se generaron
a partir de la evaluación de la composición polinomial, también debemos enviar:
El valor de f(x) y su ruta de autenticación.
El valor de f(gx) y su ruta de autenticación.
El valor de f(g^2x) y su ruta de autenticación.
Por lo tanto, la función decommit_on_query debería enviar lo anterior a través del canal y, a continuación,
llamar a decommit_on_fri_layers.
'''
def decommit_on_query(idx, channel): 
    assert idx + 16 < len(f_eval), f'query index: {idx} is out of range. Length of layer: {len(f_eval)}.'
    channel.send(str(f_eval[idx])) # f(x).
    channel.send(str(f_merkle.get_authentication_path(idx))) # ruta de autenticación para f(x).
    channel.send(str(f_eval[idx + 8])) # f(gx).
    channel.send(str(f_merkle.get_authentication_path(idx + 8))) # ruta de autenticación para f(gx).
    channel.send(str(f_eval[idx + 16])) # f(g^2x).
    channel.send(str(f_merkle.get_authentication_path(idx + 16))) # ruta de autenticación para f(g^2x).
    decommit_on_fri_layers(idx, channel)
    
# Prueba usando un hash previamente calculado:
test_channel = Channel()
for query in [8134, 1110, 1134, 6106, 7149, 4796, 144, 4738, 957]:
    decommit_on_query(query, test_channel)
assert test_channel.state == '16a72acce8d10ffb318f8f5cd557930e38cdba236a40439c9cf04aaf650cfb96', 'El estado de channel es incorrecto.'
print('Éxito 3!')

# Decommit en un conjunto de consultas:

'''
Para terminar la prueba, el probador obtiene un conjunto de consultas aleatorias del channel, y realiza el decommit en cada consulta.
Usa la función decommit_on_query() y Channel.receive_random_int para generar 3 consultas aleatorias y hacer el decommit en cada una.
'''
def decommit_fri(channel):
    for query in range(3):
        # Obtener un índice aleatorio del verificador y enviar el decommitment correspondiente.
        decommit_on_query(channel.receive_random_int(0, 8191-16), channel)
        
test_channel = Channel()
decommit_fri(test_channel)
assert test_channel.state == 'eb96b3b77fe6cd48cfb388467c72440bdf035c51d0cfe8b4c003dd1e65e952fd', 'El estado de channel es incorrecto.' 
print('Éxito 4!')

# Llegó la hora!

'''
Uniendo lo anterior y ejecutando todo el código, imprimimos la prueba:
'''
import time
from tutorial_sessions import part1, part3 

start = time.time()
start_all = start
print("Generando la traza...")
_, _, _, _, _, _, _, f_eval, f_merkle, _ = part1()
print(f'{time.time() - start}s')
start = time.time()
print("Generando la composición polinomial y las capas FRI...")
fri_polys, fri_domains, fri_layers, fri_merkles, channel = part3()
print(f'{time.time() - start}s')
start = time.time()
print("Generación de consultas y decommitments...")
decommit_fri(channel)
print(f'{time.time() - start}s')
start = time.time()
print(channel.proof)
print(f'Overall time: {time.time() - start_all}s')
print(f'Uncompressed proof length in characters: {len(str(channel.proof))}')

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