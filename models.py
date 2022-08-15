"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Establishes the connection"""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """cupcakes have a flavor size image and rating"""
    __tablename__ = 'cupcakes'

    def __repr__(self):
        return f"<Cupcake {self.id} - {self.flavor}>"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    flavor = db.Column(db.String(50),
                    nullable=False)

    size = db.Column(db.String(50),
                    nullable=False)

    image = db.Column(db.String(150),
                    nullable=False, 
                    default="https://tinyurl.com/demo-cupcake")

    rating = db.Column(db.Float, 
                    nullable=False)