import psycopg2
from pytest import fixture
from dotenv import load_dotenv
import os


#Загрузка переменных окружения из файла .env
load_dotenv()


# Фикстура для подключения к базе данных 
@fixture
def db_cursor():
    conn = psycopg2.connect(
        dbname= os.getenv('DB_NAME'),
        user= os.getenv('DB_USER'),
        password= os.getenv('DB_PASSWORD'),
        host= os.getenv('DB_HOST'),
        port= os.getenv('DB_PORT')
    )

    cursor = conn.cursor()
    
    yield cursor


    conn.commit()
    conn.close()