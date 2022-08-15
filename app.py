"""Flask app for Cupcakes"""
from flask import Flask, request, render_template, redirect, flash, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petadoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretdefinitelynotabletobeguessed'

connect_db(app)
db.create_all()

def serialize_cupcake(cupcake):
    """serialize a cupcake SQLAlchemy obj to dicationary"""
    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size":cupcake.size,
        "rating":cupcake.rating,
        "image":cupcake.image
    }

@app.route('/')
def home():
    """Render homepage"""
    return render_template('home.html')

@app.route('/api/cupcakes')
def list_all_cupcakes():
    """List all cupcakes"""
    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:id>')
def list_single_cupcake(id):
    """List a single cupcake with an id"""
    cupcake = Cupcake.query.get_or_404(id)
    serialized = serialize_cupcake(cupcake)
    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a cupcake"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating= request.json["rating"]
    image = request.json["image"]
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)
    return (jsonify(cupcake=serialized),201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Update an existing cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.add(cupcake)
    db.session.commit()
    serialized= serialize_cupcake(cupcake)
    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")