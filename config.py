import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'JexsJHawr1qEzNXD7B1Vv1m2VbGzsmM7r1Yji0Le8Yw'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://king_db:pass_db@localhost/login_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'NjpjyR8EqD0z8Ra6DTEIp1g3Be9BVVofjiZi-DhiIEM'