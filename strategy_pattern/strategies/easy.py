class Easy():
    # BEGIN (write your solution here)
    def analyze_field(self, field) -> None:
        position = []
        for index, raw in enumerate(field):
            if all(raw):
                continue
            position.append(index)
            for index, col in enumerate(raw):
                if col is None:
                    position.append(index)
                    break
            break
        return position
    # END
