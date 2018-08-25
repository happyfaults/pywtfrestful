from .. import Interactor, Factory

class Factory(Factory):
    pass

class World(Interactor):
    
    FactoryType = Factory.Default

    def set_names(self):
        self.names = {}
        return self.names

    def getName(self, nick):
        return self.names.get(nick)

    def setName(self, nick, name):
        self.names[nick] = name
        return self

    def getStats(self):
        return {
            'count': len(self.names),
        }
    
