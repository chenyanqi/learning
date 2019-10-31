#auther chenyanqi
import tornado.ioloop
import tornado.web
import time
import tornado.httpserver
import tornado.options   #命令行解析模块，让模块定义自己得选项

from tornado.options import define,options

define('port',default=8080,help='run port',type=int)

class HeaderHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('set_header')
        self.set_header('aaa','1111')
        self.set_header('bbb','222')
        self.set_header('bbb','333')


class AddHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('add_header')
        self.add_header('ccc','1111')
        self.add_header('ccc','1111')

class SendHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('send_header')
        self.send_error(500)

    def write_error(self, status_code, **kwargs):
        self.write('status_code:%s' % status_code  )
        self.write('<br>你得页面被吃掉了')


class NotfoundHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('send_header')
        self.send_error(404)

    def write_error(self, status_code, **kwargs):
        self.write('status_code:%s' % status_code  )
        self.write('<br>你访问得是啥啊。')
   '''
    def set_default_headers(self):
    def initialize(self):
    def post(self, *args, **kwargs):
    def get(self):
    def prepare(self):
    def on_finish(self):
    '''





aappclication = tornado.web.Application(
   handlers =  [
       (r"/main",HeaderHandler),
       (r"/add",AddHandler),
       (r"/send",SendHandler),
       (r"/(.*)",NotfoundHandler),
    ],
    template_path='templates',
    debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(aappclication)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()