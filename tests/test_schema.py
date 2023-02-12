import unittest
from marshmallow import ValidationError
from app.schemas import CompanySchema, CompanyEmployeeSchema, OfferSchema

class TestMarshmallowSchemas(unittest.TestCase):
    def test_company_schema(self):
        company_data = {
            "display_name": "Test Company",
            "address_detail": "Test Address",
            "city_name": "Test City",
            "region_name": "Test Region",
            "zip_code": "Test Zip",
            "employees": [],
            "offers": []
        }
        company = CompanySchema().load(company_data)
        self.assertEqual(company["display_name"], "Test Company")
        self.assertEqual(company["address_detail"], "Test Address")
        self.assertEqual(company["city_name"], "Test City")
        self.assertEqual(company["region_name"], "Test Region")
        self.assertEqual(company["zip_code"], "Test Zip")
        self.assertEqual(company["employees"], [])
        self.assertEqual(company["offers"], [])

        company_data_invalid = {
            "display_name": 123,
            "address_detail": 123,
            "city_name": 123,
            "region_name": 123,
            "zip_code": 123,
            "employees": [],
            "offers": []
        }
        with self.assertRaises(ValidationError):
            CompanySchema().load(company_data_invalid)

    def test_company_employee_schema(self):
        employee_data = {
            "company_id": 1,
            "employee_id": 1,
            "fullname": "Test Employee",
            "email": "test@email.com",
            "phoneNumber": "1234567890"
        }
        employee = CompanyEmployeeSchema().load(employee_data)
        self.assertEqual(employee["company_id"], 1)
        self.assertEqual(employee["employee_id"], 1)
        self.assertEqual(employee["fullname"], "Test Employee")
        self.assertEqual(employee["email"], "test@email.com")
        self.assertEqual(employee["phoneNumber"], "1234567890")

        employee_data_invalid = {
            "company_id": "invalid",
            "employee_id": "invalid",
            "fullname": 123,
            "email": 123,
            "phoneNumber": 123
        }
        with self.assertRaises(ValidationError):
            CompanyEmployeeSchema().load(employee_data_invalid)
            
    def test_offer_schema(self):
        offer_data = {
            "company_id": 1,
            "offer_id": 1,
            "title": "Test Offer",
            "description": "Test Description",
            "salary": 1000,
            "location": "Test Location",
            "requirements": "Test Requirements",
            "benefits": "Test Benefits",
            "date_posted": "2020-01-01",
            "date_expires": "2020-01-01",
            "status": "Test Status"
        }
        offer = OfferSchema().load(offer_data)
        self.assertEqual(offer["company_id"], 1)
        self.assertEqual(offer["offer_id"], 1)
        self.assertEqual(offer["title"], "Test Offer")
        self.assertEqual(offer["description"], "Test Description")
        self.assertEqual(offer["salary"], 1000)
        self.assertEqual(offer["location"], "Test Location")
        self.assertEqual(offer["requirements"], "Test Requirements")
        self.assertEqual(offer["benefits"], "Test Benefits")
        self.assertEqual(offer["date_posted"], "2020-01-01")
        self.assertEqual(offer["date_expires"], "2020-01-01")
        self.assertEqual(offer["status"], "Test Status")

        offer_data_invalid = {
            "company_id": "invalid",
            "offer_id": "invalid",
            "title": 123,
            "description": 123,
            "salary": "invalid",
            "location": 123,
            "requirements": 123,
            "benefits": 123,
            "date_posted": 123,
            "date_expires": 123,
            "status": 123
        }
        with self.assertRaises(ValidationError):
            OfferSchema().load(offer_data_invalid)