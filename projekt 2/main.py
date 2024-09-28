import json

def load_data():
    try:
        with open("users.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("users.json", 'w') as file:
        json.dump(data, file, indent=4)

def login(users, username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

def admin_panel(users):
    while True:
        print("1. Zmień dane użytkownika")
        print("2. Wyjdź")
        choice = input("Wybierz opcję: ")
        if choice == "1":
            username = input("Podaj nazwę użytkownika do zmiany: ")
            new_username = input("Nowa nazwa użytkownika: ")
            new_password = input("Nowe hasło: ")
            for user in users:
                if user['username'] == username:
                    user['username'] = new_username
                    user['password'] = new_password
                    save_data(users)
                    print("Dane zmienione!")
                    break
            else:
                print("Nie znaleziono użytkownika.")
        elif choice == "2":
            break

def main():
    users = load_data()
    username = input("Podaj login: ")
    password = input("Podaj hasło: ")
    user = login(users, username, password)

    if user:
        print(f"Zalogowano jako {user['role']}")
        if user['role'] == "admin":
            admin_panel(users)
    else:
        print("Błędny login lub hasło")

if __name__ == "__main__":
    main()
