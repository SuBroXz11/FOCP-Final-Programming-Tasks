def delete_user():
    """
    This function prompts the user to enter a username, reads a file containing username-password pairs,
    and deletes the specified user's credentials if found. It then prints a message indicating the status of the operation.
    """

    # Prompt user for the username to be deleted
    username = input("Enter username: ").lower()

    # Read all lines from the password file
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()

    # Open the password file in write mode
    with open('passwd.txt', 'w') as file:
        user_deleted = False

        # Iterate through each line in the file
        for line in lines:
            # Check if the line does not start with the specified username
            if not line.startswith(username + ':'):
                # Write the line back to the file (keeping lines that do not match the specified username)
                file.write(line)
            else:
                # Mark the user as deleted
                user_deleted = True

        # Print appropriate message based on whether the user was deleted or not
        if user_deleted:
            print("User Deleted.")
        else:
            print("User not found. Nothing changed.")
