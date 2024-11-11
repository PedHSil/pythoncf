#PyMysql pip install PyMySQL
# pip install types-pymysql
# pip install python-dotenv

import os
import pymysql
import dotenv

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABAS']
)

with connection:
    with connection.cursor() as cursor:
        #SQL
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
        #cuidado, isso limpa a tabela !!!!!!!!!!!!!
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
        
    #manipulação de dados a partir daqui
    with connection.cursor() as cursor:
        result = cursor.execute(  # type: ignore
            f'INSERT INTO {TABLE_NAME}'
            '(nome, idade) VALUES (%s, %s)'
        )
        data = ('Pedro', 19)
        result = cursor.execute(sql, data)
        print(result)
    connection.commit()