def gym_menu(player):
    while True:
        print("\n===== GYM =====")
        print("Energy:", player.energy)

        print("\n1. Train Strength")
        print("2. Train Defence")
        print("3. Train Speed")
        print("4. Train Dexterity")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            train(player, "strength")

        elif choice == "2":
            train(player, "defence")

        elif choice == "3":
            train(player, "speed")

        elif choice == "4":
            train(player, "dexterity")

        elif choice == "5":
            break

        else:
            print("Invalid option.")

def train(player, stat):
    energy_cost = 10
    stat_gain = 2

    if player.energy < energy_cost:
        print("Not enough energy.")
        return
    
    player.energy -= energy_cost

    if stat == "strength":
        player.strength += stat_gain

    elif stat == "defence":
        player.defence += stat_gain

    elif stat == "speed":
        player.speed += stat_gain

    elif stat == "dexterity":
        player.dexterity += stat_gain

    else:
        raise ValueError(f"Unknown battle stat: {stat}")

    print("\nTraining complete!")
    print(stat.capitalize(), "+", stat_gain)
    print("Energy -", energy_cost)
