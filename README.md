# Image Process Project

## Let's to start the project! first make a virtual environment:
### windows:
``` bash
py -m venv venv
```
### linux:
``` bash
python3 -m venv venv
```

## then go back to the repository directory and start the venv:
### windows:
### cmd
``` bash
venv\Scripts\activate.bat
```
#### powershell
``` bash
venv\Scripts\activate.ps1
```
### linux:
``` bash
source venv/bin/activate
```

## install the packages:
``` bash
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

## migrate the database:
``` bash
python manage.py migrate
```

########################## define env variables:
``` bash
cp .env.example .env
```

## run server:
``` bash
python manage.py runserver
```
