from abc import ABCMeta, abstractmethod
from Servicio import Servicio


class KeyWords(Servicio, metaclass=ABCMeta):
    @abstractmethod
    def extraerKeywords(self, frase):
        pass
