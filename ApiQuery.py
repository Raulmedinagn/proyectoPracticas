from abc import ABCMeta, abstractmethod
from Servicio import Servicio


class ApiQuery(Servicio, metaclass=ABCMeta):
    @abstractmethod
    def extraerDatos(self, url):
        pass
