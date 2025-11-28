# BEGIN (write your solution here)
from states.state import State

class AlarmState:
    def __init__(self, clock):
        self.clock = clock

    def tick(self):
        self.clock.alarm_minutes += 1
    
    def get_current_mode(self):
        return 'alarm'
    
    def click_mode(self):
        self.clock.set_state('clock')

# END
