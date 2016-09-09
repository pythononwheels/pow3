#
# pow server
#
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
import os.path
import sys
from config import config
routes = [
        (r'/',                                 LoginHandler),
        (r'.*',                                DispatcherHandler)
        ]

if __name__ == "__main__":

    #tornado.options.parse_command_line()
    #from tornado.log import enable_pretty_logging
    #enable_pretty_logging()
    #print(dir(tornado.options.options))
    tornado.options.options.log_file_prefix ='pow_server.log'
    tornado.options.options.log_file_num_backups=5
    # size of a single logfile
    tornado.options.options.log_file_max_size = 10 * 1000 * 1000
    tornado.options.parse_command_line()

    app = tornado.web.Application(handlers=routes, **app_settings)

    print("starting the MAVS Server ")
    print("visit: https://localhost:" + str(app_settings["port"]))
    print()
    #http_server = tornado.httpserver.HTTPServer(app)
    #http_server = tornado.httpserver.HTTPServer(app, **server_settings)
    #http_server.listen(app_settings["port"])
    app.listen(server["port"], **server_settings)
    tornado.ioloop.IOLoop.instance().start()