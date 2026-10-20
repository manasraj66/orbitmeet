import os
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-only-change-me')
TURN_URL = os.getenv('TURN_URL', '')
TURN_USERNAME = os.getenv('TURN_USERNAME', '')
TURN_CREDENTIAL = os.getenv('TURN_CREDENTIAL', '')
