import pymysql
import json
from ErrorCodes import codes
from passlib.hash import pbkdf2_sha1

class mysqlDB:

    def __init__(self, host, user, password, db):
        self.db = pymysql.connect(host,user, password, db)
        self.cur = self.db.cursor()

    def login(self, data):
        query = "INSERT INTO {} VALUES('{}', '{}', '{}', {})".format("users", "sofi", "basit@gmail.com", "mypass", 132465)
        print(query)
        print(str(self.db))
        print(str(self.cur))
        self.cur.execute(query)
        self.db.commit()

    def register(self, data):
        print(data)
        if 'username' in data and 'email' in data and 'password' in data and 'phone' in data:
            try:
                query = "INSERT INTO {} VALUES('{}', '{}', '{}', {})".format("users", data['username'],
                                                                         data['email'], data['password'],
                                                                         data['phone'])
                self.cur.execute(query)
                self.db.commit()
                return json.dumps({"status": "success", "message": {"username": data['username']}})
            except pymysql.err.IntegrityError:
                return codes.userExists()
            except:
                return codes.invalidEntries()
        else:
            return codes.badRequest()

            # try:
            """select = "SELECT * FROM USERS IF username='{}'".format(data['username'])
            sel = self.cur.execute(select)

            if sel == 0:"""
            #pymysql.err.IntegrityError
            """else:
                return codes.userExists()"""
            # except:
            #   return codes.invalidEntries()

