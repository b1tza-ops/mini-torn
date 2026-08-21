import random
from game.progression import award_xp


def crimes_menu(player):
    while True:
        print("\n===== CRIMES =====")
        print("Nerve:", player.nerve)

        print("\n1. Shoplift in Camden")
        print("2. Pickpocket in Soho")
        print("3. Break into a flat in Hackney")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            commit_crime(
                player,
                name="Shoplift in Camden",
                nerve_cost=2,
                success_chance=80,
                min_reward=20,
                max_reward=60,
                xp_reward=10,
            )

        elif choice == "2":
            commit_crime(
                player,
                name="Pickpocket in Soho",
                nerve_cost=4,
                success_chance=65,
                min_reward=50,
                max_reward=150,
                xp_reward=25,
            )

        elif choice == "3":
            commit_crime(
                player,
                name="Break into a flat in Hackney",
                nerve_cost=8,
                success_chance=40,
                min_reward=200,
                max_reward=600,
                xp_reward=60
            )

        elif choice == "4":
            break

        else:
            print("Invalid option.")


def commit_crime(
    player,
    name,
    nerve_cost,
    success_chance,
    xp_reward,
    min_reward,
    max_reward
):
    if player.nerve < nerve_cost:
        print("\nNot enough nerve.")
        return

    player.nerve -= nerve_cost

    roll = random.randint(1, 100)

    print("\nAttempting:", name)

    if roll <= success_chance:
        reward = random.randint(min_reward, max_reward)

        player.money += reward
        levels_gained = award_xp(player, xp_reward)

        print("Crime successful!")
        print("You made £", reward)
        print("XP +", xp_reward)

        if levels_gained > 0:
            print(
                f"Level up! You are now level {player.level}."
            )

    else:
        damage = random.randint(5, 15)
        player.health = max(0, player.health - damage)

        print("Crime Failed!")
        print("You lost", damage, "health")
