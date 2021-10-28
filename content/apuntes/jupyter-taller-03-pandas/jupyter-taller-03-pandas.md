Title: Proyecto Jupyter (parte 3) Pandas
Slug: jupyter-taller-03-pandas
Summary: Terminamos el Taller de Juypter Notebook usando el paquete Pandas con datos abiertos referentes a casos COVID-19 en México.
Tags: python, jupyter
Date: 2021-10-26 22:20:00
Modified: 2021-10-27 20:00:00
Category: Apuntes
Preview: jupyter.png


## Descargar

Puede obtener el contenido de esta página como un _notebook_:

- [jupyter-taller-03-pandas.ipynb](jupyter-taller-03-pandas.ipynb)

## Intrucción a Pandas

Estudiaremos los datos abiertos referentes a casos [COVID-19 en México](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico).

1. Descargue **datos_abiertos_covid19.zip** en el vínculo anterior.
2. Descomprima el archivo y póngalo en el mismo directorio donde está este _notebook_.
3. Cambie el nombre del archivo en `archivo_csv = Path("______COVID19MEXICO.csv")`

Ejecutamos en **Jupyter Notebook** la siguiente celda esperando ver el mensaje "Ya veo el archivo".

    # Pathlib es para usar archivos de nuestro sistema operativo
    from pathlib import Path

    archivo_csv = Path("______COVID19MEXICO.csv")
    if archivo_csv.exists():
        print("Ya veo el archivo", archivo_csv.name)
    else:
        raise Exception("No lo encuentro")

Si no lo ha hecho, instale en su entorno virtual el paquete pandas con `pip install pandas`

    # Pandas es excelente para analizar datos
    import pandas as pd

    # Cargar el archivo. NOTA: Se tarda un buen tiempo por su tamaño, si falla agregue low_memory=False
    covid19 = pd.read_csv(archivo_csv, low_memory=False)

    # Dar un vistazo a sus primeros renglones
    covid19.head()

Para conocer las columnas de este _dataset_ baje el [Diccionario de Datos](https://www.gob.mx/salud/documentos/datos-abiertos-152127).

    # Mostrar las columnas
    covid19.columns

Apliquemos dos filtros, para quedarnos con los datos de un estado y los resultados positivos.

    # Coahuila de Zaragoza es la entidad 5
    # RESULTADO_LAB 1 es POSITIVO A SARS-COV-2
    entidad = covid19[(covid19.ENTIDAD_RES == 5) & (covid19.RESULTADO_LAB == 1)]
    len(entidad)

Seleccionamos algunas de de las columnas y establecemos como categorias aquellas que son cualitativas.

    # Elegimos unas columnas y las redefinimos como categorias para se cuantifiquen
    entidad = entidad[["SEXO", "ENTIDAD_RES", "MUNICIPIO_RES", "FECHA_DEF", "INTUBADO", "EDAD"]]
    entidad.SEXO = entidad.SEXO.astype('category')
    entidad.ENTIDAD_RES = entidad.ENTIDAD_RES.astype('category')
    entidad.MUNICIPIO_RES = entidad.MUNICIPIO_RES.astype('category')
    entidad.INTUBADO = entidad.INTUBADO.astype('category')
    entidad.info()

La columna SEXO tiene los valores 1 o 2. Vamos a reemplazarlos por MUJER y HOMBRE.

    # Los sexos
    entidad.SEXO.cat.categories

    # Reemplazar los sexos de numero a texto
    entidad["SEXO"] = entidad["SEXO"].replace(to_replace=[1,2], value=["MUJER","HOMBRE"])

En MUNICIPIO_RES se usan números. Vamos a cambiarlos por sus nombres cargando [municipios_coahuila.csv](municipios_coahuila.csv)

    # Los municipios
    entidad.MUNICIPIO_RES.cat.categories

    # Cargar listados con las claves de los municipios de Coahuila
    import csv
    claves = []
    nombres = []
    with open("municipios_coahuila.csv", encoding="utf8") as puntero:
        renglones = csv.DictReader(puntero)
        for renglon in renglones:
            claves.append(int(renglon["CLAVE_MUNICIPIO"]))
            nombres.append(renglon["MUNICIPIO"])
    print(claves)
    print(nombres)

    # Reeplazar esas claves por los nombres de los municipios de Coahuila
    entidad["MUNICIPIO_RES"] = entidad["MUNICIPIO_RES"].replace(to_replace=claves, value=nombres)
    entidad.head()

Al dar un vistazo en FECHA_DEF notamos que se trata como categorías, no como tiempos. En una próxima entrega resolveremos este reto.

    # Las fechas de defuncion
    entidad.FECHA_DEF.unique()

Elaboremos un reporte listando los casos positivos por sexo y municipio.

    # Pivot table por sexo
    entidad.pivot_table(
        index=["MUNICIPIO_RES"],
        columns=pd.Grouper(key="SEXO"),
        values="ENTIDAD_RES",
        aggfunc='count',
    )

Y terminamos con un reporte con las cantidades de casos positivos por edad y municipio.

    # Pivot table por edad
    entidad.pivot_table(
        index=["MUNICIPIO_RES"],
        columns=pd.Grouper(key="EDAD"),
        values="ENTIDAD_RES",
        aggfunc='count',
    )

## Ir a la primera parte [Proyecto Jupyter: Instalar](../jupyter-taller-01-instalar/)

## Ir a la segunda parte [Proyecto Jupyter: Python Básico](../jupyter-taller-02-python-basico/)
