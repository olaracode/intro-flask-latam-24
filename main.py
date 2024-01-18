from flask import Flask, request # importo flask

app = Flask(__name__) # Creado mi aplicacion de flask

# Mi primer endpoint
# Para ejecutar nuestro proyecto de flask
star_wars_characters = [
    {
        "id": 1,
        "name": "Luke Skywalker",
        "hair_color": "Blonde"
    },
    {
        "id": 2,
        "name": "C3PO",
        "hair_color": "N/A" # No Aplica
    },
    {
        "id": 3,
        "name": "R2-D2",
        "hair_color": "N/A"
    }
]

# GET -> Obtencion de data
# POST -> Creacion de DATA
# PATCH/PUT -> Actualizacion de DATA
# Delete -> Eliminacion de DATA

# @algo -> decorador en python
@app.route("/") # @app.route("/") define un endpoint
def hello_world():
    return {
        "data": "Mi primer endpoint",
        "status": "success"
    }

@app.route("/characters", methods=["GET"]) # GET
def get_characters():
    # EL RETURN DE LA FUNCION es lo que devuelve mi API
    return {
        "results": star_wars_characters,
        "count": len(star_wars_characters) # len(lista) devuelve el largo de la lista
    }

# No deberiamos definir dos decoradores de la api con el mismo path
# int | string
@app.route("/character/<int:id>", methods=["GET"])
def get_character_by_id(id):
    for character in star_wars_characters:
        if character["id"] == id:
            return{
                "character": character
            }
    
    # Manejando error
    return {
        "error": f"character with id: {id} not found"
    }, 404 # Not FOUND
    

@app.route("/character", methods=["POST"])
def create_character():
    body = request.json # Accedo al body(tipo JSON) de la peticion
    body_name = body.get("name", None) # Extrayendo el Key: Value name de el diccionario body. Si no existe name retorna None
    body_hair_color = body.get("hair_color", None)

    if body_name is None:
        return {
            "error": "El campo NAME es requerido para crear un personaje"
        }, 400
    elif body_hair_color is None:
        return {
            "error": "El campo hair_color es requerido para crear un personaje"
        }, 400


    # {  }
    return {
        "status": {
            "status_code": 201,
            "status_msg": "created",
            "date": "la fecha actual"
        },
        "character": {
            "name": body_name,
            "hair_color": body_hair_color,
            "id": 16
        }
    }, 201 # 201 -> created

