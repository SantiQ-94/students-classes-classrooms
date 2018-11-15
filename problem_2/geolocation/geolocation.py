#! python3
"""
@author  : Santiago Quiroga Turdera
@version : 1.0
"""


import math


class Student:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    

class Classroom:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


def calculate_distance(latitude_a, longitude_a, latitude_b, longitude_b):
    EARTH_RADIUS = 6371000

    delta_latitude = math.radians(latitude_b - latitude_a)
    delta_longitude = math.radians(longitude_b - longitude_a)
    latitude_a_in_radians = math.radians(latitude_a)
    latitude_b_in_radians = math.radians(latitude_b)

    """
    'a' and 'c' variable names are strongly related to the mathematical definition of the Haversine Formula,
    for clarity they will be used in the same fashion as in a more mathematical context.
    """

    a = ((math.sin(delta_latitude / 2) * math.sin(delta_latitude / 2)) + 
            (math.sin(delta_longitude / 2) * math.sin(delta_longitude / 2) * math.cos(latitude_a_in_radians) 
            * math.cos(latitude_b_in_radians)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = EARTH_RADIUS * c
    return distance


def StudentFoundList(StudentList=[], ClassroomList=[]):
    return_set = []
    for student in StudentList:
        for classroom in ClassroomList:
            distance_to_classroom = calculate_distance(student.latitude, student.longitude, classroom.latitude,
                                        classroom.longitude)
            if distance_to_classroom <= 20:
                return_set.append({'latitude': student.latitude, 'name': student.name, 
                                    'longitude': student.longitude})
                break
    return return_set

