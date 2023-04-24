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

def handle_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return (dict(
                id = planet.id,
                name= planet.name,
                description= planet.description
            ))
