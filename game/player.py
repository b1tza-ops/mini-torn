class Player:
    def __init__(
        self,
        player_id,
        user_id,
        name,
        level,
        money,
        health,
        energy,
        strength,
        defence,
        speed,
        dexterity,
        nerve
    ):
        self.id = player_id
        self.user_id = user_id
        self.name = name
        self.level = level
        self.money = money
        self.health = health
        self.energy = energy
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.dexterity = dexterity
        self.nerve = nerve


    def show_stats(self):
        print("\n===== CHARACTER =====")
        print("Name:", self.name)
        print("Level:", self.level)
        print("Money:", self.money)
        print("Energy:", self.energy)
        print("Nerve:", self.nerve)

        print("\n===== BATTLE STATS =====")

        print("Strength:", self.strength)
        print("Defence:", self.defence)
        print("Speed:", self.speed)
        print("Dexterity:", self.dexterity)



