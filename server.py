import tornado.ioloop
import tornado.web


class HandlerMethod(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world!")
        print(tornado.web.RequestHandler)


def make_app():
    return tornado.web.Application([
        (r"/", HandlerMethod),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()