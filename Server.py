from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    @abstractmethod
    def procesarRequest():
        pass
