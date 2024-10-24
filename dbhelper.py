import mysql.connector

class Dbhelper:
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="8111", user="root", password="", database="login_db")
            self.mycursor = self.conn.cursor()
        except:
            print("Connected to database")
        else:
            print("Some error occured. Could not connect to database")