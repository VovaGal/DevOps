# import calculated values
from lab2_calc import quad, add_fn, sub_fn, mult_fn, div_fn, a, b, c


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
        #quada = self.get_argument()
        #quadb
        #quadc
        self.write("<h1>"+quad+ "</h1>")

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        valuea1 = self.get_argument("a1_arg")
        valuea2 = self.get_argument("a2_arg")
        outputa = add_fn(a1_arg=int(valuea1),a2_arg=int(valuea2))
        self.render("add.html", outputa = outputa)

class SubHandler(tornado.web.RequestHandler):
    def get(self):
        values1 = self.get_argument("s1_arg")
        values2 = self.get_argument("s2_arg")
        outputs = sub_fn(a1_arg=int(values1),a2_arg=int(values2))
        self.render("add.html", outputs = outputs)

class MultHandler(tornado.web.RequestHandler):
    def get(self):
        valuem1 = self.get_argument("m1_arg")
        valuem2 = self.get_argument("m2_arg")
        outputm = mult_fn(m1_arg=int(valuem1),m2_arg=int(valuem2))
        self.render("add.html", outputm = outputm)

class DivHandler(tornado.web.RequestHandler):
    def get(self):
        valued1 = self.get_argument("d1_arg")
        valued2 = self.get_argument("d2_arg")
        outputd = div_fn(d1_arg=int(valued1),d2_arg=int(valued2))
        self.render("add.html", outputd = outputd)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/home", HomeHandler),
        (r"/quad", QuadHandler),
        (r"/add", AddHandler),
        (r"/sub", SubHandler),
        (r"/mult", MultHandler),
        (r"/div", DivHandler),
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