# import calculated values
from lab2_calc import quad, add_fn


# import the main event loop
import tornado.ioloop

# map htttp requesthandlers (map requests to requests handlers)
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Lab 2 Calculator on Tornado")

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("homelab2.html")

class QuadHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>"+quad+ "</h1>")

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        value1 = int(self.get_argument("a1_arg","a2_arg", assert add_fn()))
        #value2 = int(self.get_argument("a2_arg"))
        output = add_fn()
        self.render("add.html", output = output)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/home", HomeHandler),
        (r"/quad", QuadHandler),
        (r"/add", AddHandler),
    ],
    debug = True,
    autoreload= True)

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print('all good here on 8888')

    # to start the server on current thread
    tornado.ioloop.IOLoop.current().start()