from states.clock_state import ClockState
from states.alarm_state import AlarmState
from states.bell_state import BellState


# BEGIN (write your solution here)
class AlarmClock:
    def __init__(self):
        self.STATES = {
            'clock': ClockState,
            'alarm': AlarmState
        }
        self.set_state('clock')
        self.hours = 12
        self.minutes = 0
        self.alarm_hours = 6
        self.alarm_minutes = 0
        self.alarm = False

    def set_state(self, name):
        self.state = self.STATES[name](self)
    
    def get_alarm_minutes(self):
        return self.alarm_minutes
    
    def get_alarm_hours(self):
        return self.alarm_hours
    
    def get_minutes(self):
        return self.minutes
    
    def get_hours(self):
        return self.hours

    def is_alarm_on(self):
        return self.alarm
    
    def get_current_mode(self):
        return self.state.get_current_mode()
    
    def click_mode(self):
        self.state.click_mode()
    
    def tick(self):
        self.state.tick()
    
    def long_click_mode(self):
        if self.alarm:
            self.alarm = False
        else:
            self.alarm = True

# END
