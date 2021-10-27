Title: Proyecto Jupyter (parte 2) Python Básico
Slug: jupyter-taller-02-python-basico
Summary: Segunda parte del taller sobre el proyecto Jupyter donde se practican algunos ejercicios básicos de Python.
Tags: python, jupyter
Date: 2021-10-25 09:21:00
Modified: 2021-10-25 22:10:00
Category: Apuntes
Preview: jupyter.png


## Descargar

Puede obtener el contenido de esta página como un _notebook_:

- [jupyter-taller-02-python-basico.ipynb](jupyter-taller-02-python-basico.ipynb)

## Introducción a Python

Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Python usa tipado dinámico y conteo de referencias para la administración de memoria.

Python fue creado a finales de los ochenta​ por [Guido van Rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum).

De forma sencilla, vamos a conocer algunos conceptos básicos y ejemplos de Python...

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

## Condiciones

Una sentencia condicional **if** ejecuta su bloque de código interno solo si se cumple cierta condición. Se define usando la palabra clave **if** seguida de la condición, y el bloque de código. Condiciones adicionales, si las hay, se introducen usando **elif** seguida de la condición y su bloque de código. Todas las condiciones se evalúan secuencialmente hasta encontrar la primera que sea verdadera, y su bloque de código asociado es el único que se ejecuta. Opcionalmente, puede haber un bloque final (la palabra clave **else** seguida de un bloque de código) que se ejecuta solo cuando todas las condiciones fueron falsas.

    # Comparar textos
    fruta_1 = 'manzana'
    fruta_2 = 'MANZANA'
    if fruta_1 == fruta_2:
        print('Son iguales')
    else:
        print('Son diferentes')
        if len(fruta_1) > len(fruta_2):
            print('Tiene más letras el primero')
        elif len(fruta_1) == len(fruta_2):
            print('Tienen la misma cantidad de letras')
        else:
            print('Tiene más letras el segundo')
    if fruta_1.lower() == fruta_2.lower():
        print('Si las cambio a minúsculas ¡SON IGUALES!')

## Tipos de datos

De inicio se pueden tener valores boleanos, enteros, números racionales y textos.

El tipo de datos **listado** es una secuencia de datos del mismo tipo o diferentes.

    # Mostrar las vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    print('Estas son las vocales:')
    for vocal in vocales:
        print(vocal)
    print()

## Funciones

Una función es una palabra clave seguida de paréntesis, dentro de estos puede haber parámetros.

Puede entregar uno o varios resultados por un **return**.

    # La función len entrega la cantidad de caracteres de un texto
    nombre = "Miguel de Icaza"
    print('La cantidad de letras que tiene es', len(nombre))

## Métodos

Python es un lenguaje orientado a objetos. Prácticamente cualquier dato es un objeto que tiene propiedades y métodos. Depués de un objeto se escribe un punto y el nombre del método a llamar, con parámetros entre paréntesis de ser necesario.

    # Los textos tienen los métodos
    # - upper para convertir a mayúsculas y
    # - lower para convertir a minúsculas
    print('En mayúsculas es {}'.format(nombre.upper()))
    print('En minúsculas es {}'.format(nombre.lower()))

## Bucles

La estructura **for** es sencilla de hacer un ciclo...

    # De inicio, crear una tabla de multiplicar del dos
    factor = 2
    for numero in [1, 2, 3, 4, 5]:
        print(' {} x {} = {} '.format(numero, factor, numero * factor))

    # Luego, hagamos más tablas
    for factor in range(1, 5):
        print(f'Tabla del {factor}')
        print()
        for numero in range(1, 5):
            print(f' {numero} x {factor} = {numero * factor} ')
        print()

## Funciones hechas por nosotros mismos

Las funciones se definen con la palabra clave **def**, seguida del nombre de la función y sus parámetros.

El valor devuelto en las funciones será el dado con la instrucción **return**.

    # Vamos a eliminar las vocales
    def quitar_vocales(nombre):
        nombre_sin_vocales = ''
        for numero in range(0, len(nombre)):
            letra = nombre[numero].lower()
            if letra not in vocales:
                nombre_sin_vocales = nombre_sin_vocales + letra
        return(nombre_sin_vocales)

    print(quitar_vocales('Tim Berners-Lee'))
    print(quitar_vocales('Richard Matthew Stallman'))
    print(quitar_vocales('Linus Benedict Torvalds'))

    # Vamos a escribir al revés los nombres
    def cambiar_al_reves_1(nombre):
        al_reves = ''
        for posicion in range(len(nombre) - 1, -1, -1):
            al_reves = al_reves + nombre[posicion]
        return(al_reves.upper())

    # Ahora usando reverse
    def cambiar_al_reves_2(nombre):
        lista = list(reversed(nombre))
        al_reves = ''.join(lista)
        return(al_reves.upper())

    # Y ahora usando join
    def cambiar_al_reves_3(nombre):
        al_reves = ''.join(list(reversed(nombre)))
        return(al_reves.upper())

    print(cambiar_al_reves_1('Tim Berners-Lee'))
    print(cambiar_al_reves_1('Richard Matthew Stallman'))
    print(cambiar_al_reves_1('Linus Benedict Torvalds'))
