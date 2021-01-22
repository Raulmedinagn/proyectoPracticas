from abc import ABCMeta, abstractmethod
from Servicio import Servicio


class Calculador(Servicio, metaclass=ABCMeta):
    @abstractmethod
    def get_precision(self):
        pass
    
    @abstractmethod
    def get_exhaustividad(self):
        pass
# -*- coding: utf-8 -*-

