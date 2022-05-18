# nuvola
 
Swagger Api documentation is in `api/v1/docs`


- create a virtual environment and install the packages using ```pip install -r requirements.txt```
- Run ```python manage.py makemigrations```
- Run ```python manage.py migrate``` 
- Run ```python manage.py runserver``` to start the server. 

#### Endpoints
- ```api/v1/flights``` List of flights.


-  ```api/v1/flights/<int:flight_number>/``` Update Flight.
-  ```api/v1/create/``` Create Flight. 
-  ```api/v1/delete/<str:flight_number>/``` Delete Flight.

#### Tests

Run ```python manage.py test``` for tests
