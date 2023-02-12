import unittest
from app import db, create_app
from app.models import Company, CompanyEmployee, Offer

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_company_model(self):
        company = Company(
            display_name='Test Company',
            address_detail='Test Address',
            city_name='Test City',
            region_name='Test Region',
            zip_code='Test Zip'
        )
        db.session.add(company)
        db.session.commit()

        company = Company.query.filter_by(display_name='Test Company').first()
        self.assertIsNotNone(company)
        self.assertEqual(company.display_name, 'Test Company')
        self.assertEqual(company.address_detail, 'Test Address')
        self.assertEqual(company.city_name, 'Test City')
        self.assertEqual(company.region_name, 'Test Region')
        self.assertEqual(company.zip_code, 'Test Zip')
        
    def test_company_employee_model(self):
        company = Company(
        display_name='Test Company',
        address_detail='Test Address',
        city_name='Test City',
        region_name='Test Region',
        zip_code='Test Zip'
        )
        db.session.add(company)
        db.session.commit()

        employee = CompanyEmployee(
            company_id=company.id,
            employee_id=1,
            fullname='Test Employee',
            email='test@email.com',
            phoneNumber='1234567890'
        )
        db.session.add(employee)
        db.session.commit()

        employee = CompanyEmployee.query.filter_by(fullname='Test Employee').first()
        self.assertIsNotNone(employee)
        self.assertEqual(employee.company_id, company.id)
        self.assertEqual(employee.employee_id, 1)
        self.assertEqual(employee.fullname, 'Test Employee')
        self.assertEqual(employee.email, 'test@email.com')
        self.assertEqual(employee.phoneNumber, '1234567890')
        
    def test_offer_model(self):
        company = Company(
        display_name='Test Company',
        address_detail='Test Address',
        city_name='Test City',
        region_name='Test Region',
        zip_code='Test Zip'
        )
        db.session.add(company)
        db.session.commit()

        offer = Offer(
            company_id=company.id,
            product_1_budget=100,
            product_1_issuing_value=100,
            product_1_mailing_value=100,
            product_1_value=100,
            product_2_budget=100,
            product_2_issuing_value=100,
            product_2_mailing_value=100,
            product_2_value=100,
            product_3_budget=100,
            product_3_issuing_value=100,
            product_3_mailing_value=100,
            product_3_value=100
        )
        db.session.add(offer)
        db.session.commit()

        offer = Offer.query.filter_by(company_id=company.id).first()
        self.assertIsNotNone(offer)
        self.assertEqual(offer.company_id, company.id)
        self.assertEqual(offer.product_1_budget, 100)
        self.assertEqual(offer.product_1_issuing_value, 100)
        self.assertEqual(offer.product_1_mailing_value, 100)
        self.assertEqual(offer.product_1_value, 100)
        self.assertEqual(offer.product_2_budget, 100)
        self.assertEqual(offer.product_2_issuing_value, 100)
        self.assertEqual(offer.product_2_mailing_value, 100)
        self.assertEqual(offer.product_2_value, 100)
        self.assertEqual(offer.product_3_budget, 100)
        self.assertEqual(offer.product_3_issuing_value, 100)
        self.assertEqual(offer.product_3_mailing_value, 100)
        self.assertEqual(offer.product_3_value, 100)