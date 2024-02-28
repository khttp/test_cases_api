import unittest
from app import app
from models.model import db
ap = app.create_app()
class MyTestCase(unittest.TestCase):
    """Test case for createing test case functionality."""
    def setUp(self):
        """Set up test case."""
        # Set up test case here...
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
        self.app = app.test_client()
        db.create_all()  
    def tearDown(self) -> None:
        # Tear down test case here...
        db.session.remove()
        db.drop_all()
        
    def test_creating_test_case(self):
        """Verify successful testcase creation."""
        # Test implementation here...
        data ={ "name":"test_case_1",
              "description":"test_case_1 description"} 
        response = self.app.post('/create_test_case', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_test_cases(self):
        """Verify failed registration."""
        # Test implementation here...
        pass
    def test_get_test_case(self ,id):
        """retrieve a specific test case"""
        pass
    def test_update_test_case(self):
        """verify success of the update of the test case"""
        pass
    def test_delete_test_case(self):
        """verify deletion of testcase"""
        pass
    
    
if __name__ == '__main__':
    # Get test case names and descriptions
    unittest.main()
