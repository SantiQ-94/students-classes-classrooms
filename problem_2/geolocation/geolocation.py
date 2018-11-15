#! /usr/bin python3
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


if __name__ == "__main__":
    engineering_classroom = Classroom(name= 'Principles of computational geo-location analysis', latitude= 34.069140, 
                                        longitude= -118.442689)
    geology_classroom = Classroom(name= 'Sedimentary Petrology', latitude= 34.069585, longitude= -118.441878)
    psychology_classroom = Classroom(name= 'Introductory Psychobiology', latitude= 34.069742, longitude= -118.441312)
    music_classroom = Classroom(name= 'Art of Listening', latitude= 34.070223, longitude= -118.440193)
    humanities_classroom = Classroom(name= 'Art Hitory', latitude= 34.071528, longitude= -118.441211)

    john_student = Student(name= 'John Wilson', latitude= 34.069849, longitude= -118.443539 ) # engineering
    jane_student = Student(name= 'Jane Graham', latitude= 34.069901, longitude= -118.441562 ) # geology
    pam_student = Student(name= 'Pam Bam', latitude= 34.071523, longitude= -118.441171 ) # humanities

    student_list = [john_student, jane_student, pam_student]
    classroom_list = [geology_classroom, psychology_classroom, music_classroom, humanities_classroom,
                         engineering_classroom]
        
    print(StudentFoundList(student_list, classroom_list))

    john_student2 = Student(name= 'John Wilson', latitude= 34.069149, longitude= -118.442639 ) # engineering
    jane_student2 = Student(name= 'Jane Graham', latitude= 34.069601, longitude= -118.441862 ) # geology
    pam_student2 = Student(name= 'Pam Bam', latitude= 34.071513, longitude= -118.441181 ) # humanities

    student_list2 = [john_student2, jane_student2, pam_student2]
    print(StudentFoundList(student_list2, classroom_list))