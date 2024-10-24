import mysql.connector
import sys

class Dbhelper:
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="login_db")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occured. Could not connect to database")
            sys.exit(0)
        else:
            print("Connected to database")
            
    def register(self, name, email, password):
        try:
            self.mycursor.execute(""" 
            INSERT INTO `users` (`id`, `name`, `email`, `pssword`) VALUES (NULL, '{}', '{}', '{}');""".format(name, email, password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        
        
    def search(self, email, password):
        self.mycursor.execute("""
            SELECT  * FROM users WHERE email LIKE '{}' AND PASSWORD LIKE '{}' """.format(email, password))
        data = self.mycursor.fetchall()
        print(data)
            