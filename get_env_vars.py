import os

def get_db_tier():
    return os.getenv("DB_TIER")

def get_db_server():
    return os.getenv("DB_SERVER")

def get_db_user():
    return os.getenv("DB_USER")

def get_db_pass():
    return os.getenv("DB_PASS")
