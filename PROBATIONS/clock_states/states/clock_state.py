# BEGIN (write your solution here)
from states.state import State

class ClockState():

    def __init__(self, clock):
        self.clock = clock

    def get_current_mode(self):
        return 'clock'
    
    def click_mode(self):
        self.clock.set_state('alarm')

    def tick(self):
        self.clock.minutes += 1

    def click_h(self):
    	self.clock.hours += 1

    def click_m(self):
    	self.clock.tick()
# END
