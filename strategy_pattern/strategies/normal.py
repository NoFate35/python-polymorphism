class Normal():
    # BEGIN (write your solution here)
    def analyze_field(self, field) -> None:
        print('self.fiiield', field)
        position = []
        for index, raw in enumerate(field[::-1], start=-len(field)):
            if all(raw):
                continue
            position.append(abs(index) - 1)
            for index, col in enumerate(raw):
                if col is None:
                    position.append(index)
                    break
            break
        return position
    # END
