# BEGIN (write your solution here)
class BellState:
    def __init__(self, clock):
        self.clock = clock

    def get_current_mode(self):
        return 'bell'

    def is_alarm_time(self):
        return (self.clock.hours, self.clock.minutes) == (self.clock.alarm_hours, self.clock.alarm_minutes)
    
    def tick(self):
        minutes = self.clock.minutes
        minutes += 1
        if minutes / 60 == 1.0:
            self.clock.click_h()
            self.clock.click_m()
        else:
            self.clock.minutes = minutes
        self.clock.set_state('clock')

    def click_mode(self):
        self.clock.set_state('clock')

    def is_alarm_time(self):
        return (self.clock.hours, self.clock.minutes) == (self.clock.alarm_hours, self.clock.alarm_minutes)

    def is_alarm_on(self):
        return self.clock.is_alarm_on()
# END
