# import pymysql
import cx_Oracle
import os
from configs.config import MyConfig
import subprocess
def singleton(cls, *args, **kwargs):
    instances ={}
    def _singleton():
        if cls not in instances:
            instance[cls] =cls(*args, **kwargs)
        # return to a single class object
        return instances[cls]

    return _singleton

# single instance class
# MySQL only create one object to make sure only one object
# @singleton
class liboMySQL():
    def __init__(self, host, username, passwd, dbName):
        print("***[ORM/liboMySQL initiate function***")
        self.host =  host
        self.user = username
        self.passwd = passwd
        self.dbName = dbName

    #def __new__(cls, *args, **kwargs):
    #    pass
    def connect(self, *args, **kwargs):
        print("***[ORM/liboMySQL] trying to connect to database")
        # self.db = cx_Oracle.connect('tiger/scott@localhost:1521/xe')
        # self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName, cursorclass=pymysql.cursor.DictCursor)
        profiles = MyConfig.get_profiles()
        sid = 'nx61'
        print("***[ORM/liboMySQL] sid is ", sid)
        user = "netexpt"
        print("***[ORM/liboMySQL] user is ", user)
        prime=os.getenv('GNS_PROFILE')
        print("***[ORM/liboMySQL] prime is ", prime)
        box=profiles[prime]
        print("***[ORM/liboMySQL] prime and box are : ", prime, "   ", box)         
        password_prime = subprocess.check_output(['ssh', 'netexpt@{}'.format(box),
                                        'grep', 'OSI_DB_PASSWORD',
                                        '/opt/gns/GNS_dnm/share/profiles/{}/dnm/profile.env'.format(prime)])
        print("***[ORM/liboMySQL] subprocess output is ", password_prime)
 
        password_prime = password_prime.decode().split('=')[1].rstrip().strip("'").strip('"')
        print("***[ORM/liboMySQL] password prime is ", password_prime)
        # extract the password from the password_prime string
        self.conn = cx_Oracle.connect(user, password_prime, sid)
        print("***[ORM/liboMySQL] connected to oracle database ")
        self.cursor = self.conn.cursor
        print("***[ORM/liboMySQL] got self.conn and self.cursor ")
  
    def close(self):
        self.cursor.close()
        self.db.close()
    def get_one(self, sql):
        res = None
        try:
            self.connect()
            res = self.cursor.fetchone()
            self.close

        except:
            print("connection to database failed")

        return res

    def get_all(self, *args, **kwargs):
        print ("***[liboMySql]/get_all function starts!") 
        res = []
        try:
            self.connect()
            print("***[liboMySql] building the sql for execution ", self.cursor)    
            

            self.cursor.execute("SELECT moname, attribute, compname " \
                 "FROM composite " \
                 "WHERE attribute LIKE 'DNM_Sat%Antenna'")
            res = self.cursor.fetchall()
            print("***[liboMySql] feches all objects in get_all ", res)
            self.close

        except:
            print("connection to database failed in get_all")

        return res

    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        if (len(args)>0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldsSql = "select COLUMN_NAME from information_schema.COLUMNS where tableName = '%s' and table_schema is '%s'" % ( 
            tableName, self.dbName)
            fields = self.get_all(fieldSql)
            for item in fields:
                fieldsList.append(item[0])
        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
        return resList        

    def insert(self, sql):
        return self.__edit(sql)
    def update(self, sql):
        return self.__edit(sql)
    def delete(self, sql):
        return self.__edit(sql)
    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("Submition failed")
        return count
        return self.__edit(sql)

