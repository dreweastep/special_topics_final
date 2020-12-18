#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self): # Intialize app for testing
        app.app.testing = True
        self.app = app.app.test_client() 

    def test_index(self): # Ensure base route works correctly
        rv = self.app.get('/') # Get request on base route
        self.assertEqual(rv.status, '200 OK') # Assert route status is equal to 200

    def test_bad_route(self): # Ensure non existent route returns 404
        rv = self.app.get('/badRoute')
        self.assertEqual(rv.status, '404 NOT FOUND')

    def test_get_one_temp(self): # Ensure get one temp route works, also ensures db connection is live
        rv = self.app.get('/get_one_temp_api')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
