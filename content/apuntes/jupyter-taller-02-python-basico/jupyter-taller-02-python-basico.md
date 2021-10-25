Title: Proyecto Jupyter (parte 2) Python Básico
Slug: jupyter-taller-02-python-basico
Summary: Segunda parte del taller sobre el proyecto Jupyter donde se practican algunos ejercicios básicos de Python.
Tags: Python
Date: 2021-10-25 09:21:00
Modified: 2021-10-25 09:21:00
Category: Apuntes
Preview: jupiter.png


## Introducción a Python

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Python usa tipado dinámico y conteo de referencias para la administración de memoria.

Python fue creado a finales de los ochenta4​ por [Guido van Rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum).

## Variables

Las variables se definen de forma dinámica, lo que significa que no se tiene que especificar cuál es su tipo de antemano y puede tomar distintos valores en otro momento, incluso de un tipo diferente al que tenía previamente. Se usa el símbolo = para asignar valores.

    # Calcular el área de un rectángulo
    ancho = 5
    alto = 12
    area = ancho * alto
    print("Área", area)

## Comentarios

Los comentarios se pueden poner de dos formas. La primera y más apropiada para comentarios largos es utilizando la notación ''' comentario ''', tres apóstrofos o comillas de apertura y tres de cierre. La segunda notación utiliza el símbolo #, y se extienden hasta el final de la línea.

## Identación

Python está destinado a ser un lenguaje de fácil lectura. Su formato es visualmente ordenado y, a menudo, usa palabras clave en inglés donde otros idiomas usan puntuación. A diferencia de muchos otros lenguajes, **no utiliza llaves para delimitar bloques, ni se necesitan puntos y comas después de las declaraciones** (aunque se puede, pero es rara la vez que se usan).

El contenido de los bloques de código (bucles, funciones, clases, etc.) es delimitado mediante espacios (o tabuladores), conocidos como indentación. **El estándar es usar cuatro espacios para identar.**
