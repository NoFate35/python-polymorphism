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
        def make_step(field: list, raw: int , col: int, badge: int) -> None:
            field[raw][col] = badge

        if raw is None:
            raw, col = self.level().analyze_field(self.field)
            badge = 2
        else:
            badge = 1
        make_step(self.field, raw, col, badge)
        #print('self.fiiield', self.field)
        return self.is_winner()


    def is_winner(self) -> bool:
        lines = [[(0, 1),(1, 1), (2, 1)],
                 [(0, 0), (0, 1), (0, 2)],
                 [(0, 0), (1, 1), (2, 2)],
                 [(2, 0), (2, 1), (2, 2)],
                 ]
        for line in lines:
            num = []
            for point in line:
                num.append(self.field[point[0]][point[1]])
            if (num[0]==num[1]) and (num[0]==num[2]) and (num[0] != None):
                return True
        return False
# END
