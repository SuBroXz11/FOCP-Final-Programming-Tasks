# main.py
# Function imports from external modules
from adduser import add_user
from deluser import delete_user
from passwd import change_password
from login import login

def main():
    """
    Main function is an user management program.

    This function presents a menu to the user with options to perform various user-related actions:
    1. Add User
    2. Delete User
    3. Change Password
    4. Login
    5. Quit

    The function enters into a loop, repeatedly prompting the user for their choice and executing
    the corresponding action based on the selected option. The loop continues until the user chooses
    to exit the program.

    Options:
    - 1: Calls the add_user() function to add a new user.
    - 2: Calls the delete_user() function to delete an existing user.
    - 3: Calls the change_password() function to modify a user's password.
    - 4: Calls the login() function for user login.
    - 5: Exits the program.

    Returns:
    None
    """
    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. Login")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            change_password()
        elif choice == "4":
            login()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# This conditional statement checks whether the current script is the main program
# and not being imported as a module. If it is the main program, it calls the
# main() function, providing a clear entry point for execution.
if __name__ == "__main__":
    main()
