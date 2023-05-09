from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    planet_id = db.Column("Planet", back_populates="id") 
    planet = db.relationship(db.Integer, db.ForeignKey("planet.id"))

