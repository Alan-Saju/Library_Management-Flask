import unittest
from flask import json
from app import app

class FlaskAPITestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_books(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['books']), 2)

    def test_add_book(self):
        new_book = {
            'title': 'New Book',
            'author': 'New Author',
            'published_year': 2022
        }
        response = self.client.post('/books', json=new_book)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], new_book['title'])

    def test_get_book(self):
        response = self.client.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Book One')

    def test_update_book(self):
        updated_data = {'title': 'Updated Book One'}
        response = self.client.put('/books/1', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Updated Book One')

    def test_delete_book(self):
        response = self.client.delete('/books/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Book deleted')

    def test_get_members(self):
        response = self.client.get('/members')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json['members']), 2)

    def test_add_member(self):
        new_member = {
            'name': 'New Member',
            'join_date': '2022-01-01'
        }
        response = self.client.post('/members', json=new_member)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], new_member['name'])

    def test_get_member(self):
        response = self.client.get('/members/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Member One')

    def test_update_member(self):
        updated_data = {'name': 'Updated Member One'}
        response = self.client.put('/members/1', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated Member One')

    def test_delete_member(self):
        response = self.client.delete('/members/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Member deleted')

if __name__ == '__main__':
    unittest.main()