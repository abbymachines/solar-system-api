from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, chemical_composition):
        self.id = id
        self.name = name
        self.description = description
        self.composition = chemical_composition


planets = [
    Planet(1, "Mercury", "dark gray", "terrestrial"), 
    Planet(2, "Venus", "light yellow", "terrestrial"),
    Planet(3, "Earth", "blue and green", "terrestrial"),
    Planet(4, "Mars", "red", "terrestrial"),
    Planet(5, "Jupiter", "orange and brown", "gas giant")
]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "chemical composition": planet.composition
        })
    return jsonify(planets_response)

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} not valid"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
        
    abort(make_response({"message": f"planet {planet_id} not found"}, 404))

def make_dict(planet):
    return dict(
                id = planet.id,
                name= planet.name,
                description= planet.description,
                composition= planet.composition
            )

@bp.route("/<planet_id>", methods = ["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)   
    return make_dict(planet)