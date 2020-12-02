# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from Servicio import Servicio


class Recomendador(Servicio, metaclass=ABCMeta):
    @abstractmethod
    def get_recomendations(self):
        pass

