import json
# import pickle
import numpy as np
# import geopy.distance
from flask import Flask, request

# def distance_coords(coords_1, coords_2):
#     """
#     Get the distance between two coordinates
#     """
#     return geopy.distance.vincenty(coords_1, coords_2).miles

app = Flask(__name__)
@app.route("/", methods=['POST'])
def address():
    '''
    Takes a list of json dictionaries and return calculated CO2E emissions
    '''

    # receive input
    inputs = request.get_json(force=True)

    # get data from json
    # coords_1 = inputs['coords_1']
    # coords_2 = inputs['coords_2']
    car_distance_km = inputs['car_distance']
    car_distance_miles = car_distance_km * 0.621
    # bus_distance_miles = inputs['bus_distance']
    # train_distance_miles = inputs['train_distance']
    # if inputs['passengers'] < 1:
    #     passengers = 1
    # else:
    # passengers = inputs['passengers']
    # if inputs['mpg'] > 0:
    #     car_mpg = inputs['mpg']
    # else:
    avg_car_mpg = 22.0

    # car, bus, rail

    # flight distance in miles
    # flight_distance_miles = distance_coords(coords_1, coords_2)

    # Emission rate
    co2e_lbs_per_gas_gal = 19.830
    co2e_lbs_per_diesel_gal = 22.716
    # bus_co2_lbs_per_passenger_mile = .17 / .988  # CO2 equivalents conversion
    # train_co2e_lbs_per_passenger_mile = .31
    # flight_co2e_lbs_per_passenger_mile = .39

    """
    Radiative Forcing:
    Aircraft are thought to have greater climate effects than just the CO2 emissions from burning the fuel.
    The additional effects include contributions from nitrous oxides and ozone.
    Because of this, the CO2 emissions from aviation should be increased by an appropriate factor.
    """
    # rf_factor = 2

    # CO2E Emission
    car_gas_co2e_emission_per_vehicle = car_distance_miles * \
        co2e_lbs_per_gas_gal / avg_car_mpg
    car_diesel_co2e_emission_per_vehicle = car_distance_miles * \
        co2e_lbs_per_diesel_gal / avg_car_mpg
    # bus_emission_per_passenger = bus_co2_lbs_per_passenger_mile * bus_distance_miles
    # train_emission_per_passenger = train_co2e_lbs_per_passenger_mile * train_distance_miles
    # flight_emission_per_passenger = flight_co2e_lbs_per_passenger_mile * flight_distance_miles * rf_factor

    # Use a dictionary to format output for json
    out = {'Pounds of CO2E emission per car on gasoline (22 mpg)': car_gas_co2e_emission_per_vehicle,
           'Pounds of CO2E emission per car on diesel (22 mpg)': car_diesel_co2e_emission_per_vehicle} #,
        #    'Pounds of CO2E emission per passenger on bus': bus_emission_per_passenger,
        #    'Pounds of CO2E emission per passenger on train': train_emission_per_passenger}

    # give output to sender.
    return app.response_class(
        response=json.dumps(out),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True)
