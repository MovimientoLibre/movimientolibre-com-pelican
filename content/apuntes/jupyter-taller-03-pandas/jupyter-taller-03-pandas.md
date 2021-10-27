Title: Proyecto Jupyter (parte 3) Pandas
Slug: jupyter-taller-02-python-basico
Summary: Conoceremos cómo trabajar con gran cantidad de datos abiertos en la tercera parte del taller sobre el proyecto Jupyter.
Tags: python, jupyter
Date: 2021-10-26 22:20:00
Modified: 2021-10-26 22:20:00
Category: Apuntes
Preview: jupyter.png
Status: draft


Estudiaremos los datos abiertos sobre la [vacunación COVID-19 en México](https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico).

1. Descargue **datos_abiertos_covid19.zip** en el vínculo anterior.
2. Descomprima el archivo y póngalo en el mismo directorio donde está este _notebook_.
3. Cambie el nombre del archivo en `archivo_csv = Path("______COVID19MEXICO.csv")`

Ejecutamos en **Jupyter Notebook** la siguiente celda esperando ver el mensaje "Ya veo el archivo".

    # Pathlib es para usar archivos de nuestro sistema operativo
    from pathlib import Path

    archivo_csv = Path("211008COVID19MEXICO.csv")
    if archivo_csv.exists():
        print("Ya veo el archivo", archivo_csv.name)
    else:
        raise Exception("No lo encuentro")

Para conocer lo que significan las columnas del _dataset_ bajamos el [Diccionario de Datos](https://www.gob.mx/salud/documentos/datos-abiertos-152127).

