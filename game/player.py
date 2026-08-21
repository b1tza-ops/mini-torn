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
        nerve,
        max_energy,
        max_nerve,
        last_energy_update,
        last_nerve_update
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
        self.max_energy = max_energy
        self.max_nerve = max_nerve
        self.last_energy_update = last_energy_update
        self.last_nerve_update = last_nerve_update



    def show_stats(self):
        print("\n===== CHARACTER =====")
        print("Name:", self.name)
        print("Level:", self.level)
        print("Money:", self.money)
        print("Health: ", self.health)
        print(f"Energy: {self.energy}/{self.max_energy}")
        print(f"Nerve: {self.nerve}/{self.max_nerve}")
        print("\n===== BATTLE STATS =====")

        print("Strength:", self.strength)
        print("Defence:", self.defence)
        print("Speed:", self.speed)
        print("Dexterity:", self.dexterity)



