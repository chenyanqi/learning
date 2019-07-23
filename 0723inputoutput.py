#auther chenyanqi
import tornado.ioloop
import tornado.web
import time
import tornado.httpserver
import tornado.options   #命令行解析模块，让模块定义自己得选项

from tornado.options import define,options

define('port',default=8080,help='run port',type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello，我是贱桥') #字符串打印
        self.write('<br>')
        self.write(b'xupeng<br>')   #二进制
        self.flush()  #缓冲区
        user = {
            'name' : 'chenshuaiqi',
            'age' : 19,
            'li' : [1, 2, 3, 4, 5]
        }                   #字典打印，不能直接打印列表，可以当作字典传参
        self.write(user)
        self.finish()     #结束打印
        self.write(b'/hahahahah')

class TemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('0723inout.html')


class RecHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.redirect('/tem')



class InHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name','no')
        self.write(name)
        name1 = self.get_arguments('name')
        print(name1)

###
aappclication = tornado.web.Application(
   handlers =  [
        (r"/jianqiao",MainHandler),
        (r"/get",InHandler),
        (r"/tem",TemHandler),
        (r"/rec",RecHandler)
    ],
    template_path='templates',
    debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(aappclication)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()