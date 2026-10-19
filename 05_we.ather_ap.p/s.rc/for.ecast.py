# Tur..ns raw da.ta. into some.thing readable
from src.api import fetch
from src.units import to_celsius


def get_forecast(city):
    # One line of text for ea.c..h da.y
    data = fetch(city)
    return [f"{d['day']}: {to_celsius(d['temp']):.1f} C" for d in data["days"]]
