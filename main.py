from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional



app = FastAPI()

#Para cambiar el nombre de la aplicacion
app.title = "Mi aplicación con FastAPI"

#Para cambiar la version de la aplicacion
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022) # con le indico el maximo del numero del que no puede pasar
    rating: float = Field(ge=1, le=10) #mínimo y máximo rating
    category: str = Field(min_length=5, max_length=15)


    # creo una clase que queda como por defecto ya lista.
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi Película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 7,
                "category": "Acción"
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } ,
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    }
]


#los tags nos permite agrupar las rutas de la aplicación
@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

#obtener las películas mediante un id
@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(default=1, ge=1, le=2000)):
    for item in movies:
        if item["id"] == id:
            return item
    return []

#obtener las películas mediante categoría

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)): 

    #funcionalidad para filtrar las películas por categoría
    return [item for item in movies if item['category'] == category]

@app.post('/movies/', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie.dict())  #Se guarda la peli como diccionario usando dict para evitar errores
    return movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id: 
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
    return movies 




