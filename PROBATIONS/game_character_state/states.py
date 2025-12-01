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
class NormalState(State):
    def __init__(self, character):
    	self.character = character
    	self.enter()
    	
    def handle_attack(self):
    	return self.character.base_attack_power
    
    def enter(self):
    	print('enters normal state')
    
    def exit(self):
    	pass
    
    def get_title(self):
        return 'Normal'
    
    def update(self):
        pass
    def __str__(self):
    	return(self.character)
    	
    	

class PoisonedState:
    pass
    
class BerserkState:
    pass

class FrozenState:
    pass
# END
