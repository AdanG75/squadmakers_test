# Squadmakers test

Test to apply to a squadmakers's job

## APP's direction

The application can be visited in the next URL:

    https://polar-tundra-92156.herokuapp.com/docs/

## To run locally

    python -m venv venv
    source .venv/bin/activate
    pip install -r requirements.txt

After, create a file .env with the next structure:
    
    POSTGRES_USER=Your_user
    POSTGRES_PASSWORD=Your_password
    POSTGRES_SERVER=Your_server
    POSTGRES_PORT=Your_port
    POSTGRES_DB=Your_db

I have used PostgreSQL to save all data, so you need to execute the content of file **'db_schema.sql'** in PostgerSQL to have 
the structure that it is uses by the app. 

Finally, run via uvicorn:

    uvicorn main:app --reload


## To run the tests

Execute the next command in your terminal at root directory:

    pytest -v

**Note:** Set ID_JOKE_TO_TEST = 1 (test_joke_router.py) if not values have been saved into DB
and you want to run the tests.