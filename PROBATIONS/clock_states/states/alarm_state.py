# BEGIN (write your solution here)
from states.state import State

class AlarmState:
    def __init__(self, clock):
        self.clock = clock

    def tick(self):
        minutes = self.clock.minutes
        minutes += 1
        if minutes / 60 == 1.0:
            self.clock.hours = (self.clock.hours + 1) % 24
            self.clock.minutes = (self.clock.minutes + 1) % 60
        else:
            self.clock.minutes = minutes
        if self.clock.is_alarm_time() and self.clock.is_alarm_on():
            self.clock.set_state('bell')
    
    def get_current_mode(self):
        return 'alarm'
    
    def click_mode(self):
        self.clock.set_state('clock')
    
    def click_h(self):
       self.clock.alarm_hours = (self.clock.alarm_hours + 1) % 24

    def click_m(self):
       self.clock.alarm_minutes = (self.clock.alarm_minutes + 1) % 60
    
    def is_alarm_time(self):
        #print('self.clock.hours', self.clock.hours, 'self.clock.minutes', self.clock.minutes, 'self.clock.alarm_hours', self.clock.alarm_hours, 'self.clock.alarm_minutes', self.clock.alarm_minutes)
        return (self.clock.hours, self.clock.minutes) == (self.clock.alarm_hours, self.clock.alarm_minutes)

# END
