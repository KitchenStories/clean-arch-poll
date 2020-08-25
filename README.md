# Poll - Clean architecture implemented in python

# Development

## run fastAPI
```
export PYTHONPATH=$PWD/src 

uvicorn --app-dir=src/infrastructure/web/fastapi main:app
```

## run flask
```
export PYTHONPATH=$PWD/src 
export FLASK_APP=infrastructure.web.flask.main 

flask run
```

## run django
```
export PYTHONPATH=$PWD/src

python src/infrastructure/web/dj/manage.py runserver 0.0.0.0:8000
```

## run console
```
export PYTHONPATH=$PWD/src

python src/infrastructure/console/poll.py
```

## run test 
```
export PYTHONPATH=$PWD/src 

pytest -vvs --cov=src src  
```