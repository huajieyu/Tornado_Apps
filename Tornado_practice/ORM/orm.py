import tornado.web
from ORM.liboMysql import liboMySQL

class ORM(tornado.web.RequestHandler):
    def __init__(self, site):
        self.site = site 
    def DB_connection(self, selsite):
        #1 get_environment 

        profiles = {
            'LAB': 'dnm6svr',
            'SD1': 'dnm6svr',
            'SD2': 'dnm6svr',
            'MCC': 'dnm5svr',
            'LSOC': 'dnm2svr',
            'ESOC': 'dnm1svr',
        }
        sid = 'nx61'
        user = "netexpt"
        prime=os.getenv('GNS_PROFILE')
        box=profiles[prime]
        
        password_prime = subprocess.check_output(['ssh', 'netexpt@{}'.format(box),
                                        'grep', 'OSI_DB_PASSWORD',
                                        '/opt/gns/GNS_dnm/share/profiles/{}/dnm/profile.env'.format(prime)])
         
        password_prime = password_prime.decode().split('=')[1].rstrip().strip("'").strip('"')
        print("***[ORM] password prime is ", password_prime)
        # extract the password from the password_prime string
        
        conn = cx_Oracle.connect(user, password_prime, sid)
        cur = conn.cursor()

        cur.execute("SELECT moname, attribute, compname " \
             "FROM composite " \
             "WHERE attribute LIKE 'DNM_Sat%Antenna'")
        res = cur.fetchall()
        # loop over all the content in the table and print out on the screen
        # get all the subnet information in selsite
        idx=0
        for row in res:
            # print(row)
            # check the data type of row : tuple
            # print("***[ORM] the data type of the rows gotten from data base is ", type(row))
            # get the length of each tuple though the len function
            tempidx = idx
            temprow = row 
            tlen = len(row)
            # loop over all the items in the tuple
            if tempidx < 3:
                tempkey=str(selsite)+'_'+str(tempidx)
                genvarDict[tempkey]=temprow[1]
                genparDict[tempkey]=temprow[1]

            idx = idx + 1
        cur.close()
        conn.close()


    def save(self):
        # insert students (name, age) values ('Tracy', 8)
        #           ??1     ??2  ??3           ??4    ??5
        # homework
        '''
        self.__class__.__name__ : get the current class and class name
        same as the table name
        convert into lower case
        fieldsStr(??2 and ??3) -> keys
        valuesStr(??4 and ??5) -> values
        '''
        tableName = (self.__class__.__name__).lower()
        fieldsStr= valuesStr="("
        for field in self.__dict__:
            fieldsStr += (field + ",")
            if isinstance(self.__dict__[field], str):
                valuesStr += ("'"+self.__dict__[field] + ",")
        fieldsStr = fieldsStr[:len(fieldsStr)-1] + ")"
        valuesStr = valuesStr[:len(valuesStr)-1] + ")"
        sql = "insert into " + tableName + " " + fieldsStr + " values " + valuesStr

        db = liboMySQL()
        db2 = liboMySQL()
        # means it is a single instance class
        print('check if db is  db2 ', db is db2)

        db.insert(sql)

        self.Application.db.insert(sql)

        pass

    def delete(self):
        pass

    def update(self):
        pass

    
    @classmethod
    def all(self):
        # select * from students
        tableName = (cls.__name__).lower()
        sql = "select * from " + tableName
        db = liboMySQL()
        print("sql statement is " , sql)
            
        return db.get_all_obj(sql, tableName)
    
    @classmethod
    def filter(self):
        pass
