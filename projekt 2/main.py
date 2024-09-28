from auth import Auth
from admin import Admin
from user import User
from data_manager import DataManager

def main():
    auth = Auth("users.json")

    username = input("Podaj login: ")
    password = input("Podaj hasło: ")
    user = auth.login(username, password)

    if user:
        print(f"Zalogowano jako {user['role']}")
        if user['role'] == "admin":
            admin_panel(auth)
    else:
        print("Błędny login lub hasło")

def admin_panel(auth):
    admin = Admin("admin", "admin123")
    while True:
        print("1. Zmień dane użytkownika")
        print("2. Wyjdź")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            username = input("Podaj nazwę użytkownika do zmiany: ")
            new_data = {
                "username": input("Nowa nazwa użytkownika: "),
                "password": input("Nowe hasło: ")
            }
            if admin.change_user_data(auth.users, username, new_data):
                auth.data_manager.save_data(auth.users)
                print("Dane zmienione!")
            else:
                print("Nie znaleziono użytkownika.")
        elif choice == "2":
            break

if __name__ == "__main__":
    main()
