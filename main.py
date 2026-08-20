from database.setup import create_tables
from auth.register import register

def main():
    create_tables()

    print("\n===== MINI TORN =====")
    print("1. Register")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        print("Goodbye!")

if __name__ == "__main__":
    main()