# import cx_Oracle
# import traceback
# conn = None
# try:
#     conn = cx_Oracle.connect("mouzikka/music@127.0.0.1/xe")
#     print("Mohit you have Connected successfully to DB")
#     print("Datebase version: ",conn.version)
#     print("DB User: ",conn.username)
# except cx_Oracle.DatabaseError:
#     print("error",traceback.format_exc())
# finally:
#     if conn is not None:
#         conn.close()
#         print("Mohit you have Disconnect successfully")
