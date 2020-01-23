## user_login_system_in_django

### Clone this repository
`git clone https://github.com/joyonto51/user_login_system_in_django.git`

### Install python3.6 first
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
### Install virtual environment

`sudo apt install virtualenv`

### Create virtual environment

`virtualenv venv --python=python3.6`

### Activate virtual environment

`source venv/bin/activate`

### Go to project directory

`cd basic_auth`

### Install requirements

`pip install -r requirements.txt`

### Migrate
`python manage.py migrate`

### Create superuser and login with the credential

`python manage.py createsuperuser`
