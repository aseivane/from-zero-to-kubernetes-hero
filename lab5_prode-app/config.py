import os
import redis
from dotenv import load_dotenv

# API VARS IN ENV
env_dir = os.path.abspath(os.path.dirname(__file__))

class Config():

    load_dotenv(os.path.join(env_dir, '.env_docker'))

    FLASK_ENV= os.environ.get('FLASK_ENV')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # pagination var
    ROWS_PER_PAGE = 10

    # postgres + orm config
    PSQL_PASS = os.environ.get('PSQL_PASS')
    PSQL_USER = os.environ.get('PSQL_USER')
    PSQL_DB_NAME = os.environ.get('PSQL_DB_NAME')
    PSQL_HOST_DB = os.environ.get('PSQL_HOST_DB')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST_DB}:5432/{PSQL_DB_NAME}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis config
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_TYPE = 'redis'

    REDIS_HOST = os.environ.get('REDIS_HOST')

    SESSION_REDIS = redis.Redis(
        host=REDIS_HOST, 
        port=6379, 
        db=0, 
    )

    # mail server config
    ADM_MAIL = os.environ.get('ADM_MAIL')
    ADM_PASS = os.environ.get('ADM_PASS')

