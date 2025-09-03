from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

#configuração sqlite
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SECRET_KEY = os.getenv('SECRET_KEY')

#teste de conexão

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print('Banco conectado')

#mostrar erro 
except Exception as e:
    print(f'falha ao conectar no banco {e}')

Base = declarative_base()