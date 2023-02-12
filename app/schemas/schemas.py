from marshmallow import Schema, fields

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