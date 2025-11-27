class CalcLogger:
    # BEGIN (write your solution here)
    def __init__(self, calc):
        self.calc = calc
        self.log = []
    
    def add(self, num):
        first_num = self.calc.acc
        self.calc = self.calc.add(num)
        self.log.append(f'Первое число: {first_num} Второе число: {num} Сумма: {self.calc.acc}')
        return self

    def sub(self, num):
        first_num = self.calc.acc
        self.calc = self.calc.sub(num)
        self.log.append(f'Первое число: {first_num} Второе число: {num} Разность: {self.calc.acc}')
        return self

    def mul(self, num):
        first_num = self.calc.acc
        self.calc = self.calc.mul(num)
        self.log.append(f'Первое число: {first_num} Второе число: {num} Результат: {self.calc.acc}')
        return self

    def result(self):
        print('\n'.join(self.log))
        return self.calc.result()
    # END