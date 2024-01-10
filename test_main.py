import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_item_route(self):
        response = self.app.post('/add', data={'item': 'Test Item'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_delete_item_route(self):
        # Assuming there's at least one item to delete
        response = self.app.get('/delete/0')
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_update_item_route(self):
        # Assuming there's at least one item to update
        response = self.app.post('/update/0', data={'new_item': 'Updated Item'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

if __name__ == '__main__':
    unittest.main()
