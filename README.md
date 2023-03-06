my-movie-api
curso de FastApi introductorio de platzi

Creación del entorno virtula en ubuntu
Creación del entorno virtual

python3 -m venv venv
Activación del entorno virtual

source venv/bin/activate
Creación del entorno virtual en windows
creación del entorno virtual
python -m venv env
activación del entorno vitual
venv/Scripts/activate
Desactivar el entorno virtual
deactivate
Instalaciòn de los modulos que vamos a necesitar para crear la app
instalacion de fastapi en ubuntu
pip3 install fastapi
instalación de fastApi en windows
pip install fastapi
Actualizar pip
python -m pip install --upgrade pip
instalación del modulo donde va a correr, uvicorn
pip install uvicorn
Correr la app
uvicorn main:app 
Correr la app, pero que se recarge automaticamente
uvicorn main:app --reload
Correr la app pero cambiando el puerto
uvicorn main:app --reload --port 1234
Correr la app la app tanto en el pc como en el celular
uvicorn main:app --reload --port 1234 -- host 0.0.0.0
Agregar todos los modulos requirements.txt para poderlos instalar despues
pip3 freeze > requeriments.txt# fastapi
