from app import app, db
import requests
from app.models import Company, CompanyEmployee, Offer
from app.schemas import CompanySchema, CompanyEmployeeSchema, OfferSchema
from flask import jsonify

# This function is used to get data from the URL
def get_data():
    url = "http://49.12.237.145:5150/"
    headers = {
        "Authorization": "Basic dXNlcjI6Z1JkMnZQVXR6M2ZqYnJ2WQ=="
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    return response.json()

# The main route, getting and saving data in the database
@app.route("/")
def index():
    data = get_data()
    if data is None:
        return jsonify({"message":"Unsuccessful request", "code":401})
    try:
        company, company_employees, offer = data["company"], data["company_employees"], data["offer"]
    except Exception as e:
        return jsonify({"message":"Invalid data : " + str(e), "code":400})
    
    # Save company data
    try:
        company_obj = Company.query.filter_by(display_name=company["display_name"]).first()
        if not company_obj:
            company_obj = Company(**CompanySchema().load(company))
            db.session.add(company_obj)
            db.session.commit()
            app.logger.info('Company saved successfully')
        else:
            app.logger.info('Company already exists')
    except Exception as e:
        db.session.rollback()
        app.logger.error('Company data not saved : ' + str(e))

    # Save company employee data
    try:
        for employee in company_employees:
            employee_obj = CompanyEmployee.query.filter_by(email=employee["email"]).first()
            if not employee_obj:
                employee_obj = CompanyEmployee(**CompanyEmployeeSchema().load(employee), company_id=company_obj.id)
                db.session.add(employee_obj)
                db.session.commit()
                app.logger.info('Employee saved successfully')
            else:
                app.logger.info('Employee already exists')
    except Exception as e:
        db.session.rollback()
        app.logger.error('Employee data not saved : ' + str(e))

    # Save offer data
    try:
        for key in offer:
            if offer[key] == 0:
                offer[key] = None
        offer_obj = Offer(**OfferSchema().load(offer), company_id=company_obj.id)
        db.session.add(offer_obj)
        db.session.commit()
        app.logger.info('Offer saved successfully')
    except Exception as e:
        db.session.rollback()
        app.logger.error('Offer data not saved : ' + str(e))

    return jsonify({"message":"Data saved successfully", "code":200})