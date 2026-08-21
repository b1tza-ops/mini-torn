from database.setup import create_tables
from auth.register import register
from auth.login import login
from database.players import create_player, get_player_by_user_id, save_player
from database.players import save_player
from game.player import Player
from game.gym  import gym_menu
from game.crimes import crimes_menu

def main():
    create_tables()
    while True: 
        print("\n===== MINI TORN =====")
        print("1. Login")
        print("2. Register")
        print("3. Forgot Password")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            user_id = login()

            if user_id:
                player = load_or_create_player(user_id)
                game_menu(player)

        elif choice == "2":
            register()

        elif choice == "3":
            print("Forgot password coming next")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

def game_menu(player):

    while True:
        print("\n===== GAME MENU =====")
        print("1. Character")
        print("2. Gym")
        print("3. Crimes")
        print("4. Jobs")
        print("5. Inventory")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == "1":
            player.show_stats()

        elif choice == "2":
            gym_menu(player)
            save_player(player)

        elif choice == "3":
            crimes_menu(player)
            save_player(player)
            
        elif choice == "4":
            print("Jobs coming soon.")

        elif choice == "5":
            print("Inventory coming soon.")

        elif choice == "6":
            save_player(player)
            print("Player Saved")
            print("Logged out.")
            break

        else:
            print("Invalid option.")

def load_or_create_player(user_id):
    player_data = get_player_by_user_id(user_id)

    if player_data is None:
        print("\nYou do not have a character yet.")

        name = input("Choose your character name: ").strip()

        create_player(user_id, name)

        player_data = get_player_by_user_id(user_id)

        print("\nCharacter created!")

    return Player(*player_data)

if __name__ == "__main__":
    main()

