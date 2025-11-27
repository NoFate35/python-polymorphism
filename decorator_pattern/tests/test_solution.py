import sys
sys.path.append('/home/ivan/python-polymorphism/decorator_pattern')
from solution import CalcLogger
from calculator import Calculator


def test_calc():
    calc = Calculator(5)
    assert calc.add(5).mul(5).sub(10).result() == 40
    assert calc.add(5).result() == 10


def test_calc_logger_with_init_state(capsys):
    calc = Calculator().add(3)

    calc = CalcLogger(calc)
    assert calc.add(4).result() == 7
    captured = capsys.readouterr()
    assert captured.out == "Первое число: 3 Второе число: 4 Сумма: 7\n"


def test_calc_logger_fluent(capsys):
    calc = CalcLogger(Calculator(5))

    assert calc.add(5).mul(5).sub(10).result() == 40
    captured = capsys.readouterr()
    assert captured.out == """Первое число: 5 Второе число: 5 Сумма: 10
Первое число: 10 Второе число: 5 Результат: 50
Первое число: 50 Второе число: 10 Разность: 40\n"""
