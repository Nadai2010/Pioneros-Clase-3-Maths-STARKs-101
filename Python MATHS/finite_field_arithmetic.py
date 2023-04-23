####################
# Máximo común divisor:
# ax + by = 1
####################

def xgcd(x, y):
    old_r, r = (x, y)
    old_s, s = (1, 0)
    old_t, t = (0, 1)
    count = 0
    while r != 0:
        print("\tEncontrando el xgcd({}): {} {} {}".format(count, old_r, old_t, old_s), end="\r")
        count += 1
        quotient = old_r // r
        old_r, r = (r, old_r - quotient * r)
        old_s, s = (s, old_s - quotient * s)
        old_t, t = (t, old_t - quotient * t)

    print()
    return old_s, old_t, old_r  # a, b, g

primo = 13

print("Operadores matemáticos en campo finito:")
####################
# Adición en campo finito
####################
izquierda = 4
derecha = 12
print("\tSuma: ({} + {}) % {} = {}\n".format(izquierda, derecha, primo, (izquierda + derecha) % primo))

####################
# Sustracción en campo finito
####################
izquierda = 35
derecha = 5
print("\tResta: ({} - {}) % {} = {}\n".format(izquierda, derecha, primo, (izquierda + derecha * -1) % primo))

####################
# Multiplicación en campo finito
####################
izquierda = 90
derecha = 10
print("\tMultiplicación: ({} * {}) % {} = {}\n".format(izquierda, derecha, primo, (izquierda * derecha) % primo))

####################
# División en campo finito
####################
dividendo = 2
divisor = 3
print("\tDivisión: ({} / {})".format(dividendo, divisor))
a, b, g = xgcd(divisor, primo)
print("\tse encontró: {}*{} + {}*{}=1".format(a, divisor, b, primo))
print("\t({} / {}) % {} = {}\n".format(dividendo, divisor, primo, (dividendo * a) % primo))
