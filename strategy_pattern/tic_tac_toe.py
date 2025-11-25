from strategies.easy import Easy
from strategies.normal import Normal

STRATEGY = {'easy': Easy,
            'normal': Normal}

class TicTacToe():
    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
# BEGIN (write your solution here)
        self.level = STRATEGY[level]

    def go(self, raw:int = None, col:int = None) -> bool:
        if raw is None:
            self.level().step(self.field)
        else:
            self.field[raw][col] = 1
        return self.is_winner()
    def is_winner(self) -> bool:
        pass

# END
