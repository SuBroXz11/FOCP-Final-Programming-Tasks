import getpass
import codecs

def change_password():
    """
    This function prompts the user for a username and the current password, reads a file containing username-password pairs,
    and allows the user to change their password. It then updates the password file accordingly and prints a message indicating the status of the operation.
    """

    # Prompt user for username and current password
    username = input("User: ").lower()
    current_password = getpass.getpass("Current Password: ")

    # Read all lines from the password file
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    # Open the password file in write mode
    with open('passwd.txt', 'w') as file:
        password_changed = False

        # Iterate through each line in the file
        for line in lines:
            parts = line.strip().split(':')

            # Check if the username and current password match the stored credentials
            if parts[0] == username and parts[2] == codecs.encode(current_password, 'rot_13'):
                # Prompt user for new password and confirmation
                new_password = input("New Password: ")
                confirm_password = input("Confirm: ")

                # Check if the new password and confirmation match
                if new_password == confirm_password:
                    # Update the line with the new encoded password
                    line = f"{parts[0]}:{parts[1]}:{codecs.encode(new_password, 'rot_13')}\n"
                    password_changed = True
                    print("Password changed.")
                else:
                    print("Passwords do not match. Nothing changed.")
            
            # Write the line back to the file
            file.write(line)

        # Print appropriate message based on whether the password was changed or not
        if not password_changed:
            print("User not found or current password is invalid. Nothing changed.")

if __name__ == "__main__":
    change_password()
