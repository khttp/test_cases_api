from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from models.model import db, TestResult,TestAsset,TestCase
result_api = Blueprint('result_api',__name__)

# Recording the execution result of a test case for a specific test asset in the SQLite database

@result_api.route('/create_test_result',methods=['POST'])    
def create_test_result():
    try:
        data = request.json
        result = data['result']
        test_case_id = data['test_case_id']
        test_asset_id = data['test_asset_id']
        
        test_cases = TestCase.query.all()
        test_assets =TestAsset.query.all()
       
        testcasesid=[True for testcase in test_cases if testcase.id == test_case_id]
        testassetsid =[True for testasset in test_assets if testasset.id == test_asset_id]
        if True not in testcasesid :
            return jsonify({'message':"test case not found"}),404
        if True not in testassetsid:
            return jsonify({'message':"test asset not found"}),404
        test_result = TestResult(
            result=result,
            test_case_id=test_case_id,
            test_asset_id=test_asset_id
            )
        db.session.add(test_result)
        db.session.commit()
        return jsonify({'message': 'Test result created successfully'}), 201
    except Exception as e:
        return jsonify({'message':f'Error {e}'}),500
    
#Retrieving the execution results of all test cases for a specific test asset from the SQLite database
@result_api.route('/get_test_results/<int:asset_id>',methods=['GET'])
def get_test_results(asset_id):
    try:
        # retrieve all results of all testcases for a specific test asset
        results = db.session.query(TestResult).filter_by(test_asset_id=asset_id).all()
        if len(results) == 0:
            return 'no results'
        formatted_results = [{
            'id': result.id,
            'result': result.result,
            'test_case_id': result.test_case_id,
            'test_asset_id': result.test_asset_id
        } for result in results]
        return jsonify({"results":formatted_results}), 200 
    except Exception as e:
        return jsonify({'message':f'Error {e}'})