import codecs
import getpass


def login():
    """
    This function prompts the user for a username and password, reads a file containing username-password pairs,
    and checks if the entered credentials match any in the file. If a match is found, access is granted else access is denied.
    """
    # Prompt user for username and password
    username = input("User: ").lower() # .lower method to ensure proper value
    password = getpass.getpass("Password: ") # Hide password input

    with open('passwd.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            # Decode the stored password using ROT13
            decoded_password = codecs.decode(parts[2], 'rot_13')
            # Check if the entered username and decoded password match the stored credentials
            if parts[0] == username and decoded_password == password:
                print("Access granted.")
                return

    print("Access denied.")

if __name__ == "__main__":
    login()
