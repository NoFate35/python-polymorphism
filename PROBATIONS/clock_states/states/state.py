from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def increment_h(self):
        pass

    @abstractmethod
    def increment_m(self):
        pass

    @abstractmethod
    def tick(self):
        pass
