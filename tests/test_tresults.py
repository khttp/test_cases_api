import unittest
from app import create_app
from models.model import db
app = create_app()
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
        
    def test_recording_test_results(self):
        """Verify successful testcase creation."""
        # Test implementation here...
        data ={ "name":"test_case_1",
              "description":"test_case_1 description"} 
        response = self.app.post('/create_test_case', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_test_resutls_for_asset_id(self,asset_id):
        """Verify failed registration."""
        # Test implementation here...
        pass

if __name__ == '__main__':
    # Get test case names and descriptions
    unittest.main()
