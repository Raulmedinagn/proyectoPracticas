from abc import ABCMeta, abstractmethod


class Servicio(metaclass=ABCMeta):
    @abstractmethod
    def execute():
        pass
