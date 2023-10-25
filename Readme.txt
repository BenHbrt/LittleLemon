API Endpoints:

MENU ITEMS (GET, POST):
http://127.0.0.1:8000/restaurant/menu/

SINGLE MENU ITEM (GET, PUT, PATCH, DELETE):
http://127.0.0.1:8000/restaurant/menu/<id>

TABLE BOOKINGS (GET, POST):
http://127.0.0.1:8000/restaurant/booking/tables/

SINGLE TABLE BOOKING (GET, PUT, DELETE):
http://127.0.0.1:8000/restaurant/booking/tables/<id>/

SET UP NEW USER (provide username and password):
http://127.0.0.1:8000/auth/users/

GET USER TOKEN (provide username and password):
http://127.0.0.1:8000/auth/token/login/

LOGOUT USER (POST)
http://127.0.0.1:8000/auth/token/logout/