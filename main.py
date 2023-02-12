import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://up_hellas:up_hellas@localhost:5432/project_up'
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app

app = create_app()

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


def get_data():
    url = "http://49.12.237.145:5150/"
    headers = {
        "Authorization": "Basic dXNlcjI6Z1JkMnZQVXR6M2ZqYnJ2WQ=="
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    return response.json()

@app.route("/")
def index():
    data = get_data()
    if data is None:
        return "Unsuccessful request", 401

    company, company_employees, offer = data["company"], data["company_employees"], data["offer"]

    # Save company data
    company_obj = Company.query.filter_by(display_name=company["display_name"]).first()
    if not company_obj:
        company_obj = Company(display_name=company["display_name"], address_detail=company["address_detail"], city_name=company["city_name"], region_name=company["region_name"], zip_code=company["zip_code"])
        db.session.add(company_obj)
        db.session.commit()
        print('Company saved successfully')
    else:
        print('Company already exists')

    # Save company employee data
    for employee in company_employees:
        employee_obj = CompanyEmployee.query.filter_by(email=employee["email"]).first()
        if not employee_obj:
            employee_obj = CompanyEmployee(company_id=company_obj.id, employee_id=employee["employee_id"], fullname=employee["fullname"], email=employee["email"], phoneNumber=employee["phoneNumber"])
            db.session.add(employee_obj)
            db.session.commit()
            print('Employee saved successfully')
        else:
            print('Employee already exists')

    # # Save offer data
    for key in offer:
        if offer[key] == 0:
            offer[key] = None
    offer_obj = Offer(company_id=company_obj.id, product_1_budget=offer["product_1_budget"], product_1_issuing_value=offer["product_1_issuing_value"], product_1_mailing_value=offer["product_1_mailing_value"], product_1_value=offer["product_1_value"], product_2_budget=offer["product_2_budget"], product_2_issuing_value=offer["product_2_issuing_value"], product_2_mailing_value=offer["product_2_mailing_value"], product_2_value=offer["product_2_value"], product_3_budget=offer["product_3_budget"], product_3_issuing_value=offer["product_3_issuing_value"], product_3_mailing_value=offer["product_3_mailing_value"], product_3_value=offer["product_3_value"])
    db.session.add(offer_obj)
    db.session.commit()
    print('Offer saved successfully')

    #db.session.commit()

    return "Data saved successfully", 200

if __name__ == "__main__":
    app.run(port=9500, debug=True)

with app.app_context():
    db.create_all()