<div align="center">
  <img src="https://github.com/Nadai2010/Pioneros-Maths-STARKs/blob/master/Pioneros%20Maths%20Starks/basecamp.png" style="width: 300px">
  <h1 style="font-size: larger;">
    <img src="https://github.com/Nadai2010/Nadai-SHARP-Starknet/blob/master/im%C3%A1genes/Starknet.png" width="40">
    <strong>Starknet Pioneros - Maths STARKs 101</strong> 
    <img src="https://github.com/Nadai2010/Nadai-SHARP-Starknet/blob/master/im%C3%A1genes/Starknet.png" width="40">
  </h1>
</div>

<div align="center">
     
|Presentación|Video|Prueba lo que has aprendido
|:----:|:----:|:----:|
|[Septiembre 2022](https://drive.google.com/file/d/1asONnOcSnRJwMXF-Zx1uJBdpbMrLYnmE/view?usp=sharing), [Febrero 2023](https://drive.google.com/file/d/1AWeCNRLgoiXVvLS31HxqslxUGIFMnwRf/view)|[Camp 1 (Septiembre 2022)](https://www.youtube.com/watch?v=7p60e7RzuMs), [Camp 2 (Febrero 2023)](https://m.youtube.com/live/n9vG4G_JqLE) |Pásate al hardcore con StarkWare [STARK 101](https://starkware.co/stark-101)|

Puede encontrar Traducciones de documentos oficiales de MATHS Starkware [aquí](https://github.com/Starknet-Es/Maths-StarknetEs/blob/main/Gu%C3%ADas%20Oficiales/Readme.md)
</div>
<p align="center">
    <a href="https://starkware.co/">
        <img src="https://img.shields.io/badge/powered_by-StarkWare-navy">
    </a>
</p>

---

### Temas

<ol>
    <li><a href="#Introducción a STARKs y Validity Proofs">Introducción a STARKs y Validity Proofs</a></li>
    <li><a href="#Campos">Campos</a></li>
    <li><a href="#Aritmética Modular">Aritmética Modular</a></li>
    <li><a href="#STARKS - Parte 1">STARKS - Parte 1</a></li>
    <li><a href="#STARKS - Parte 2">STARKS - Parte 2</a></li>
    <li><a href="#STARKS - Parte 3">STARKS - Parte 3</a></li>
    <li><a href="#STARKS - Parte 4">STARKS - Parte 4</a></li>
</ol>

---

<div align="center">
    <h2 id="Introducción a STARKs y Validity Proofs">Introducción a STARKs y Validity Proofs</h2>
    <p> </p>
    <img src="">
</div>



---

<div align="center">
    <h2 id="Campos">Campos</h2>
</div>

Gran parte de la criptografía práctica actual se basa en `campos finitos`. Un campo finito es un campo que contiene un número finito de elementos y define operaciones aritméticas de multiplicación, suma, resta y división. 

Un campo finito no puede contener subcampos y, por tanto, suele aplicar los principios de la aritmética modular sobre un número primo grande e irreducible. El número de elementos del campo también se conoce como `orden`.

Un campo es un conjunto de números enteros junto con dos operaciones llamadas suma y multiplicación.

Un ejemplo de campo son los números reales sometidos a adición y multiplicación, otro es un conjunto de números enteros mod un número primo con adición y multiplicación. 

Se requiere que las operaciones de campo satisfagan los siguientes axiomas de campo. En estos axiomas, a, b y c son elementos arbitrarios del campo `𝔽`.

1. Asociatividad de la suma y la multiplicación: `a + (b + c) = (a + b) + c` y `a • (b • c) = (a • b) • c`.
2. Conmutatividad de la suma y la multiplicación: `a + b = b + a` y `a • b = b • a`
3. Identidad aditiva y multiplicativa: existen dos elementos diferentes 0 y 1 en `𝔽` tales que `a + 0 = a` y `a • 1 = a`.
4. Inversos aditivos: para cada a en F, existe un elemento en F, denotado -a, llamado inverso aditivo de a, tal que `a + (-a) = 0`.
5. Inversos multiplicativos: para cada a ≠ 0 en F, existe un elemento en F, denotado por α⁻¹, llamado inverso multiplicativo de a, tal que `a•α⁻¹ = 1`.
6. Distributividad de la multiplicación sobre la suma: `a•(b + c) = (a•b) + (a•c)`.

## Ejemplo Práctico
Si quiere hacer una prueba en su lenguaje con más conocimientos como Python o Rust, primero clone este repositorio.

Primero clone este repositorio para tener todo los codigos ejecutando:

```bash
gh repo clone Nadai2010/Pioneros-Maths-STARKs-101
```

Luego en caso de Rust, abra el archivo `Cargo.toml` y verifica que todas las dependencias, rutas y nombres estén listadas correctamente. En este ejemplo de `Cargo.toml`

```bash
[[bin]]
name = "finite_field_arithmetic"
path = "src/finite_field_arithmetic.rs"
```

Ejecuta el comando `cargo build` para compilar el proyecto. Este comando creará un archivo ejecutable en la carpeta `target/debug` llamado `finite_field_arithmetic`.

```bash
cargo build
```

Navega hasta la carpeta `target/debug` en la terminal y ejecuta el archivo ejecutable con el comando `./finite_field_arithmetic`

```bash
./finite_field_arithmetic
```

![Graph](/Im%C3%A1genes/fieldrs.png)


Ejemplo Python

```bash
python3 finite_field_arithmetic.py
```

![Graph](/Im%C3%A1genes/fieldpy.png)

---

<div align="center">
    <h2 id="aritmética_modular">Aritmética Modular</h2>
</div>

[Véase esta introducción](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)

Sistema aritmético para números enteros en el que los números se "enrollan" al alcanzar un determinado valor (también conocido como "módulo").

<div align="center">
<img src="https://github.com/Starknet-Es/Maths-StarknetEs/blob/main/im%C3%A1genes/AritemticaModular.png" width="1000">
</div>

Cuando escribimos n mod k nos referimos simplemente al residuo cuando n se divide por k. Así:

```bash
9 mod 7 = 2
2 mod 7 = 2
```
El resto debe ser positivo.

Un ejemplo real de aritmética modular es la medición del tiempo mediante un reloj. Cuando la hora del día sobrepasa el módulo (12) nos "envolvemos" y empezamos en cero.

## Ejemplo Práctico
Si quiere hacer una prueba en su lenguaje con más conocimientos como Python o Rust, primero clone este repositorio.

Primero clone este repositorio para tener todo los codigos ejecutando:

```bash
gh repo clone Nadai2010/Pioneros-Maths-STARKs-101
```

Luego en caso de Rust, abra el archivo `Cargo.toml` y verifica que todas las dependencias, rutas y nombres estén listadas correctamente. En este ejemplo de `Cargo.toml`

```bash
[[bin]]
name = "arithmetic_modular"
path = "src/arithmetic_modular.rs"
```

Ejecuta el comando `cargo build` para compilar el proyecto. Este comando creará un archivo ejecutable en la carpeta target/debug llamado finite_field_arithmetic.

```bash
cargo build
```

Navega hasta la carpeta `target/debug` en la terminal y ejecuta el archivo ejecutable con el comando `./arithmetic_modular`

```bash
./arithmetic_modular
```

Ejemplo Python:

```bash
python3 arithmetic_modular.py
```

## Operaciones en Aritmética Modular Base para RUST

Suponiendo que tiene conocimietnos previos sobre Rust y que ha revisado los conceptos de Aritmetica modular, nos centraremos en ejecutar varios contratos y ver los resultados. 

- [Aritmetica_Modular_Base.rs](/Pioneros-Maths-STARKs-101/Rust%20MATHS/Aritmetica_Modular_Base.rs)- Código Base para las diferentes ecuaciones suma, resta, multiplicación y división en aritmética modular.


Primero clone este repositorio para tener todo los codigos ejecutando:

```bash
gh repo clone Nadai2010/Pioneros-Maths-STARKs-101
```

### Operaciones en Aritmética Modular Base

Para ejecutar los comandos dentro de la carpeta donde se encuentra nuestros archivo Rust y ejecute

```rust
rustc Aritmetica_Modular_Base.rs
```

Se generará un archivo el cual puede luego ejecutar corriendo en su terminal:

```rust
./Aritmetica_Modular_Base
```

![Graph](/Im%C3%A1genes/modbasers.png)

### Suma modular de 15 y 7 modulo 10
```rust
let result = mod_add(15, 7, 10);
    println!("{}", result); 
```
En este ejemplo, 15 + 7 = 22. El resto de la división de 22 entre 10 es 2, por lo que el resultado de la suma modular de 15 y 7 módulo 10 es 2.

### Resta modular de 15 y 7 modulo 10
```rust
let result = mod_subtract(15, 7, 10);
    println!("{}", result);
```

La resta de 15 y 7 es 8. Sin embargo, como estamos trabajando en el módulo 10, necesitamos asegurarnos de que el resultado esté dentro del rango de valores permitidos (en este caso, de 0 a 9). El resto de la división de 8 entre 10 es 8, lo que significa que el resultado de la resta modular de 15 y 7 módulo 10 es 8.

### Producto modular de 15 y 7 modulo 10
```rust
let result = mod_multiply(15, 7, 10);
    println!("{}", result); 
```

En este caso, el producto de 15 y 7 es 105. Sin embargo, como estamos trabajando en el módulo 10, necesitamos asegurarnos de que el resultado esté dentro del rango de valores permitidos (en este caso, de 0 a 9). El resto de la división de 105 entre 10 es 5, lo que significa que el resultado del producto modular de 15 y 7 módulo 10 es 5.

### División modular de 15 y 7 modulo 10
```rust
let result = mod_divide(15, 7, 10);
    println!("{}", result);
```

La operación de división no es una operación modular en sí misma, por lo que en este caso estamos usando una técnica conocida como inverso multiplicativo para encontrar el resultado de la división modular.

El inverso multiplicativo de un número `a` en módulo `m` es un número `b` tal que `ab` es `congruente con 1 módulo m` (es decir, el resto de la división de ab entre m es 1). En otras palabras, `b` es el número que, al multiplicarse por `a`, nos da un `resultado congruente con 1 módulo m`.

En este ejemplo, estamos buscando el inverso multiplicativo de 7 en módulo 10. El inverso multiplicativo de 7 en módulo 10 es 3, porque 7*3 es congruente con 1 módulo 10 (21 es divisible entre 10, por lo que el residuo de la división es 1).

Por lo tanto, la división de 15 entre 7 en módulo 10 es equivalente a la multiplicación de 15 por el inverso multiplicativo de 7 en módulo 10, es decir, 15 * 3. El resultado de 15 * 3 módulo 10 es 5, por lo que el resultado de la división modular de 15 y 7 módulo 10 es 5

---

## Guia de Aritmética Modular Base para Python

Suponiendo que tiene conocimietnos previos sobre Python y que ha revisado los concpetos de Aritmetica modular, nos centraremos en ejecutar varios contratos y ver los resultados. 

- [Aritmetica_Modular_Base.py](/Pioneros-Maths-STARKs-101/Python%20MATHS/Aritmetica_Modular_Base.py)- Código Base para las diferentes ecuaciones suma, resta, multiplicación y división en aritmética modular.

Primero clone este repositorio para tener todo los codigos ejecutadndo
```bash
gh repo clone Nadai2010/Pioneros-Maths-STARKs-101
```

### Operaciones en Aritmética Modular Base
Para ejecutar los comandos dentro de la carpeta donde se encuentra nuestros archivo Python ejecute

```python
python3.9 Aritmetica_Modular_Base.py
```

![Graph](/Im%C3%A1genes/modbasepy.png)

### Suma modular de 15 y 7 modulo 10
```python
result = mod_add(15, 7, 10)
print(result)
```
En este ejemplo, 15 + 7 = 22. El residuo de la división de 22 entre 10 es 2, por lo que el resultado de la suma modular de 15 y 7 módulo 10 es 2.

### Resta modular de 15 y 7 modulo 10
```python
result = mod_subtract(15, 7, 10)
print(result) 
```

La resta de 15 y 7 es 8. Sin embargo, como estamos trabajando en el módulo 10, necesitamos asegurarnos de que el resultado esté dentro del rango de valores permitidos (en este caso, de 0 a 9). El residuo de la división de 8 entre 10 es 8, lo que significa que el resultado de la resta modular de 15 y 7 módulo 10 es 8.

### Producto modular de 15 y 7 modulo 10
```python
result = mod_multiply(15, 7, 10)
print(result)
```

En este caso, el producto de 15 y 7 es 105. Sin embargo, como estamos trabajando en el módulo 10, necesitamos asegurarnos de que el resultado esté dentro del rango de valores permitidos (en este caso, de 0 a 9). El residuo de la división de 105 entre 10 es 5, lo que significa que el resultado del producto modular de 15 y 7 módulo 10 es 5.

### División modular de 15 y 7 modulo 10
```python
result = mod_divide(15, 7, 10)
print(result)
```

La operación de división no es una operación modular en sí misma, por lo que en este caso estamos usando una técnica conocida como inverso multiplicativo para encontrar el resultado de la división modular.

---

<div align="center">
    <h2 id="STARKS - Parte 1">STARKS - Parte 1</h2>
</div>
El inverso multiplicativo de un número `a` en módulo `m` es un número `b` tal que `ab` es `congruente con 1 módulo m` (es decir, el residuo de la división de ab entre m es 1). En otras palabras, `b` es el número que, al multiplicarse por `a`, nos da un `resultado congruente con 1 módulo m`.

En este ejemplo, estamos buscando el inverso multiplicativo de 7 en módulo 10. El inverso multiplicativo de 7 en módulo 10 es 3, porque 7*3 es congruente con 1 módulo 10 (21 es divisible entre 10, por lo que el residuo de la división es 1).

Por lo tanto, la división de 15 entre 7 en módulo 10 es equivalente a la multiplicación de 15 por el inverso multiplicativo de 7 en módulo 10, es decir, 15 * 3. El resultado de 15 * 3 módulo 10 es 5, por lo que el resultado de la división modular de 15 y 7 módulo 10 es 5

