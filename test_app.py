import unittest
from app import app
import json
from config import API_KEY

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {'X-API-KEY': API_KEY}

    def test_status(self):
        resp = self.client.get('/status', headers=self.headers)
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])

    def test_chat_invalid(self):
        resp = self.client.post('/chat', headers=self.headers, json={})
        self.assertEqual(resp.status_code, 400)
        data = resp.get_json()
        self.assertFalse(data['success'])

    def test_chat_valid(self):
        resp = self.client.post('/chat', headers=self.headers, json={"messages": [{"role": "user", "content": "Halo AI"}]})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        self.assertIn('reply', data['data'])

    def test_generate_soal_invalid(self):
        resp = self.client.post('/generate-soal', headers=self.headers, json={})
        self.assertEqual(resp.status_code, 400)
        data = resp.get_json()
        self.assertFalse(data['success'])

    def test_generate_soal_valid(self):
        resp = self.client.post('/generate-soal', headers=self.headers, json={"topik": "matematika", "jumlah": 2, "tingkat": "SMP"})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        self.assertIn('soal', data['data'])

if __name__ == '__main__':
    unittest.main()
