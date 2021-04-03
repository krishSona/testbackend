import datetime

import base64
import requests
from daily_salary import settings


def get_base_url():
    if settings.ENV == "production":
        base_url = "https://inedgenxt.inedgeretail.com/"
    else:
        # base_url = "http://inedge.heptagon.tech/"
        base_url = "https://inedgenxt.inedgeretail.com/"
    return base_url


def get_arr_for_token(partner_name, applicant_id, date, partner_key):
    return '{"partner_name":"' + partner_name + '","applicant_id":"' +\
           applicant_id + '","date":"' + date + '","partner_key":"' +\
           partner_key + '"}'


def generate_token(applicant_id):
    partner_name = 'DailySalary'
    partner_key = settings.CORE_QUESS_PARTNER_KEY
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    arr = get_arr_for_token(partner_name, applicant_id, date, partner_key)
    token = base64.b64encode(arr.encode('utf-8')).decode()
    return token, partner_key


def get_employee_details(applicant_id):
    base_url = get_base_url()
    token, partner_key = generate_token(applicant_id)
    payload = {
        "token": token,
        "applicant_id": applicant_id,
        "partner_name": "DailySalary",
        "partner_key": partner_key
    }
    try:
        response = requests.post(
            url=base_url + "SubmitLoanDetail", data=payload
        )
        return response.json()
    except Exception as e:
        print(e)
