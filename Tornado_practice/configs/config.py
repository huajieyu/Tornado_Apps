import os

PROJECT_ROOT=os.path.dirname(os.path.abspath(__file__))
BASE_DIR=os.path.dirname(PROJECT_ROOT)
 
# BASE_DIR=os.path.dirname(__file__)
# BASE_DIR=os.getcwd()
class MyConfig:
    def get_config():
        options = {
            'destPort':8885,
            'destIP':'10.145.39.141',
        }
        return options
    def get_mysql():
        mysql = {
            "host":"10.0.144.21",
            "username":"root",
            "password":"scc",
            "dbName":"test"
        }
        return mysql
    def get_settings():
        my_settings = {
            "base_path": BASE_DIR,
            "static_path": os.path.join(BASE_DIR, "static"),
            "static_url_prefix": "/static/",
            # "cookie_secret":"__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            "cookie_secret":"b'N+8JAok+SlK+gaC/K4JeniIt0B3YVEsgiwEnZDwJv6k='",
            "login_url":"/login",
            "template_path":os.path.join(BASE_DIR, "templates"),
            "xsrf_cookies":True, # trun on the xsrf protection  will use the cookie_secret
            # "autoescape":None,
        }
        return my_settings
    def get_dbconn_info():
        my_dbconn_info = {
            "hostname": "hostnametemp",
            "username": "scc",
            "password": "scc",
            "dbName": "tablename"
        }
        return my_dbconn_info
    def get_profiles():
        profiles = {
            'LAB': 'dnm6svr',
            'SD1': 'dnm6svr',
            'SD2': 'dnm6svr',
            'MCC': 'dnm5svr',
            'LSOC': 'dnm2svr',
            'ESOC': 'dnm1svr',
        }
        return profiles
