# • Creating a new test case and storing it in the SQLite database
from flask import Blueprint, request, jsonify
from models.model import db, TestCase
api = Blueprint('api',__name__)

# create a new test case and store it in the SQLite database
@api.route('/create_test_case',methods=['POST'])
def create_test_case():
    try:
        data = request.json
        name = data['name']
        description = data['description']
        test_case = TestCase(name=name,description=description)
        db.session.add(test_case)
        db.session.commit()
        return jsonify({'message': 'Test case created successfully'}), 201
    except Exception as e:
        return f'Error {e}',500
    
# • Retrieving a list of all test cases from the SQLite database
@api.route('/get_test_cases',methods=['GET'])
def get_test_cases():
    try:
        test_cases = TestCase.query.all()
        formatted_test_cases = [{
        'id': test_case.id,
        'name': test_case.name,
        'description': test_case.description
        } for test_case in test_cases]
        if len(formatted_test_cases) == 0 :
            return 'no testcases'
        return jsonify({"test_cases":formatted_test_cases}), 200
    except Exception as e:
        return f'Error {e}',500

# • Retrieving a single test case by its ID from the SQLite database
@api.route('/get_test_case/<int:id>',methods=['GET'])
def get_test_case(id):
    try:
        test_case = TestCase.query.get_or_404(id)
        formatted_test_case = {
        'id': test_case.id,
        'name': test_case.name,
        'description': test_case.description
        }
        return jsonify({"test_case":formatted_test_case}), 200
    except Exception as e:
        return f'Error {e}',500

# • Updating an existing test case in the SQLite database
@api.route('/update_test_case/<int:id>',methods=['PUT'])
def update_test_case(id):
    try:
        test_case = TestCase.query.get_or_404(id)
        data=request.json
        test_case.name = data['name']
        test_case.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Test case updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return f'Error {e}',500

# Deleting a test case by its ID from the SQLite database
@api.route('/delete_test_case/<int:id>',methods=['DELETE'])
def delete_test_case(id):
    try:
        test_case = TestCase.query.get_or_404(id)
        db.session.delete(test_case)
        db.session.commit()
        return jsonify({'message':f'test case with the name {test_case.name} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
