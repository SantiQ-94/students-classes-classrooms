@author  : Santiago Quiroga Turdera
@version : 1.0


Description
===========
This problem consists on finding out if any **Student** from a collection of students, 
is located within a **Classroom** geographical space.

Every *Student* has a name and a locations described as coordinates, the same applies to every
*Classroom*.

Assumptions
-----------

- To calculate the distance between to pair of coordinates we will use the **Haversine Formula**, the returned value
will be the distance between two points in *meters*.
- The value for the value of the radius of the earth will be 6371000 meters.
- To consider a Student to be inside a Classroom, the distance between both should be equal or less than 20 meters
(it's fair to say that we are assuming that the classrooms are circular rather than rectangular shaped).


Requirements
============
This python project uses
    
    -python 3.6.6


Installation
============
This project requires no further actions to work.


Testing
=======
