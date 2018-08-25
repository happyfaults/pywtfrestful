from .. import Resource


class World(Resource):

    @classmethod
    def AddToAPI(cls, api, wsgi, base_uri='', hello_app=None, **kwargs):
        if hello_app is None:
            from wtfrestful.client.hello import World
            hello_app = World.Load()

        api.add_resource(
            cls, 
            base_uri + '/hello/<string:nick>',
            resource_class_args=(
                hello_app,
                wsgi
            ),
            resource_class_kwargs=kwargs
        )

        return api

    def __init__(self, hello_app, *args, **kwargs):
        super(World, self).__init__(*args, **kwargs)
        self.hello_app = hello_app

    def get(self, nick): 
        app = self.hello_app
        name = app.getName(nick)
        return {
            'msg': f'Hello {name}!'
        }

    def put(self, nick):
        app = self.hello_app
        app.setName(nick, self.wsgi.request.form['name'])
        return app.getStats()