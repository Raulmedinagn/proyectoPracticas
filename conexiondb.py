from abc import ABCMeta, abstractmethod
from Servicio import Servicio


class BBDD(Servicio, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, host, user, password, database):
        self.host = host,
        self.user = user,
        self.spassword = password,
        self.database = database

    @abstractmethod
    def executeQ(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def update(self):
        pass
