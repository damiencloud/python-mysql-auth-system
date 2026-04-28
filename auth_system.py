import pymysql

def connect_db():
    try:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="*********",
            database="user_auth_db"
        )
    except Exception as e:
        print("\nError: Unable to connect to the database.")
        print(e)
        return None


def register():
    print("\nCreate a New Account ")

    conn = connect_db()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if not username or not email or not password:
            print("All fields are required. Please try again.")
            return

        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        conn.commit()

        print("Account created successfully. You can now log in.")

    except pymysql.err.IntegrityError:
        print("This email is already registered. Try logging in instead.")
    except Exception as e:
        print("Something went wrong:", e)
    finally:
        conn.close()


def login():
    print("\n Login ")

    conn = connect_db()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        email = input("Enter email: ")
        password = input("Enter password: ")

        query = "SELECT username FROM users WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))

        result = cursor.fetchone()

        if result:
            print(f"Welcome, {result[0]}. Login successful.")
        else:
            print("Invalid email or password. Please try again.")

    except Exception as e:
        print("Error during login:", e)
    finally:
        conn.close()


def main():
    while True:
        print("\n==============================")
        print("       USER AUTH SYSTEM")
        print("==============================")
        print("1. Register (Sign Up)")
        print("2. Login (Sign In)")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()