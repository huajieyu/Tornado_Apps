from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.options import *  
# options is used to define, store and convert of global parameters
# [define, parse_command_line, options]
#from traitlets import config
#from traitlets.config.application import Application
#from traitlets import Integer, Unicode
import SecurityEncryption
import tornado.web
import socket, sys
import argparse
import os, time
import settings
from configs.config import MyConfig
from views import index
from ORM.liboMysql import liboMySQL
from ORM.orm import ORM
# tornado.options.define(name, default=None, type=None, help=None, metavar=None, multiple=False, group=None, callback=None)
tornado.options.define("destPort", default=8885, type=int, help='Port of GNS Site Control Server')
tornado.options.define("destIP", default='10.145.39.148', type=str, help='IP Address of the Site Control Server')


parser = argparse.ArgumentParser(description = 'Setup Server Info for Site Control')
parser.add_argument('-destIP', help = 'IP Address of the Site Control Server', required=False, default='10.145.39.148')
parser.add_argument('-destPort', help = 'Port of GNS Site Control Server', required=False, default=8885)
parser.add_argument('-debug', help = 'Use debug level logging', default=False, action = 'store_true')
parser.add_argument('-secure', help='Use HTTPS protocal', default=False, action='store_true')
# parser.add_argument('-certfile', help='Certificate file name for secure mode https', required=False, default='/etc/ssl/certs/ca-bundle.crt')
parser.add_argument('-logfile', help='Log file name', required=False, default='')
parser.add_argument('-webport', help='Port to use for web service')

settings.init()  

'''
'''
def make_app():
    mysettings = MyConfig.get_settings()
    return Application([
                        #(r"/json", JsonHandler),
                        #(r"/index1", index.IndexHandler),
                        #(r"/index2", index.RedirectHandler, {"key1":"value1", "key2":"value2"}),
                        #tornado.web.url(r"/asdfgh", index.TestHandler,{"key3":"value3", "key4":"value4"}, name="index"),
                        # url method
                        # tornado.web.url(r"/sectest/(\w+)/(\w+)/(\w+)", index.SecTestHandler),
                        #tornado.web.url(r"/sectest/(?P<par1>\w+)/(?P<par3>\w+)/(?P<par2>\w+)", index.SecTestHandler),
                        # get method 
                        #tornado.web.url(r"/thitest", index.ThiTestHandler),
                        #tornado.web.url(r"/foutest", index.FouTestHandler),
                        # post method
                        tornado.web.url(r"/postfile", index.PostFileHandler),
                        # request object
                        #tornado.web.url(r"/zhuyin", index.ZhuyinHandler),
                        #tornado.web.url(r"/upfile", index.UpFileHandler),
                        # Write
                        #tornado.web.url(r"/write", index.WriteHandler),
                        tornado.web.url(r"/home", index.HomeHandler),
                        #tornado.web.url(r"/function", index.FunctionHandler),
                        # escape
                        #tornado.web.url(r"/escape", index.EscapeHandler),
                        # inherit
                        tornado.web.url(r"/cart", index.CartHandler),
                        # static webpage 
                        # tornado.web.url(r"/cart", index.CartHandler),
                        # default_filename 
                        #(r'/(.*)$', tornado.web.StaticFileHandler, {"path":os.path.join(mysettings["base_path"], "static/html"), "default_filename":"index.html"}),
                        # connect to a database
                        #tornado.web.url(r"/dbconnection", index.DBConnHandler),
                        # regular cookie
                        tornado.web.url(r"/pcookie", index.PCookieHandler),
                        tornado.web.url(r"/getpcookie", index.GetPCookieHandler),
                        tornado.web.url(r"/clearpcookie", index.ClearPCookieHandler),
                        # encripted cookie
                        tornado.web.url(r"/scookie", index.SCookieHandler),
                        tornado.web.url(r"/getscookie", index.GetSCookieHandler),
                        # count cookies: count how many attemps that the browers 
                        tornado.web.url(r"/cookienum", index.CookieNumHandler),
                        # setup _xsrf cookie
                        tornado.web.url(r"/setxsrfcookie", index.SetXSRFCookie),
                        # (r'/(.*)$', index.StaticFileHandler, {"path":os.path.join(mysettings["base_path"], "static/html"), "default_filename":"index.html"}),
                        #authentication
                        tornado.web.url(r"/login", index.LoginHandler),
                        tornado.web.url(r"/home2", index.Home2Handler),
                        tornado.web.url(r"/home3", index.Home3Handler),
                        tornado.web.url(r"/chat", index.ChatHandler),
                        # asynchronous
                        tornado.web.url(r"/students01", index.Students1Handler),
                        tornado.web.url(r"/students02", index.Students2Handler),
                        tornado.web.url(r"/students03", index.Students3Handler),
                        ], **mysettings)

    
    debug = True   #run the app in debug/development mode
                   #several features intended for convenience 
                   #while developing will be enabled
    # autoreload = True  #The app will watch for changes to 
                       #its source files and reload itself when anything changes

    # compiled_template_cache = False # default is True  

    # static_hash_cache = False

    # serve_traceback = True
    # move to other place
    # mysql = MyConfig.get_mysql()
    # self.db=MyConfig.liboMySQL(mysql["host"], mysql["username"], mysql["password"], mysql["dbName"])

 
if __name__ == "__main__":

    # Run the webapp test in LAB 
    os.environ["GNS_PROFILE"]="LAB"  
    ssl_config = SecurityEncryption.get_encryption_params()
     
    app = HTTPServer(make_app(), ssl_options={
        "certfile": ssl_config['crt'],
       "keyfile": ssl_config['key']
    })
    
    
    print('***[app] ssl certificate file is ', ssl_config['crt'])
    print('***[app] ssl key file is ', ssl_config['key'])
    #********************************************************************

    args = parser.parse_args()
    port = args.destPort


    print('***[app] the port number is ', port)
    print('***[app] the hostname is ', socket.gethostname())

    # Get the site name, crb number and ip address that we want to start; 
    # get it from the webpage later
    ipaddr = socket.gethostbyname(socket.gethostname()) #sys.argv[2]

    

    # start accepting connections on the give port number 
    # app.listen(tornado.options.options.destPort)
    myoptions = MyConfig.get_config()


    app.bind(myoptions['destPort'])
    app.start(1)
    # app.listen(myoptions['destPort'])


    print ('***[app] Client Selected IP Address for Operation is ', ipaddr)
    print ('***[app] The host name is ', socket.gethostname())
    print ('***[app] Server for webapp started at {0}:{1} ***'.format(ipaddr, port))


    # use iploop.instance when you mean to communicate to the main thread from a different one
    # tornado.ioloop.IOLoop.instance().start()
    # usually use ioloop.current as the default shen constructing an asynchronous object
    tornado.ioloop.IOLoop.current().start()


