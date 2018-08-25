from flask_restful import Resource

from wtfrestful.lib.lang import LazyObject

class WSGI(LazyObject):

    def set_request(self):
        from flask import request
        self.request = request
        return self.request


class Resource(Resource):

    def __init__(self, wsgi, *args, **kwargs):
        self.wsgi = wsgi
