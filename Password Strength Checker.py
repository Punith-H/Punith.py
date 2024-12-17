while True:
    check = input("Enter the password: ")

    if len(check) < 8: 
        print("Too short (minimum 8 characters required).")
    elif not any(c.islower() for c in check):  
        print("Needs at least one lowercase letter.") 
    elif not any(c.isupper() for c in check):  
        print("Needs at least one uppercase letter.")  
    elif not any(c.isdigit() for c in check):  
        print("Needs at least one digit.")  
    elif not any(c in '@#$%^&+=' for c in check):  
        print("Needs at least one special character (@#$%^&+=).")  
    else: 
        print("Strong password!")
        break 

print("Access Granted.")
