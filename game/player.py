class Player:
    def __init__(
        self,
        player_id,
        name,
        level=1,
        money=500,
        health=100,
        energy=100,
        strength=10,
        defence=10,
        speed=10,
        dexterity=10
    ):
        self.id = player_id
        self.name = name
        self.level = level
        self.money = money
        self.health = health
        self.energy = energy
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.dexterity = dexterity

    def show_stats(self):
        print("\n===== PLAYER =====")
        print("Name:", self.name)
        print("Level:", self.level)
        print("Money: £", self.money)
        print("Health:", self.health)
        print("Energy:", self.energy)

        print("\n===== BATTLE STATS =====")
        print("Strength:", self.strength)
        print("Defence:", self.defence)
        print("Speed:", self.speed)
        print("Dexterity:", self.dexterity)