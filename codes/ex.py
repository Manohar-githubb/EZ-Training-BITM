#Write a program in which to built login system using functions. The function name shud be login and register first it shud ask user to enter the details for registration and out of all these details user name and password shud be stored.
#Now this func shud ask user to enter username and password.if these match with register details login success otherwise repeat the login process saying that enter again until correct.

# d = {}
# def login_and_registration():
#     user_name = input("Enter username: ")
#     password = input("Enter the password: ")
# login_and_registration()

def register(user_db):
    print("Registration:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_db[username] = password
    print("Registration successful!")

def login(user_db):
    while True:
        print("Login:")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in user_db and user_db[username] == password:
            print("Login successful!")
            break
        else:
            print("Incorrect username or password. Please try again.")

def main():
    user_db = {}
    register(user_db)
    login(user_db)

if __name__ == "__main__":
    main()
