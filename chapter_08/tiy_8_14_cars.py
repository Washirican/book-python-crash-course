# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-05-07
# --------------------------------------------------------------------------- #


def make_car(manufacturer, model_name, **car_data):
    """Receives keyword arguments for a car"""
    car_data['manufacturer'] = manufacturer
    car_data['model_name'] = model_name

    return car_data


my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
                         headlights='popup')
print(my_old_accord)
