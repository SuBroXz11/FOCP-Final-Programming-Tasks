import codecs

def username_exists(username):
    """
    Check if a username exists in the 'passwd.txt' file.

    Parameters:
    - username (str): The username to check for existence.

    Returns:
    bool: True if the username exists, False otherwise.

    The function reads the 'passwd.txt' file, which is assumed to have lines in the
    format 'username:real_name:encoded_password'. It checks if the provided username
    matches any existing usernames in a case-insensitive manner.
    """
    with open('passwd.txt', 'r') as file:
        for line in file:
            existing_username = line.split(':')[0].lower()
            if existing_username == username:
                return True
    return False

def add_user():
    """
    Adds a new user to the 'passwd.txt' file.

    The function prompts the user to enter a new username, checks if it already exists,
    and then collects the user's real name and password. The password is encoded using
    ROT-13 before being stored in the 'passwd.txt' file.

    If the username already exists, the function prints an error message and exits.
    """
    username = input("Enter new username: ").lower()

    # Check if the username already exists
    if username_exists(username):
        print("Cannot add. Most likely username already exists.")
        return

    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    # Use codecs.encode() for ROT-13 encoding
    encoded_password = codecs.encode(password, 'rot_13')

    with open('passwd.txt', 'a') as file:
        file.write(f"{username}:{real_name}:{encoded_password}\n")
    
    print("User Created.")

if __name__ == "__main__":
    add_user()
