# Poll - Clean archtitecture implemented in python

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

## run test 
```
export PYTHONPATH=$PWD/src 

pytest -vvs --cov=src src  
```