# convert.py
METER_TO_FEET = 3.281
METER_TO_YARDS = 1.094
YARD_TO_FEET = 3
YARD_TO_METER = 0.9144
FEET_TO_METER = 0.3048
FEET_TO_YARD = 0.3333

def meters_to_feet(value):
    return value * METER_TO_FEET

def meters_to_yards(value):
    return value * METER_TO_YARDS

def yards_to_feet(value):
    return value * YARD_TO_FEET

def yards_to_meters(value):
    return value * YARD_TO_METER

def feet_to_meters(value):
    return value * FEET_TO_METER

def feet_to_yards(value):
    return value * FEET_TO_YARD
