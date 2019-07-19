#!/usr/bin/env python
#print('hello 美好的世界')
#tornado learing start
# ==============================================
# import  tornado.ioloop
# import  tornado.web
#
# class MainHadler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('你好，我是贱桥。')
# application = tornado.web.Application(
#     [
#         (r"/",MainHadler),
#     ]
# )
#
# if __name__ == "__main__":
#     application.listen(8080)
#     tornado.ioloop.IOLoop.instance().start()
# ====================================================

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

from tornado.options import define,options

define('port',default=8080,help='run port',type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello，我是贱桥')


class InHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name','no')
        self.write(name)
        name1 = self.get_arguments('name')
        print(name1)

###
aappclication = tornado.web.Application(
    [
        (r"/jianqiao",MainHandler),
        (r"/get",InHandler)
    ]
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(aappclication)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

