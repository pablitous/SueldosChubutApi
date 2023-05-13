# What is it?
It´s an API to get the salaries from my State as a dataset in JSON format.
Every data you can get from here is public.

# Install
- git clone github.com/pablitous/SueldosChubutApi
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate

  
# Run
python manage.py runserver 0.0.0.0:8000


# Endpoints
http://127.0.0.1:8000/api/
http://127.0.0.1:8000/api/organisms/
http://127.0.0.1:8000/api/salary/?name=&dni=&organism=6218&page=1

