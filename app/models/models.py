from app import db
from marshmallow import Schema, fields

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(255), unique=True, nullable=False)
    address_detail = db.Column(db.String(255))
    city_name = db.Column(db.String(255))
    region_name = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))
    employees = db.relationship("CompanyEmployee", backref="company", lazy=True)
    offers = db.relationship("Offer", backref="company", lazy=True)


class CompanyEmployee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=False)
    employee_id = db.Column(db.Integer)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phoneNumber = db.Column(db.String(255))


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=False)
    product_1_budget = db.Column(db.Float)
    product_1_issuing_value = db.Column(db.Float)
    product_1_mailing_value = db.Column(db.Float)
    product_1_value = db.Column(db.Float)
    product_2_budget = db.Column(db.Float)
    product_2_issuing_value = db.Column(db.Float)
    product_2_mailing_value = db.Column(db.Float)
    product_2_value = db.Column(db.Float)
    product_3_budget = db.Column(db.Float)
    product_3_issuing_value = db.Column(db.Float)
    product_3_mailing_value = db.Column(db.Float)
    product_3_value = db.Column(db.Float)

class CompanySchema(Schema):
    id = fields.Integer()
    display_name = fields.String()
    address_detail = fields.String()
    city_name = fields.String()
    region_name = fields.String()
    zip_code = fields.String()
    employees = fields.Nested("CompanyEmployeeSchema", many=True)
    Offers = fields.Nested("OfferSchema", many=True)
    
class CompanyEmployeeSchema(Schema):
    id = fields.Integer()
    company_id = fields.Integer()
    employee_id = fields.Integer()
    fullname = fields.String()
    email = fields.String()
    phoneNumber = fields.String()

class OfferSchema(Schema):
    id = fields.Integer()
    company_id = fields.Integer()
    product_1_budget = fields.Float(allow_none=True)
    product_1_issuing_value = fields.Float(allow_none=True)
    product_1_mailing_value = fields.Float(allow_none=True)
    product_1_value = fields.Float(allow_none=True)
    product_2_budget = fields.Float(allow_none=True)
    product_2_issuing_value = fields.Float(allow_none=True)
    product_2_mailing_value = fields.Float(allow_none=True)
    product_2_value = fields.Float(allow_none=True)
    product_3_budget = fields.Float(allow_none=True)
    product_3_issuing_value = fields.Float(allow_none=True)
    product_3_mailing_value = fields.Float(allow_none=True)
    product_3_value = fields.Float(allow_none=True)
