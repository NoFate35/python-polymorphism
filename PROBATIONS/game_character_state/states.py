from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def handle_attack(self):
        pass


# BEGIN (write your solution here)
class NormalState:
    pass

class PoisonedState:
    pass
    
class BerserkState:
    pass

class FrozenState:
    pass
# END
