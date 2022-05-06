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
            respone = jsonify(empRows)
            respone.status_code = 200
            return respone
        except Exception as err:
            return err
        finally:
            cursor.close() 
            conn.close()

    def post(user):
        try:
            a = Script.create(user)
            b = a
            print(b)
            # conn = mysql.connect():
            # cursor = conn.cursor(pymysql.cursors.DictCursor)
            # cursor.execute(Script.create(user))
            # conn.commit()
            return True
        except Exception as err:
            return err
        # finally:
        #     cursor.close() 
        #     conn.close()