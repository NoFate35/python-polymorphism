import pytest
from io import StringIO
import sys
from character import Character


@pytest.fixture
def character():
    return Character("Hero", 100, 20)


@pytest.fixture
def capture_output():
    captured_output = StringIO()
    sys.stdout = captured_output
    #print('sys.stdout', sys.__stdout__)
    yield captured_output
    sys.stdout = sys.__stdout__


def test_default_state(character, capture_output):
    assert character.name == "Hero"
    assert character.max_health == 100
    assert character.current_health == 100
    assert character.base_attack_power == 20
    assert character.current_attack_power == 20

    actual_damage = character.attack()
    assert actual_damage == character.base_attack_power

    actual_output = capture_output.getvalue().strip()
    
    assert "Hero attacks for 20 damage" in actual_output

    expected_representation = "Hero (HP: 100/100, AP: 20, State: Normal)"
    assert str(character) == expected_representation


def test_poisoned_state(character, capture_output):
    character.poison()
    assert character.current_health == character.max_health

    character.update()
    assert character.current_health == character.max_health - 5
    assert character.current_attack_power == character.base_attack_power // 2

    actual_damage = character.attack()
    assert actual_damage == character.base_attack_power // 2

    actual_output = capture_output.getvalue().strip()
    assert "Hero exits normal state" in actual_output
    assert "Hero is poisoned" in actual_output
    assert "Hero attacks for 10 damage" in actual_output

    expected_representation = "Hero (HP: 95/100, AP: 10, State: Poisoned)"
    assert str(character) == expected_representation


def test_frozen_state(character, capture_output):
    character.freeze()
    character.update()

    assert character.current_health == character.max_health
    assert character.current_attack_power == 0
    assert character.attack() == 0

    actual_output = capture_output.getvalue().strip()
    assert "Hero exits normal state" in actual_output
    assert "Hero is frozen" in actual_output
    assert "Hero attacks for 0 damage" in actual_output

    expected_representation = "Hero (HP: 100/100, AP: 0, State: Frozen)"
    assert str(character) == expected_representation


def test_berserk_state(character, capture_output):
    character.berserk()
    character.update()

    assert character.current_health == character.max_health

    actual_damage = character.attack()
    assert actual_damage == character.base_attack_power * 2

    self_damage = character.base_attack_power // 2
    assert character.current_health == character.max_health - self_damage

    actual_output = capture_output.getvalue().strip()
    assert "Hero exits normal state" in actual_output
    assert "Hero goes berserk" in actual_output
    assert "Hero attacks for 40 damage" in actual_output

    expected_representation = "Hero (HP: 90/100, AP: 40, State: Berserk)"
    assert str(character) == expected_representation


def test_take_damage(character):
    damage = 30
    character.take_damage(damage)
    assert character.current_health == character.max_health - damage

    expected_representation1 = "Hero (HP: 70/100, AP: 20, State: Normal)"
    assert str(character) == expected_representation1

    with pytest.raises(ValueError):
        character.take_damage(70)


def test_transition_chain(character):
    character.poison()
    character.update()
    assert character.current_health == 95
    assert character.current_attack_power == character.base_attack_power // 2
    expected_representation1 = "Hero (HP: 95/100, AP: 10, State: Poisoned)"
    assert str(character) == expected_representation1

    character.reset()
    character.update()
    assert character.current_health == 95
    assert character.current_attack_power == character.base_attack_power
    expected_representation2 = "Hero (HP: 95/100, AP: 20, State: Normal)"
    assert str(character) == expected_representation2

    character.berserk()
    character.update()
    assert character.current_health == 95
    assert character.current_attack_power == character.base_attack_power * 2
    character.attack()
    assert character.current_health == 85
    expected_representation3 = "Hero (HP: 85/100, AP: 40, State: Berserk)"
    assert str(character) == expected_representation3


def test_invariants1(character):
    character.take_damage(95)
    with pytest.raises(ValueError):
        character.poison()
        character.update()


def test_invariants2(character):
    character.take_damage(95)
    character.berserk()
    character.update()
    with pytest.raises(ValueError):
        character.attack()
