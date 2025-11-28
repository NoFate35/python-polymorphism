from alarm_clock import AlarmClock


def test_default_values():
    clock = AlarmClock()
    assert clock.get_minutes() == 0
    assert clock.get_hours() == 12
    assert clock.get_alarm_hours() == 6
    assert clock.get_alarm_minutes() == 0


def test_change_state_when_click_mode():
    clock = AlarmClock()
    assert not clock.is_alarm_on()
    assert clock.get_current_mode() == 'clock'

    clock.click_mode()
    clock.tick()
    assert not clock.is_alarm_on()
    assert clock.get_current_mode() == 'alarm'

    clock.click_mode()
    clock.tick()
    assert not clock.is_alarm_on()
    assert clock.get_current_mode() == 'clock'

    clock.long_click_mode()
    clock.tick()
    assert clock.is_alarm_on()
    assert clock.get_current_mode() == 'clock'

    clock.click_mode()
    clock.tick()
    assert clock.is_alarm_on()
    assert clock.get_current_mode() == 'alarm'

    clock.click_mode()
    clock.tick()
    assert clock.is_alarm_on()
    assert clock.get_current_mode() == 'clock'

    clock.long_click_mode()
    assert not clock.is_alarm_on()
    assert clock.get_current_mode() == 'clock'


def test_changing_hours_and_minutes():
    clock = AlarmClock()

    clock.click_h()
    assert clock.get_minutes() == 0
    assert clock.get_hours() == 13
    assert clock.get_alarm_hours() == 6
    assert clock.get_alarm_minutes() == 0

    clock.click_m()
    assert clock.get_minutes() == 1
    assert clock.get_hours() == 13
    assert clock.get_alarm_hours() == 6
    assert clock.get_alarm_minutes() == 0

    clock.click_mode()

    clock.click_h()
    assert clock.get_minutes() == 1
    assert clock.get_hours() == 13
    assert clock.get_alarm_hours() == 7
    assert clock.get_alarm_minutes() == 0

    clock.click_m()
    assert clock.get_minutes() == 1
    assert clock.get_hours() == 13
    assert clock.get_alarm_hours() == 7
    assert clock.get_alarm_minutes() == 1

    for _ in range(60):
        clock.click_m()

    assert clock.get_alarm_hours() == 7
    assert clock.get_alarm_minutes() == 1

    for _ in range(17):
        clock.click_h()
    assert clock.get_alarm_hours() == 0


def test_no_belling_if_alarm_off():
    clock = AlarmClock()
    for _ in range(18 * 60):
        clock.tick()
    assert clock.is_alarm_time()
    assert clock.get_current_mode() == 'clock'
    assert clock.get_hours() == 6
    assert clock.get_minutes() == 0
    clock.tick()
    assert clock.get_current_mode() == 'clock'


def test_starting_bell_if_alarm_on_1():
    clock = AlarmClock()
    clock.long_click_mode()
    for _ in range(18 * 60):
        clock.tick()
    assert clock.is_alarm_time()
    assert clock.get_current_mode() == 'bell'
    assert clock.get_hours() == 6
    assert clock.get_minutes() == 0
    clock.tick()
    assert clock.get_current_mode() == 'clock'


def test_starting_bell_if_alarm_on_2():
    clock = AlarmClock()
    clock.long_click_mode()
    for _ in range(18 * 60):
        clock.tick()
    assert clock.is_alarm_time()
    assert clock.get_current_mode() == 'bell'
    clock.click_mode()
    assert clock.get_current_mode() == 'clock'


def test_starting_bell_if_alarm_on():
    clock = AlarmClock()
    clock.long_click_mode()
    clock.click_mode()
    assert clock.get_current_mode() == 'alarm'
    for _ in range(18 * 60):
        clock.tick()
    assert clock.is_alarm_time()
    assert clock.is_alarm_on()
    assert clock.get_current_mode() == 'bell'

    clock.click_mode()
    assert clock.get_current_mode() == 'clock'


def test_no_bell_for_alarm_mode_if_alarm_off():
    clock = AlarmClock()
    clock.click_mode()
    assert clock.get_current_mode() == 'alarm'
    for _ in range(18 * 60):
        clock.tick()
    assert clock.is_alarm_time()
    assert not clock.is_alarm_on()
    assert clock.get_current_mode() == 'alarm'

    clock.click_mode()
    clock.tick()
    assert clock.get_current_mode() == 'clock'


def test_increment_minutes_after_alarm():
    clock = AlarmClock()
    clock.long_click_mode()
    for _ in range(18 * 60):
        clock.tick()
    assert clock.is_alarm_time()
    assert clock.get_current_mode() == 'bell'
    clock.tick()
    assert clock.get_current_mode() == 'clock'
    assert clock.get_minutes() == 1
