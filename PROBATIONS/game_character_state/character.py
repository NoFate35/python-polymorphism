from states import NormalState, PoisonedState, BerserkState, FrozenState


class Character:
    def __init__(self, name, max_health, base_attack_power):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.base_attack_power = base_attack_power
        self.current_attack_power = base_attack_power
        self.state = NormalState(self)

    def attack(self):
        damage = self.state.handle_attack()
        message = f"{self.name} attacks for {damage} damage"
        print(message)
        return damage

    def take_damage(self, damage):
        print('self.current_health', self.current_health, 'damage', damage, )
        if damage >= self.current_health:
            raise ValueError(f"{self.name} leaves the game")
        self.current_health -= damage

    def update(self):
        self.state.update()

    def poison(self):
        self._set_state(PoisonedState(self))

    def freeze(self):
        self._set_state(FrozenState(self))

    def berserk(self):
        self._set_state(BerserkState(self))

    def reset(self):
        self._set_state(NormalState(self))

    def __str__(self):
        return f"{self.name} (HP: {self.current_health}/{self.max_health}, AP: {self.current_attack_power}, State: {self.state.get_title()})"

    def _set_state(self, state):
        self.state.exit()
        self.state = state
        self.state.enter()
