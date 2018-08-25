
def CreateApp(name=__name__):
    from flask import Flask
    from flask_restful import Api

    app = Flask(name)
    api = Api(app)

    from wtfrestful.restful import WSGI
    from wtfrestful.restful.hello import World
    World.AddToAPI(api, WSGI())

    return app

if __name__ == '__main__':
    app = CreateApp()
    app.run(debug=True)