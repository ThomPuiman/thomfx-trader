from abc import ABCMeta, abstractmethod

class GraphAbstract:

    @abstractmethod
    def retrieve_data(self, instrument): pass

    # @abstractmethod
    # def draw(self): pass
