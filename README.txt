=====
SETUP
=====

Python 2.7.x required. Recommended to be setup in a virtual environment (virtualenv).

Go to weather_dashboard folder.

$ cd weather_dashboard

Install needed requirements.

$ pip install -r requirements/dev.txt

Go to web folder.

$ cd web

Run migrations.

$ python manage.py migrate


=====
USAGE
=====

Run a dev webserver.

$ python manage.py runserver 0.0.0.0:7777

Access interface via: http://127.0.0.1:7777/weather/


====
TODO
====

- add accounts & authentication (OAuth 2), social if needed

- move to separate database instance, setup database backup

- add unit-tests, define test database in test settings

- cached responses (memcached or redis)

- setup CD/CI

- setup CORS & HTTPS (Let's Encrypt)

- split app into API + frontend app

- documented API, API interface (for ex. Swagger)

- robust exception handler with code error specification, custom exceptions...

- add some form of event logging within app; setup logging on web server/WSGI

- store & host static & media files from separate location (for ex. S3)