from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


planets = [
    Planet(1, "Mercury", "dark gray"), 
    Planet(2, "Venus", "light yellow"),
    Planet(3, "Earth", "blue and green")
]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("/<planet_id>", methods = ["GET"])

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return {"message": f"planet {planet_id} not valid"}, 400
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
        
    return {"message": f"planet {planet_id} not found"}, 404
    

def handle_planet(planet_id):
    planet = validate_planet(planet_id)   
    return dict(
                id = planet.id,
                name= planet.name,
                description= planet.description
            )