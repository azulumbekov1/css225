class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.stamina = 100
        self.money = 0
        self.skills = {"boxing": 1, "negotiation": 1}

    def train(self):
        if self.stamina > 10:
            self.stamina -= 10
            self.skills["boxing"] += 1
            print(f"{self.name} trains hard. Boxing skill increased to {self.skills['boxing']}.")
        else:
            print(f"{self.name} is too tired to train. Rest to recover stamina.")

    def rest(self):
        self.stamina += 20
        print(f"{self.name} rests and recovers stamina. Stamina is now {self.stamina}.")

    def earn_money(self, amount):
        self.money += amount
        print(f"{self.name} earns ${amount}. Total money is now ${self.money}.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
