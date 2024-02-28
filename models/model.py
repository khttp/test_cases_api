from flask_sqlalchemy import SQLAlchemy
from datetime import datetime   

db = SQLAlchemy()

# class TestCase(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text)
#     test_asset = db.relationship('TestAsset', back_populates='test_case')
#     test_results = db.relationship('ExecutionResults', back_populates='test_case')

# class TestAsset(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name= db.Column(db.String(100), nullable=False)
#     test_case_id = db.Column(db.Integer, db.ForeignKey('test_case.id'), nullable=False)
#     test_results = db.relationship('ExecutionResults', back_populates='test_asset')
    
# class ExecutionResults(db.Model):
#     id =db.Column(db.Integer, primary_key=True)
#     result = db.Column(db.String(50))
#     test_case_id = db.Column(db.Integer, db.ForeignKey('test_case.id'), nullable=False)
#     test_asset_id = db.Column(db.Integer, db.ForeignKey('test_asset.id'), nullable=False)


class TestCase(db.Model):
    __tablename__ = 'test_cases'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    test_assets = db.relationship("TestAsset", back_populates="test_case",load_on_pending=True)
    test_results = db.relationship("TestResult", back_populates="test_case",load_on_pending=True)

class TestAsset(db.Model):
    __tablename__ = 'test_assets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    test_case_id = db.Column(db.Integer, db.ForeignKey('test_cases.id'))
    test_case = db.relationship("TestCase", back_populates="test_assets",load_on_pending=True)
    test_results = db.relationship("TestResult", back_populates="test_asset",load_on_pending=True)

class TestResult(db.Model):
    __tablename__ = 'test_results'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    result = db.Column(db.String, nullable=False)
    execution_date = db.Column(db.DateTime,default=datetime.now())
    test_case_id = db.Column(db.Integer, db.ForeignKey('test_cases.id'))
    test_case = db.relationship("TestCase", back_populates="test_results")
    test_asset_id = db.Column(db.Integer, db.ForeignKey('test_assets.id'))
    test_asset = db.relationship("TestAsset", back_populates="test_results",
                                 load_on_pending=True)
  