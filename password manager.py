passwords = {}  # Dictionary to store account-password pairs

while True:
    print("\nMenu:")
    print("1. Add a new account and password")
    print("2. Retrieve a password")
    print("3. Show all accounts")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        account = input("Enter the account name: ").strip()
        if account in passwords:
            print("Account already exists!")
        else:
            password = input("Enter the password: ").strip()
            passwords[account] = password
            print(f"Password for '{account}' added successfully!")

    elif choice == "2":
        account = input("Enter the account name: ").strip()
        if account in passwords:
            print(f"Password for '{account}': {passwords[account]}")
        else:
            print("Account not found!")

    elif choice == "3":
        if passwords:
            print("Stored accounts:")
            for account in passwords:
                print(f"- {account}")
        else:
            print("No accounts stored yet.")

    elif choice == "4":
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
