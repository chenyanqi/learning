#auther chenyanqi
import tornado.ioloop
import tornado.web
import time
import tornado.httpserver
import tornado.options   #命令行解析模块，让模块定义自己得选项

from tornado.options import define,options

define('port',default=8080,help='run port',type=int)



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.render('0723inout.html')






aappclication = tornado.web.Application(
   handlers =  [
       (r"/(main",IndexHandler)
    ],
    template_path='templates',
    debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(aappclication)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()