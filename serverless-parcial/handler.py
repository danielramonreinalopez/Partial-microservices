import json


def hello(event, context):
    body = {
    }
    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def funcion_cinco_atributos(event, context):
    person = {
        "Name": "Ramon",
        "Surname": "Reina",
        "Age": 20,
        "Profession": "Carpenter",
        "Study": "Software Engineering"
    }

    response = {"statusCode": 200, "body": json.dumps(persona)}

    return response

def funcion_diez_atributos(event, context):
    auto = {
        "Brand": "Audi",
        "Model": "R8",
        "Year": 2015,
        "Displacement": 5.2,
        "Color": "White",
        "Engine": "V10",
        "0_to_100_seconds": 3.1,
        "Chassis_Material": "Aluminum",
        "Transmission": "7 speeds",
        "Brakes": "Carbon-Ceramic"
    }

    response = {"statusCode": 200, "body": json.dumps(auto)}

    return response