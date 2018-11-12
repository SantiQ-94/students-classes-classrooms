# Students-Classes-Classrooms

The solutions for the 2 problems are here, on this repository, i will explain each one on this document.

<h3>Problem 1: REST API </h3>

<p>
  For this problem the best fit was to use the <a href="https://www.djangoproject.com/">Django</a> Web framework, this allows to use a clean and simple MVC structure, but also allows us to use the django toolkit called <a href="https://www.django-rest-framework.org/">Django - REST</a>.
</p>

<p>
Django allows us to implement a MVC design pattern efficiently, by defining a model we can focus on how to handle incoming HTTP requests and even have a fully working Database. To increase the RESTfulness of the API, we use the tools offered by Django-REST, that is, how we can implement the navigation logic, query filtering with query params on the URL, listing of the different models.
</p>


<h3>Problem 2</h3>

<p>
 The second problem is more simple; it is possible to find the distance between two coordinates by appliying the following distance formula, extracted from <a href="https://www.movable-type.co.uk/scripts/latlong.html">Movable Type Scrpits page </a>:
                            
                            Haversine
                            formula: 	
                                      a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
                                      c = 2 ⋅ atan2( √a, √(1−a) )
                                      d = R ⋅ c

                            where 	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
                            note that angles need to be in radians to pass to trig functions!
                                          
The implementation of a solution, is quite simple, given that the problem description is very specific on its own; everything that was required for this problem can be found in the <strong>math</strong> library of Python.
</p>
