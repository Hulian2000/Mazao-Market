import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True
    RAPID_API_HOST = os.environ.get('RAPID_API_HOST')
    RAPID_API_KEY = os.environ.get('RAPID_API_KEY')
    RAPID_API_URL = os.environ.get('RAPID_API_URL')
    API_KEY = os.environ.get('API_KEY')
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    DEFAULT_SENDGRID_SENDER = os.environ.get('DEFAULT_SENDGRID_SENDER')
