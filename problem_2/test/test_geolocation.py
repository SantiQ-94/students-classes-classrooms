#! python3
"""
@author : Santiago Quiroga Turdera
@version: 1.0
"""


import unittest
from geolocation import geolocation
#geolocation import geolocation 
#from geolocation.geolocation import StudentFoundList


class TestGeolocation(unittest.TestCase):

    def test_all_students_inside_a_classroom(self):
        engineering_classroom = geolocation.Classroom(name= 'Principles of computational geo-location analysis',
                                             latitude= 34.069140, longitude= -118.442689)
        geology_classroom = geolocation.Classroom(name= 'Sedimentary Petrology', latitude= 34.069585, longitude= -118.441878)
        psychology_classroom = geolocation.Classroom(name= 'Introductory Psychobiology', latitude= 34.069742,
                                             longitude= -118.441312)
        music_classroom = geolocation.Classroom(name= 'Art of Listening', latitude= 34.070223, longitude= -118.440193)
        humanities_classroom = geolocation.Classroom(name= 'Art Hitory', latitude= 34.071528, longitude= -118.441211)

        john_student = geolocation.Student(name= 'John Wilson', latitude= 34.069849, longitude= -118.443539 ) # engineering
        jane_student = geolocation.Student(name= 'Jane Graham', latitude= 34.069901, longitude= -118.441562 ) # geology
        pam_student = geolocation.Student(name= 'Pam Bam', latitude= 34.071523, longitude= -118.441171 ) # humanities

        student_list = [john_student, jane_student, pam_student]
        classroom_list = [geology_classroom, psychology_classroom, music_classroom, humanities_classroom,
                         engineering_classroom]

        result = geolocation.StudentFoundList(student_list, classroom_list)
        self.assertTrue(len(result), 3)

    
    def test_only_one_student_inside_a_classroom(self):

        john_student = geolocation.Student(name= 'John Wilson', latitude= 34.069149, longitude= -118.442639 ) # engineering
        jane_student = geolocation.Student(name= 'Jane Graham', latitude= 34.069601, longitude= -118.441862 ) # geology
        pam_student = geolocation.Student(name= 'Pam Bam', latitude= 34.071513, longitude= -118.441181 ) # humanities

        engineering_classroom = geolocation.Classroom(name= 'Principles of computational geo-location analysis',
                                             latitude= 34.069140, longitude= -118.442689)
        geology_classroom = geolocation.Classroom(name= 'Sedimentary Petrology', latitude= 34.069585, longitude= -118.441878)
        psychology_classroom = geolocation.Classroom(name= 'Introductory Psychobiology', latitude= 34.069742,
                                             longitude= -118.441312)
        music_classroom = geolocation.Classroom(name= 'Art of Listening', latitude= 34.070223, longitude= -118.440193)
        humanities_classroom = geolocation.Classroom(name= 'Art Hitory', latitude= 34.071528, longitude= -118.441211)

        student_list = [john_student, jane_student, pam_student]
        classroom_list = [geology_classroom, psychology_classroom, music_classroom, humanities_classroom,
                         engineering_classroom]

        result = geolocation.StudentFoundList(student_list, classroom_list)
        self.assertTrue(len(result), 1)