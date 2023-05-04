from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

# planets = [
#     Planet(1, "Mercury", "dark gray", "terrestrial"), 
#     Planet(2, "Venus", "light yellow", "terrestrial"),
#     Planet(3, "Earth", "blue and green", "terrestrial"),
#     Planet(4, "Mars", "red", "terrestrial"),
#     Planet(5, "Jupiter", "orange and brown", "gas giant")
# ]

bp = Blueprint("planets", __name__, url_prefix="/planets")
# @bp.route("",methods=["GET"])

# helper function
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet {planet_id} not valid"}, 400))
    
    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet {planet_id} not found"}, 404))
    
    return planet

# routes
@bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    planet = validate_planet(id)
    
    return planet.to_dict(), 200

@bp.route("", methods=["POST"])
def create_planet():
    request_body=request.get_json()
    
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        composition=request_body["composition"]
    )
    
    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    planets_list = []
    for planet in planets:
        planets_list.append(planet.to_dict())
    
    return jsonify(planets_list), 200

# @bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "chemical composition": planet.composition
#         })
#     return jsonify(planets_response)

# def make_dict(planet):
#     return dict(
#                 id = planet.id,
#                 name= planet.name,
#                 description= planet.description,
#                 composition= planet.composition
#             )

# @bp.route("/<planet_id>", methods = ["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)   
#     return make_dict(planet)