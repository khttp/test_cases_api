
# • Creating a new test case and storing it in the SQLite database
from flask import Blueprint, request, jsonify
from models.model import db, TestAsset
asset_api = Blueprint('asset_api',__name__)

# create a new test asset and store it in the SQLite database

@asset_api.route('/create_test_asset',methods=['POST'])
def create_test_asset():
    try:
        data = request.json
        name = data['name']
        test_case_id = data['test_case_id']
        test_asset = TestAsset(name=name,test_case_id=test_case_id)
        db.session.add(test_asset)
        db.session.commit()
        return jsonify({'message': 'Test asset created successfully'}), 201
    except Exception as e:
        return f'Error {e}',500
# • Retrieving a list of all test assets from the SQLite database
@asset_api.route('/get_test_assets',methods=['GET'])
def get_test_assets():
    try:
        test_assets = TestAsset.query.all()
        formatted_test_assets = [{
        'id': test_asset.id,
        'name': test_asset.name,
        'test_case_id': test_asset.test_case_id
        } for test_asset in test_assets]
        if len(formatted_test_assets) == 0 :
            return 'no testassets'
        return jsonify({"test_assets":formatted_test_assets}), 200
    except Exception as e:
        return f'Error {e}',500

# • Retrieving a single test asset by its ID from the SQLite database
@asset_api.route('/get_test_asset/<int:id>',methods=['GET'])
def get_test_asset(id):
    try:
        test_asset = TestAsset.query.get_or_404(id)
        formatted_test_asset = {
        'id': test_asset.id,
        'name': test_asset.name,
        'test_case_id': test_asset.test_case_id
        }
        return jsonify({"test_asset":formatted_test_asset}), 200
    except Exception as e:
        return f'Error {e}',500

# • Updating an existing test asset in the SQLite database
@asset_api.route('/update_test_asset/<int:id>',methods=['PUT'])
def update_test_case(id):
    try:
        test_asset = TestAsset.query.get_or_404(id)
        data=request.json
        test_asset.name = data['asset']
        test_asset.test_case_id = data['test_case_id']
        db.session.commit()
        return jsonify({'message': 'Test asset updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return f'Error {e}',500

# Deleting a test asset by its ID from the SQLite database
@asset_api.route('/delete_test_asset/<int:id>',methods=['DELETE'])
def delete_test_case(id):
    try:
        test_asset = TestAsset.query.get_or_404(id)
        db.session.delete(test_asset)
        db.session.commit()
        return jsonify({'message':f'test asset with the name {test_asset.name} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message':f'Error {e}'}), 500
