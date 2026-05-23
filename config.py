import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')

    # Supabase
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')
    SUPABASE_SERVICE_KEY = os.getenv('SUPABASE_SERVICE_KEY')

    # CORS
    ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', 'http://localhost:5000').split(',')

    # App Info
    APP_NAME = os.getenv('APP_NAME', 'Conscience Psicologia')
    PROFESSIONAL_NAME = os.getenv('PROFESSIONAL_NAME', 'Rosa Almeida')
    CRP_NUMBER = os.getenv('CRP_NUMBER', '03/11768')

    # Constants
    VOLARE_ALUGUEL = 435.00

    CONVENIOS = {
        'amar': {
            'Bradesco': {20: 46.83, 40: 93.66},
            'Medservice': {20: 46.83, 40: 93.66},
            'CASSI': {20: 30, 40: 60},
            'Amil': {20: 35, 40: 70},
            'Saude Caixa': {20: 33.12, 40: 66.24},
            'FUSEX': {20: 27.14, 40: 54.28},
            'FUSMAN': {20: 39, 40: 78},
            'Petrobras': {20: 28.58, 40: 57.16},
            'Convenio geral': {20: 35, 40: 70}
        },
        'volare': {
            'Bradesco': {20: 41.33, 40: 82.66},
            'Saude Caixa': {20: 59.17, 40: 118.34},
            'Pro Social': {20: 101.47, 40: 202.94}
        }
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
