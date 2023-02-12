from app import app, db
import requests
from app.models import Company, CompanyEmployee, Offer
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
            company_obj = Company(display_name=company["display_name"], address_detail=company["address_detail"], city_name=company["city_name"], region_name=company["region_name"], zip_code=company["zip_code"])
            db.session.add(company_obj)
            db.session.commit()
            app.logger.info('Company saved successfully')
        else:
            app.logger.info('Company already exists')
    except Exception as e:
        db.rollback()
        app.logger.error('Company data not saved : ' + str(e))

    # Save company employee data
    try:
        for employee in company_employees:
            employee_obj = CompanyEmployee.query.filter_by(email=employee["email"]).first()
            if not employee_obj:
                employee_obj = CompanyEmployee(company_id=company_obj.id, employee_id=employee["employee_id"], fullname=employee["fullname"], email=employee["email"], phoneNumber=employee["phoneNumber"])
                db.session.add(employee_obj)
                db.session.commit()
                app.logger.info('Employee saved successfully')
            else:
                app.logger.info('Employee already exists')
    except Exception as e:
        db.rollback()
        app.logger.error('Employee data not saved : ' + str(e))

    # # Save offer data
    try:
        for key in offer:
            if offer[key] == 0:
                offer[key] = None
        offer_obj = Offer(company_id=company_obj.id, product_1_budget=offer["product_1_budget"], product_1_issuing_value=offer["product_1_issuing_value"], product_1_mailing_value=offer["product_1_mailing_value"], product_1_value=offer["product_1_value"], product_2_budget=offer["product_2_budget"], product_2_issuing_value=offer["product_2_issuing_value"], product_2_mailing_value=offer["product_2_mailing_value"], product_2_value=offer["product_2_value"], product_3_budget=offer["product_3_budget"], product_3_issuing_value=offer["product_3_issuing_value"], product_3_mailing_value=offer["product_3_mailing_value"], product_3_value=offer["product_3_value"])
        db.session.add(offer_obj)
        db.session.commit()
        app.logger.info('Offer saved successfully')
    except Exception as e:
        db.rollback()
        app.logger.error('Offer data not saved : ' + str(e))

    return jsonify({"message":"Data saved successfully", "code":200})