from flask import jsonify
import pymysql
from src.database.config import mysql
from src.repository.scripts.Usuario import Script


class UsuarioRepository:
    def getAll():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(Script.getAll())
            empRows = cursor.fetchall()
            response = jsonify(empRows)
            response.status_code = 200
            return empRows
        except Exception as err:
            return err
        finally:
            cursor.close() 
            conn.close()

    def post(user):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(Script.create(user))
            conn.commit()
            print(user)
            return user
        except Exception as err:
            print(err)
            return err
        # finally:
        #     cursor.close() 
        #     conn.close()