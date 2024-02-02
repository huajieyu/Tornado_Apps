import tornado
import tornado.web
import tornado.gen
import json
import os
import time
# import asyncio
from configs.config import MyConfig
from views.models import Students
from ORM.liboMysql import liboMySQL
from tornado.httpclient import AsyncHTTPClient
from typing import AsyncIterator, Mapping, Tuple
# from tornado.web import asynchronous
from tornado.websocket import WebSocketHandler 

class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print("set_default_headers")
        pass
    def initialize(self):
        print("initialize")
        pass
    def prepare(self):
        print("prepare")
        pass
    def get(self, *args, **kwargs):
        # self.write("good test")
        print("HTTP get method")
        self.send_error(500)

        self.write("<a href='/json'> Go to Another Page</a>")
    def write_error(self):
        print("write_error")
        pass
    def on_finish(self):
        print("on_finish")
        pass
   

class RedirectHandler(tornado.web.RequestHandler):
    def initialize(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        print (self.key1, self.key2)
 
    def get(self, *args, **kwargs):
        self.redirect("/json")

class TestHandler(tornado.web.RequestHandler):
    def initialize(self, key3, key4):
        self.key3 = key3
        self.key4 = key4
        print (self.key3, self.key4)

    def get(self, *args, **kwargs):
        self.write("good test")
        url=self.reverse_url("index")
        self.write("<a href='/json'> Go to Another Page</a>")

class SecTestHandler(tornado.web.RequestHandler):
    def get(self, par1, par2, par3, *args, **kwargs):
        print(par1 + "-" + par2 + "-" + par3)
        self.write("Second Test for SecTestHandler")

class ThiTestHandler(tornado.web.RequestHandler):
    def get(self,  *args, **kwargs):
        # self.get_query_argument(name, default=ARG_DEFAULT, strip=True)
        # self.get_query_argument(name, default=ARG_DEFAULT, strip=True)
        a = self.get_query_argument("a", strip=False)
        b = self.get_query_argument("b", strip=False)
        c = self.get_query_argument("c", strip=False)


        print ("a= ", a, " b= ", b, " c= ", c)
   
        self.write("Third Test for ThiTestHandler")
class FouTestHandler(tornado.web.RequestHandler):
    def get(self,  *args, **kwargs):
        # self.get_query_argument(name, default=ARG_DEFAULT, strip=True)
        # self.get_query_arguments(name, strip=True)
        alist = self.get_query_arguments("a")

        print ("alist[0]= ", alist[0], " alist[1]= ", alist[1], " alist[2]= ", alist[2])
   
        self.write("Fourd Test for FouTestHandler")
'''
class PostFileHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('sitectlreact/postfile.html')

    def post(self, *args, **kwargs):
        # self.get_body_argument(name, default=ARG_DEFAULT, strip=True)
        # self.get_query_arguments(name, strip=True)
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        hobbyList = self.get_body_arguments("hobby")
        print(username, password, hobbyList)
        self.write("PostFileTest ")
'''
# uploaded file proerties
# filename: uploaded file name got from server
# body:
# content type: image or other type, check before upload
# 
class UpFileHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('sitectlreact/upfile.html')

    def post(self, *args, **kwargs):
        # save the uploaded file
        # tornado.httputil.HTTPFile
        # request.files is a dictionary type
        filesDict = self.request.files
        for inputname in filesDict:
            fileArr = filesDict[inputname]
            for fileObj in fileArr:
                # store path
                mysettings = MyConfig.get_settings()
                basepath = mysettings['base_path'] 
                
                filePath = os.path.join(basepath, "uploaded_files/" + fileObj.filename); 
                print("file path is ", filePath)
                with open(filePath, "wb") as f:
                    f.write(fileObj.body)



        #file1 = self.request.files['files'][0]
        #original_fname = file1['filename']
        # set up location of the uploaded file will be saved
        #output_file=open("uploaded_files/" + original_fname, "wb")
        #output_file.write(file1['body'])
        # self.finish("file " + original_fname + " is uploaded ")
        pass

 
# get_arguments can be used in post or get methods
# Request object stores all the information of the requests
# HTTP request methods: get, post
# host: host name of the server
# url: address of the request, including the path and query parameters
# path: path of the request
# query: request parameters
# version: HTTP version
# headers: headers of the request protocals (type: dictionary)
# body:
# remote ip: client IP address
# files: uploaded file by client (type = dictionary)



class ZhuyinHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("request object is ", self.request.method)
        print("request host is ", self.request.host)
        print("request uri is ", self.request.uri)
        print("request path is ", self.request.path)
        print("request query is ", self.request.query)
        print("request version is ", self.request.version)
        print("request headers is ", self.request.headers)
        print("request body is ", self.request.body)
        print("request remote ip  is ", self.request.remote_ip)
        print("request files is ", self.request.files)
        self.write("Zhuyin Handler test")               

class WriteHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("abc is a good man")
        self.write("abc is a nice man")
        self.write("abc is a handsome man")
        # write method to write json data
        # update the buffer
        self.finish()
        
        # self.write("abc is a cool man") !!!!not work, can not write anything under finish
 
        pass
 

class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name": "libo",
            "age": 40
        }
        perhtml = {
            "name": "libo",
            "age": 40
        }
        stus = [
            {
                "name": "Tom",
                "age": 5
            },
            {
                "name": "Jerry",
                "age": 6
            }
        ]



        print ("***[HomeHandler] pre dictionary name is ", per["name"])

        # self.render("sitectlreact/index.html", num=temp, per=per)
        # **per is equivalent to name=per["name", and age=per["age"]
        # in case there is any name conflicts, usually, we do not use **per to pass the parameters
        flag = 0
        self.render("sitectlreact/index.html", num=temp, perhtml=perhtml, **per, flag=flag, stus = stus)


class FunctionHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name": "libo",
            "age": 40
        }
        perhtml = {
            "name": "libo",
            "age": 40
        }
        stus = [
            {
                "name": "Tom",
                "age": 5
            },
            {
                "name": "Jerry",
                "age": 6
            }
        ]
        flag = 0
        def mySum(n1, n2):
            return n1+n2

        self.render("sitectlreact/index.html", mySum = mySum, num=temp, perhtml=perhtml, **per, flag=flag, stus = stus)

        pass

class EscapeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1> abc is a good person</h>"
        self.render("sitectlreact/trans.html",str=str)  
        pass

class CartHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1> abc is a good person</h>"
        self.render("sitectlreact/cart.html",str=str)  
        pass

class StaticHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("sitectlreact/cart.html")  
        pass

# from liboMysql import LiboMySQL
# do not need to import if imported in sitectl.app

class DBConnORMHandler(tornado.web.RequestHandler):
    def initiate(self, *args, **kwargs):
        print("***[DBORMConnHandler] Initiate method ***")
        pass

    def get(self, *args, **kwargs):
        s=Students("Tracy", 8)
        stus = Students.all()
        self.render("sitectlreact/dbtest.html",stus=stus)  
 

class DBConnHandler(tornado.web.RequestHandler):
    def initiate(self, *args, **kwargs):
        print("***[DBConnHandler] Initiate method ***")
        pass

     
    #def get(self, *args, **kwargs):
    #    print ("***[StudentsHandler] Beginning of the Get method ****")
        # stus=self.Application.db.get_all_obj("select * from students", "students")
        # stus=self.Application.db.get_all_obj("select name,age from students", "students", "name", "age")
        # self.Application.db.insert("insert into students (name, age) values('tempname',agenum )")
        #per = {
        #    "name":"Lucas",
        #    "age":"7"
        #}
        # homework: try to create the following methods for manipulation to the database
        # per.save()
        # 
        # s = Students("Tracy", 8)
        # s.save()
        # stus = Students.all()
        # stu = Students("Lucy", 4)
        # stu.save()
        # stus = Students.all()
        # print ("stus are ", stus)
        #self.write("Database Connection Practice")
        # self.render("sitectlreact/students.html", per = per)  
        #pass
    

    def get(self, *args, **kwargs):
        str = "<h1> This is test for DB Connection</h>"
        print ("***[DBConnHandler] Beginning of the Get method ****")
        # hostname, username, password, dbName
        mydbconninfo = MyConfig.get_dbconn_info()
        print ("***[DBConnHandler] mydbconninfo is ", mydbconninfo)
        testmysql = liboMySQL(mydbconninfo['hostname'], mydbconninfo['username'], mydbconninfo['password'], mydbconninfo['dbName'])
        testmysql.get_all() 
        #chosenobjects=liboMySQL.get_all_obj() 
        self.render("sitectlreact/dbtest.html",str=str)  
        pass

# cookie
class PCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # method 1 usually use this method
        # self.set_cookie("sunck", "good")
        # method 2
        self.set_header("Set-Cookie", "libokey=libovalue; Path=/")
        self.write("OK")
        
# cookie
class GetPCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # Get Cookie
        cookie=self.get_cookie("linkzhiling", "Not logged in")
        print("cookie is ", cookie) 
        self.write("OK")
        
# cookie
class ClearPCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # Clear Cookie
        # self.clear_cookie(name, path="/", domain=None)
        self.clear_cookie("sunck")
        self.write("OK")
 


 
# cookie
class SCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_secure_cookie(name, value, expires_days = 30, version=None, **kwargs) 
        self.set_secure_cookie("zhangmanyu", "nice")
        self.write("OK") 

# cookie
class GetSCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_secure_cookie(name, value=None, max_age_days=31, min_version=None)) 
        scookie = self.get_secure_cookie("zhangmanyu")
        print("secure cookie is ", scookie)
        self.write("OK") 
 
# count the number of the request forgery
class CookieNumHandler(tornado.web.RequestHandler):
    def prepare(self):
        # block if too many attemps within a very short time
        pass

    def get(self, *args, **kwargs):
        count = self.get_cookie("count", None)
        if not count:
            count = 1
        else:
            count = int(count)
            count = count + 1
        self.set_cookie("count", str(count))   
        self.render("sitectlreact/cookienum.html", count=count)


    def post(self, *args, **kwargs):
        
        pass 

class PostFileHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('sitectlreact/postfile2.html')

    def post(self, *args, **kwargs):
        # self.get_body_argument(name, default=ARG_DEFAULT, strip=True)
        # self.get_query_arguments(name, strip=True)
        count = self.get_cookie("count", None)
        if not count:
            count = 1
        else:
            count = int(count)
            count = count + 1
        self.set_cookie("count", str(count))   
 
        self.redirect("/cookienum")
        '''
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        hobbyList = self.get_body_arguments("hobby")
        print(username, password, hobbyList)
        self.write("PostFileTest ")
        '''
       
class SetXSRFCookie(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # set a xsrf cookie

        self.xsrf_token
        self.finish("OK")

class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("***[views/index] LoginHandler ")
        str = "<h1> abc is a good person</h>"
        next=self.get_argument("next", "/")
        url = "login?next=" + next
        self.render("sitectlreact/login.html",str=str, url=url)  
        pass
    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username == "abc" and password == "abc":
            # direct into home page
            next = self.get_argument("next","/home2")
            self.redirect(next+"?flag=logedin")
        else: 
            next = self.get_argument("next", "/home2")
            print("***[views/index/LoginHandler] next = ", next)
            self.redirect("/login?next="+next)

class Home2Handler(tornado.web.RequestHandler):
    # get the current user and check if it is authenticated or not
    def get_current_user(self):
        flag =self.get_argument("flag", None)
        print ("***[views/index] Home2Handler returned value flag is ", flag)
         
        return flag
        # pass
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        print("***[views/index] Home2Handler ")
        self.render("sitectlreact/home.html",str=str)  
        pass


class Home3Handler(tornado.web.RequestHandler):
    # get the current user and check if it is authenticated or not
    def get(self, *args, **kwargs):
        self.render("sitectlreact/home.html") 

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

AsyncHTTPClient.configure(None, defaults=dict(user_agent="MyUserAgent"))
http_client = AsyncHTTPClient() 

class Students1Handler(tornado.web.RequestHandler):

    def on_response(self, response): # call back function
        print("********************handle_Response method")
        if response.error:
            self.send_error(500)
        else:
            data = json.loads(response.body)
            self.write(data)
          
        self.finish() # close the connection right here.

    # @tornado.web.asynchronous # do not close the connection, can still write even though the Get Method processing is over 
    def get(self, *args, **kwargs):
        print("[views/index] StudentsHandler Get Method")
        # get all the students information
        # might be stored in a database or another server
        # so this process is time consuming
        # time.sleep(30)
        # create a client
        url = "https://www.intelsat.com"
        http_client = AsyncHTTPClient()   
        http_response = http_client.fetch(url) 
        http_client.fetch(url, self.on_response(http_response))
        self.write("OK")    


class Students2Handler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "https://www.intelsat.com"
        http_client = AsyncHTTPClient()
        http_response = yield http_client.fetch(url)
        if http_response.error:
            self.send_error(500)
        else:
            # data = json.loads(http_response.body)
            data = http_response.body
        self.write(data)

class Students3Handler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        http_response=yield self.getData()     
        self.write(http_response)

    @tornado.gen.coroutine
    def getData(self):
        url = "https://www.intelsat.com"
        http_client = AsyncHTTPClient()
        http_response = yield http_client.fetch(url)
        # fetch: function to do time consuming operation
        if http_response.error:
            result = {"ret":0}
        else:
            # data = json.loads(http_response.body)
            result = http_response.body
        # raise is equivalent to send
        raise tornado.gen.Return(result)


class ChatHandler(WebSocketHandler):
    # open: execute when the connection is successful
    users = []
    def open(self):
        print("[views/index] ChatHandler*********************")
        # save the information
        self.users.append(self)
        print(self.users)
        for user in self.users:
            user.write_message("[%s] logged in "%(self.request.remote_ip))
    
    def on_message(self, message):
        for user in self.users:
            print(user)
            user.write_message("[%s] said [%s]"%(self.request.remote_ip, message))
        pass

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message("[%s] logged out "%(self.request.remote_ip))
        pass
    def check_origin(self, orgin):

        return True

    def close(self):
        pass    

