from flask import Blueprint, request, jsonify
from app.models import db, Material
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('main', __name__)

@bp.route('/materials', methods=['POST'])
@jwt_required()
def create_material():
    data = request.get_json()
    new_material = Material(
        name=data['name'],
        type=data['type'],
        expiry_date=data['expiry_date']
    )
    db.session.add(new_material)
    db.session.commit()
    return jsonify({'message': 'Material created successfully'}), 201

@bp.route('/materials/<int:id>', methods=['PATCH'])
@jwt_required()
def update_material(id):
    data = request.get_json()
    material = Material.query.get_or_404(id)
    material.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Material status updated successfully'}), 200

