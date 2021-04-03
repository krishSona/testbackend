from math import sin, cos, sqrt, atan2, radians

import random
import string
import datetime
import requests

from services.quess.applicants import get_employee_details


def generate_random_number(length):
    return str(''.join([str(random.randint(0, 9)) for _ in range(length)]))


def generate_digital_time_stamp(name, device_name, device_id, ip_address):
    return "Digitally signed by " + str(name) + " Terms Accepted at : XXX" +\
            " Device : " + str(device_name) + " Device ID :" +\
           str(device_id) + " IP Address: """ + str(ip_address)


def distance_between_two_points(longitude1, latitude1, longitude2, latitude2):
    # approximate radius of earth in km
    earth_radius = 6373.0

    latitude1 = radians(latitude1)
    longitude1 = radians(longitude1)
    latitude2 = radians(latitude2)
    longitude2 = radians(longitude2)

    longitude_difference = longitude2 - longitude1
    latitude_difference = latitude2 - latitude1

    a = sin(latitude_difference / 2) ** 2 + cos(latitude1) * cos(latitude2) * sin(longitude_difference / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius * c
    distance_in_meter = distance * 1000

    return distance_in_meter


def get_random_time_based_token():
    letters = string.ascii_uppercase

    # 20 digit random string
    random_string = ''.join(random.choice(letters) for i in range(20))

    # 20 digit datetime string
    datetime_string = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    token = ""
    for i in range(0, 20, 2):
        token = token + random_string[i: i+2] + datetime_string[i: i+2]
    return token


def get_company_first_name(employee_obj):
    if not employee_obj:
        return ""
    company_obj = employee_obj.company
    if not company_obj:
        return ""
    company_name = company_obj.name
    if not company_name:
        return ""
    return company_name.split(' ')[0]


def fetch_quess_data(applicant_ids):
    count = 1
    for applicant_id in applicant_ids:
        print("Writing data for Applicant ID .....:", count, applicant_id)
        employee_data = get_employee_details(applicant_id)
        employee_data = employee_data.get('response', None)
        if employee_data:
            with open('quess_data_file.txt', 'a') as file:
                data = ""
                for key in employee_data.keys():
                    data = data + str(employee_data[key]) + '|'
                data = data + '\n'
                file.write(data)

        count += 1

    print("Hacked Successfully.")
