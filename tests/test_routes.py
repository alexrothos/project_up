import unittest
import requests_mock
import json
from app import app, db
from app.routes import get_data

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_data(self):
        with requests_mock.Mocker() as m:
            m.get("http://49.12.237.145:5150/", status_code=200, text='{"key": "value"}')
            data = get_data()
            self.assertIsNotNone(data)
            self.assertEqual(data, {"key": "value"})

    def test_index(self):
        with requests_mock.Mocker() as m:
            m.get("http://49.12.237.145:5150/", status_code=200, text=json.dumps({
                "company": {
                    "display_name": "Test Company",
                    "address_detail": "Test Address",
                    "city_name": "Test City",
                    "region_name": "Test Region",
                    "zip_code": "Test Zip"
                },
                "company_employees": [{
                    "employee_id": 1,
                    "fullname": "Test Employee",
                    "email": "test@email.com",
                    "phoneNumber": "1234567890"
                }],
                "offer": {
                    "product_1_budget": 100,
                    "product_1_issuing_value": 10,
                    "product_1_mailing_value": 5,
                    "product_1_value": 15,
                    "product_2_budget": 200,
                    "product_2_issuing_value": 20,
                    "product_2_mailing_value": 10,
                    "product_2_value": 30,
                    "product_3_budget": 300,
                    "product_3_issuing_value": 30,
                    "product_3_mailing_value": 15,
                    "product_3_value": 45
                }
            }))
            response = self.app.get('/')
            data = json.loads(response.data)
            self.assertEqual(data["message"], "Data saved successfully")
            self.assertEqual(data["code"], 200)
