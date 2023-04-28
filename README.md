<div align="center">
  <img src="https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/Im%C3%A1genes/Pioneros.png" style="width: 200px">
  <h1 style="font-size: larger;">
    <img src="https://github.com/Nadai2010/Nadai-SHARP-Starknet/blob/master/im%C3%A1genes/Starknet.png" width="40">
    <strong>Starknet Pioneros - Maths STARKs 101</strong> 
    <img src="https://github.com/Nadai2010/Nadai-SHARP-Starknet/blob/master/im%C3%A1genes/Starknet.png" width="40">
  </h1>
</div>

<div align="center">
     
|Presentación|Video|Prueba lo que has aprendido
|:----:|:----:|:----:|
|[Septiembre 2022](https://drive.google.com/file/d/1asONnOcSnRJwMXF-Zx1uJBdpbMrLYnmE/view?usp=sharing), [Febrero 2023](https://drive.google.com/file/d/1AWeCNRLgoiXVvLS31HxqslxUGIFMnwRf/view), [Mayo 2023](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/PDF/Pioneros%20Maths.pdf)|[Camp 1 (Septiembre 2022)](https://www.youtube.com/watch?v=7p60e7RzuMs), [Camp 2 (Febrero 2023)](https://m.youtube.com/live/n9vG4G_JqLE), [Pioneros 1 (Mayo 2023)]() |Pásate al hardcore con StarkWare [STARK 101](https://starkware.co/stark-101), [Pioneros STARK 101](https://github.com/Nadai2010/Pioneros-Clase-3-Maths-STARKs-101/tree/master/STARKS101/STARK101_res)|

Puede encontrar Traducciones de los Artículos oficiales de MATHS Starkware [aquí](https://github.com/Starknet-Es/Maths-StarknetEs/blob/main/Gu%C3%ADas%20Oficiales/Readme.md)

Puede encontrar las Diapositvas de la Presentación [aquí](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/PDF/Pioneros%20Maths.pdf)
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
    <img src="https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/Im%C3%A1genes/Verificación.png"  width="600">
</div>

---

La Integridad Computacional (CI) es una propiedad fundamental para el comercio, que se refiere a la confianza en que la salida de un cálculo es correcta. Es lo que nos permite confiar en el balance de una cuenta o en el monto de una factura en una tienda. Pero, ¿cómo podemos garantizar esta integridad en un entorno digital donde no siempre podemos confiar en todas las partes involucradas?

Aquí es donde entra en juego la tecnología STARK, que se basa en las pruebas de integridad y garantiza que la computación se realice de manera correcta, incluso si nadie está mirando. STARKs utiliza las matemáticas para lograr este objetivo y está diseñado para monitorear y garantizar la integridad de un gran cálculo realizado por un grupo de supercomputadoras poco confiables.

Las Validity Proofs o Pruebas de Validez son una herramienta crucial para garantizar la integridad y validez de los cambios realizados fuera de la cadena principal. Los sistemas de pruebas Zero Knowledge, en los que hay información secreta conocida por el prover que no es conocida por el verifier, son clave para las Validity Proofs. En el caso de Starknet, se trata de un Validity Rollup que utiliza STARKs.


<div align="center">
    <img src="https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/Im%C3%A1genes/Validity.png"  width="400">
</div>

---

Es importante tener en cuenta que ZK es una propiedad adicional que se utiliza para afirmar al probador que no tiene que revelar ninguna información incluida en el cálculo. En el caso de Starknet como L2 pública, los datos de transacción son públicos, por lo que no se ofrece privacidad como tal. En Starknet, siempre nos referimos a Validity Rollup como la forma en que probamos la validez del cálculo computacional.

<div align="center">
    <img src="https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/Im%C3%A1genes/STARK.png"  width="600">
</div>


STARKs, por su parte, son un tipo de Pruebas Escalables y Transparentes de Argumentos de Conocimiento. 

* **S = Escalable.** Su principal ventaja es que trasladar un cálculo fuera de la cadena reduce exponencialmente los costes de verificación de la cadena de bloques, mientras que el proceso de creación de una prueba fuera de la cadena cuesta aproximadamente lo mismo que pedir a un único nodo de la cadena de bloques que ejecute el cálculo. 
* **T = Transparente.** La seguridad de las STARK no depende de ceremonias de configuración elaboradas que puedan generar `residuos tóxicos` criptográficos, como sucede en otras tecnologías de pruebas.
* **ARK = Argumento de Conocimiento.** Las pruebas son realizadas por un prover fuera de la cadena que realmente ejecutó el cálculo junto con las entradas auxiliares necesarias. Esto significa que la prueba es matemáticamente comprobable de manera sólida, lo que la hace auténtica y verificable por cualquier computadora.

* Si quieres profundizar en este tema, te recomendamos consultar el libro [Starknet Book](https://book.starknet.io/chapter_10/index.html)
* Si quieres revisar la presentación la encontrá [aquí](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/PDF/Pioneros%20Maths.pdf)

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

Ejecuta el comando `cargo build` para compilar el proyecto. Este comando creará un archivo ejecutable en la carpeta target/debug llamado arithmetic_modular.

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

Ambos casos deberán ejecutar un reloj en los que vayan pasando las horas y enrollándose en módulos.

![Graph](/Im%C3%A1genes/reloj.png)

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

## Ejemplo Práctico Finite Field Arithmetic
Si quiere ver más ejemplos de campos finitos en aritmética modular de una forma mas resumida y detallada revise las siguientes imágenes en su lenguaje con más conocimientos como Python o Rust, primero clone este repositorio.

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
    <h2 id="STARKS - Parte 1">STARKS - Parte 1</h2>
</div>

Este material tiene el propósito de describir el funcionamiento del protocolo STARK (**S**calable **T**ransparent **AR**gument of **K**nowledge).

Se expresa una declaración vinculada a la secuencia de los Cuadrados de Fibonacci y se presenta todo el desarrollo matemático que busca convencer al verificador de que dicha declaración es correcta.

El contenido se divide en 4 apartados. Para cada uno de ellos se proporciona un Jupyter Notebook con la explicación y código correspondiente para efectuar el procedimiento.

A continuación se ofrece una breve descripción, a modo de resumen, de cada apartado:

En esta sección se presentará la declaración que se va a probar usando el protocolo STARK y se describen los dos primeros pasos del protocolo: La Extensión de bajo grado o Low Degree Extension (LDE) y la fase de compromiso (the commitment phase).

[Notebook Parte 1](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/STARKS101/STARK101_res/STARK101_Parte1_resuelta.ipynb)

[El código Parte 1](https://github.com/Nadai2010/Pioneros-Clase-3-Maths-STARKs-101/blob/master/STARKS101/STARK101_click/STARK101_Parte1_click.py) Deberá encontrarse dentro de la carpeta del Archivo `STARK101_Parte1_click.py` para revisarlo y ejecutarlo, en este caso use en su terminal el siguiente comando:

```bash
python3.9 STARK101_Parte1_click.py
```

Deberá imprimirle la Parte 1 completa.

![Graph](/Im%C3%A1genes/Parte1.png)


<div align="center">
    <h2 id="STARKS - Parte 2">STARKS - Parte 2</h2>
</div>

En este apartado se crearán las restricciones polinómicas empleando elementos calculados en la primera parte: La traza, el generador «g» y el polinomio de traza. Al finalizar, crearemos lo que denominamos «polinomio de composición» (composition polynomial en inglés, o CP si lo abreviamos) usando tres funciones racionales, y nuestro objetivo será determinar si CP es un polinomio; de ser así, entonces estaremos probando que la declaración inicial es cierta.

[Notebook Parte 2](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/STARKS101/STARK101_res/STARK101_Parte2_resuelta.ipynb)

[El código Parte 2](https://github.com/Nadai2010/Pioneros-Clase-3-Maths-STARKs-101/blob/master/STARKS101/STARK101_click/STARK101_Parte2_click.py) Deberá encontrarse dentro de la carpeta del Archivo `STARK101_Parte2_click.py` para revisarlo y ejecutarlo, en este caso use en su terminal el siguiente comando:

```bash
python3.9 STARK101_Parte2_click.py
```

Deberá imprimirle la Parte 2 completa.

![Graph](/Im%C3%A1genes/Parte2.png)

<div align="center">
    <h2 id="STARKS - Parte 3">STARKS - Parte 3</h2>
</div>

En esta sección se desarrolla lo relacionado al protocolo FRI. En lugar de probar que CP es un polinomio, probaremos que CP es cercano a un polinomio de bajo grado, con eso es suficiente para nuestros fines y en este apartado se describen los pasos necesarios para llevarlo a cabo: Empezamos con una función, recibimos un elemento beta aleatorio y aplicamos el Operador FRI para obtener una nueva función. Se realiza este proceso varias veces hasta que se obtiene el valor de una constante, que será enviada al verificador.

[Notebook Parte 3](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/STARKS101/STARK101_res/STARK101_Parte3_resuelta.ipynb)

[El código Parte 3](https://github.com/Nadai2010/Pioneros-Clase-3-Maths-STARKs-101/blob/master/STARKS101/STARK101_click/STARK101_Parte3_click.py) Deberá encontrarse dentro de la carpeta del Archivo `STARK101_Parte3_click.py` para revisarlo y ejecutarlo, en este caso use en su terminal el siguiente comando:

```bash
python3.9 STARK101_Parte3_click.py
```

Deberá imprimirle la Parte 3 completa.

![Graph](/Im%C3%A1genes/Parte3.png)

<div align="center">
    <h2 id="STARKS - Parte 4">STARKS - Parte 4</h2>
</div>

La prueba entera está dividida en dos segmentos: El primero es el compromiso (commitment) que fue desarrollado en las tres primeras partes. En esta sección se describe la fase de descompromiso (decommitment phase), se ofrecerán detalles de la prueba y la manera en que el probador puede convencer al verificador de que realmente elaboró todos los cálculos de manera correcta.

[Notebook Parte 4](https://github.com/Nadai2010/Pioneros-Maths-STARKs-101/blob/master/STARKS101/STARK101_res/STARK101_Parte1_resuelta.ipynb)

[El código Parte 4](https://github.com/Nadai2010/Pioneros-Clase-3-Maths-STARKs-101/blob/master/STARKS101/STARK101_click/STARK101_Parte4_click.py) Deberá encontrarse dentro de la carpeta del Archivo `STARK101_Parte4_click.py` para revisarlo y ejecutarlo, en este caso use en su terminal el siguiente comando:

```bash
python3.9 STARK101_Parte4_click.py
```

Deberá imprimir la Parte 4 completa y por primera vez ha creado una STARK. ¡Enhorabuena!

![Graph](/Im%C3%A1genes/Parte4.gif)

