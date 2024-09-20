# Cliente whodrug PYTHON3

## Requerimientos

* python3
* credeciales para el consumo del API de WhoDrug
  * UMC\_CLIENT\_KEY= \[valor\]
  * UMC\_LICENSE\_KEY= \[valo\]

## Ejecución

1. Mediante una interfaz de consola.
2. Nos ubicamos en el directorio 'cliente\_python'.
3. Ejecutamos el comando.

```sh
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python2 main.py
```

## Salida

se creará un archivo en formato json con el nombre [yyyy_mm_dd]_whodrug.json, con la fecha en la que se realiza la descarga.
ejemplo: 2024_01_01_whodrug.json
