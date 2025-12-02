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
    	
    	

class PoisonedState(State):
    def __init__(self, character):
    	self.character = character
    	self.enter()

    def enter(self):
    	print('is poisoned')

    def get_title(self):
        return 'Poisoned'
 
    def exit(self):
        print('is no longer poisoned')

    def update(self):
        new_current_health = self.character.max_health
        new_attack_power = self.character.base_attack_power
        self.character.current_health = new_current_health - 5
        self.character.current_attack_power = new_attack_power // 2
        
    def handle_attack(self):
    	pass

    def __str__(self):
    	return(self.character)
    
class BerserkState:
    pass

class FrozenState:
    pass
# END
