#! /usr/bin python3
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


def distance(xA, yA, xB, yB):
    return math.sqrt(((xB - xA)**2) + ((yB - yA)**2))

def StudentFoundList(StudentList=[], ClassroomList=[]):
    return_set = []

    for student in StudentList:
        for classroom in ClassroomList:
            distance_to_classroom = int(distance(student.latitude, student.longitude, classroom.latitude, classroom.longitude))
            if distance_to_classroom <= 20:
                return_set.append({'latitude': student.latitude, 'name': student.name, 'longitude': student.longitude})
                break

    return return_set


if __name__ == "__main__":
   
    engineering_classroom = Classroom(name= 'Principles of computational geo-location analysis', latitude=34.069140, 
        longitude=-118.442689 )
    geology_classroom = Classroom(name='Sedimentary Petrology', latitude=34.069585, longitude=-118.441878)
    psychology_classroom = Classroom(name='Introductory Psychobiology', latitude=34.069742, longitude=-118.441312)
    music_classroom = Classroom(name='Art of Listening', latitude=34.070223, longitude=-118.440193)
    humanities_classroom = Classroom(name='Art Hitory', latitude=34.071528, longitude=-118.441211)

    john_student = Student(name='John Wilson', latitude= 34.069149, longitude=-118.442639 ) # engineering
    jane_student = Student(name='Jane Graham', latitude= 34.069601, longitude=-118.441862 ) # geology
    pam_student = Student(name='Pam Bam', latitude=34.071513, longitude=-118.441181 ) # humanities

    student_list = [john_student,jane_student,pam_student]
    classroom_list = [geology_classroom,psychology_classroom,music_classroom,humanities_classroom,engineering_classroom]
    
    print(StudentFoundList(student_list, classroom_list))