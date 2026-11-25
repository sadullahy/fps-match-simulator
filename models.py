class Weapon:
    def __init__(self, name, cost, damage):
        self.name = name
        self.cost = cost
        self.damage = damage


class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.money = 800
        self.weapon = Weapon("Glock/Classic", 0, 25)

    def buy_weapon(self, weapon):
        if self.money >= weapon.cost:
            self.money -= weapon.cost
            self.weapon = weapon
            return True
        return False