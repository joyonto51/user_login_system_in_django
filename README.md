## user_login_system_in_django

### Clone this repository
`git clone https://github.com/joyonto51/user_login_system_in_django.git`

### go to project directory

`cd basic_auth`

### install python3.6 first
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```
### Install dependensis
```
sudo apt-get install python3-dev
sudo apt-get install libffi6 libffi-dev
```

### install virtualenv

`sudo apt install virtualenv`

### create virtual venv

`virtualenv venv --python=python3.6`

### activate virtual environment

`source venv/bin/activate`

### install requirements

`pip install -r requirements.txt`

### migrate
`python manage.py migrate`

### create superuser
`python manage.py createsuperuser`
