#
#
# pow settings file
# 
from sqlalchemy.ext.declarative import declarative_base

server = {
    "app_name"          :   "powtest",
    "port"              :   8080,
    "debug"             :   True,
    "https"             :   False,
    "template_path"     :   "./views",
    "static_path"       :   "./static",
    "static_url_prefix" :   "/static/",
    "login_url"         :   "/login",
    "cookie_secret"     :   "254f2254-6bb0-1312-1104-3a0786ce285e",
}

app = {
    "stubs_path"        :   "./stubs",
    "model_path"        :   "./models",
    "default_format"    :   "html",
    "base_url"          :   "https://localhost",
}


db = {
    "type"  :   "postgresql",
    "name"  :   "powtest",
    "host"  :   "localhost",
    "port"  :   5432,
    "user"  :   "powtest",
    "passwd":   "powtest"
}


Base = declarative_base()

