# my-movie-api
curso de FastApi introductorio de platzi

## Creación del entorno virtula en ubuntu

* Creación del entorno virtual
    ```sh
    python3 -m venv venv
    ```

* Activación del entorno virtual

    ```sh
    source venv/bin/activate
    ```
---

## Creación del entorno virtual en windows
* creación del entorno virtual
    ```sh
    python -m venv env
    ```
* activación del entorno vitual
    ```sh
    venv/Scripts/activate
    ```
---
## Desactivar el entorno virtual
```sh
deactivate
```

---
## Instalaciòn de los modulos que vamos a necesitar para crear la app

* instalacion de fastapi en ubuntu
    ```sh
    pip3 install fastapi
    ```
* instalación de fastApi en windows
    ```sh
    pip install fastapi
    ```
## Actualizar pip

```sh
python -m pip install --upgrade pip
```

## instalación del modulo donde va a correr, uvicorn
```sh
pip install uvicorn
```
## Correr la app
```sh
uvicorn main:app 
```
## Correr la app, pero que se recarge automaticamente

```sh
uvicorn main:app --reload
```

## Correr la app pero cambiando el puerto
```sh
uvicorn main:app --reload --port 1234
```
## Correr la app la app tanto en el pc como en el celular
```sh
uvicorn main:app --reload --port 1234 -- host 0.0.0.0
```

## Agregar todos los modulos requirements.txt para poderlos instalar despues
```sh
pip3 freeze > requeriments.txt
```

* ver la documentación de Swagger agregando docs

    http://127.0.0.1:8000/docs

## Cambiando el nombre de la App y versión
```py
from fastapi import FastAPI

app = FastAPI()  #creación de una instancia
app.title = "My aplicación con FastAPI"  #Colocar nombre a la app
app.version = "0.0.1" #Colocar version en especifico

#creacion del endpoin
@app.get('/', tags=['home']) #Se agrega el home para agrupar determinadas rutas
def message():
    return "Hello world! desde mi celular"

```

## Metodos HTTP
Es aquel que define el conjunto de metodos de peticiones que indica la acción que se desea realizar para un recurso determinado del servidor.

Los principales metodos usados por una **API** es:

* **_POST:_** crea un recurso nuevo.
* **_PUT:_** Modifica un recurso existente.
* **_GET:_** consulta informaciòn de un recurso.
* **_DELETE:_** Elimina un recurso

## creación de la ruta movies y metodo GET

```sh
from fastapi import FastAPI
from fastapi.responses import HTMLResponse #importaciòn de la clase para utilizar html

app = FastAPI() 
app.title = "My aplicación con FastAPI" 
app.version = "0.0.1" 

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]
#creacion del endpoin
@app.get('/', tags=['home']) 
def message():
    return HTMLResponse('<h1>Hello world</h1>') #utilizando html

#creaciòn de la ruta peliculas, y la etiqueta peliculas
@app.get('/movies', tags=['movies'])
def get_movies(): #devuelve el listado de las peliculas
    return movies

```

