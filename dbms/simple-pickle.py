import pickle


def login():
    # get user credentials and validate them
    username = input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "password":
        # create a session dictionary to store user data
        session = {"username": username, "logged_in": True}
        # serialize and save the session to a file
        with open("session.pickle", "wb") as f:
            pickle.dump(session, f)
        print("Login successful.")
    else:
        print("Invalid credentials.")

def logout():
    # deserialize and load the session from file
    with open("session.pickle", "rb") as f:
        session = pickle.load(f)
    # update the session to reflect logout
    session["logged_in"] = False
    # serialize and save the updated session to file
    with open("session.pickle", "wb") as f:
        pickle.dump(session, f)
    print("Logout successful.")

def main():
    # load the session from file
    try:
        with open("session.pickle", "rb") as f:
            session = pickle.load(f)
    except FileNotFoundError:
        session = {"username": None, "logged_in": False}

    # display appropriate menu based on session state
    if session["logged_in"]:
        print(f"Welcome back, {session['username']}!")
        choice = input("1. Logout\n2. Exit\n")
        if choice == "1":
            logout()
        elif choice == "2":
            exit()
        else:
            print("Invalid choice.")
    else:
        print("Welcome to the program!")
        choice = input("1. Login\n2. Exit\n")
        if choice == "1":
            login()
        elif choice == "2":
            exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
