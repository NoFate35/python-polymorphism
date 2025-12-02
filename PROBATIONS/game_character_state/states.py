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
        print('Hero exits normal state')

    def get_title(self):
        return 'Normal'
    
    def update(self):
        self.character.current_attack_power = self.character.base_attack_power
    def __str__(self):
    	return(self.character)
    	
    	

class PoisonedState(State):
    def __init__(self, character):
        self.character = character
        self.enter()
        self.poisoned_current_health = self.character.current_health - 5
        self.poisoned_attack_power = self.character.base_attack_power // 2

    def enter(self):
        print('Hero is poisoned')

    def get_title(self):
        return 'Poisoned'
 
    def exit(self):
        print('Hero is no longer poisoned')

    def update(self):
        self.character.current_health = self.poisoned_current_health
        self.character.current_attack_power = self.poisoned_attack_power
        if self.poisoned_current_health <= 0:
            raise ValueError(f"{self.character.name} leaves the game")
    def handle_attack(self):
        return self.character.current_attack_power
    
    def reset(self):
        self.character._set_state(NormalState(self))

    def __str__(self):
    	return(self.character)
    
class BerserkState(State):
    def __init__(self, character):
        self.character = character
        self.enter()
        self.berserk_current_health = self.character.current_health
        self.berserk_attack_power = self.character.base_attack_power * 2

    def enter(self):
        print('Hero goes berserk')

    def get_title(self):
        return 'Berserk'
 
    def exit(self):
        print('Hero calms down')

    def update(self):
        self.character.current_health = self.berserk_current_health
        self.character.current_attack_power = self.berserk_attack_power
        
    def handle_attack(self):
        self_damage = self.character.base_attack_power // 2
        self.character.current_health = self.berserk_current_health - self_damage
        if self.character.current_health <= 0:
            raise ValueError(f"{self.character.name} leaves the game")
        return self.character.current_attack_power 
    
    def __str__(self):
    	return(self.character)

class FrozenState(State):
    def __init__(self, character):
        self.character = character
        self.enter()
        self.frozen_current_health = self.character.max_health
        self.frozen_attack_power = 0

    def enter(self):
        print('Hero is frozen')

    def get_title(self):
        return 'Frozen'
 
    def exit(self):
        print('Hero is no longer frozen')

    def update(self):
        self.character.current_health = self.frozen_current_health
        self.character.current_attack_power = self.frozen_attack_power
        
    def handle_attack(self):
        return self.character.current_attack_power
    
    def __str__(self):
    	return(self.character)
# END
