#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client() 

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_bad_route(self):
        rv = self.app.get('/badRoute')
        self.assertEqual(rv.status, '404 NOT FOUND')

    def test_get_one_temp(self):
        rv = self.app.get('/get_one_temp_api')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
