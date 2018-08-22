from .. import Interactor, Factory

class Factory(Factory):
    pass

class World(Interactor):
    
    FactoryType = Factory.Default

    def hello(self, name):
        return r'Hello {name}!'
