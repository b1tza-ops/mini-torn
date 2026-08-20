from database.setup import create_tables
from auth.register import register
from auth.login import login

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
                game_menu(user_id)
                
        elif choice == "2":
            register()

        elif choice == "3":
            print("Forgot password coming next")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

def game_menu(user_id):

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
            print("Character coming soon.")

        elif choice == "2":
            print("Gym coming soon.")

        elif choice == "3":
            print("Crimes coming soon.")

        elif choice == "4":
            print("Jobs coming soon.")

        elif choice == "5":
            print("Inventory coming soon.")

        elif choice == "6":
            print("Logged out.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

