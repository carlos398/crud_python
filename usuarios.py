def menu():
    print("-"*20+"MENU OPTIONS"+"-"*20)
    print("write 'C' for create a user")
    print("write 'L' for login with your user")
    selection = input("Please write what you want to do: ")
    
    return selection


def user_data():
    name = input("write your name here please: ")
    email = input("write your email here please: ")
    password = input("write your password here: ")

    return name, email, password


def create_user(name, email, password):
    with open("./archivos/usuarios.txt", "a") as f:
        f.write(" name: {name} email: {email} password: {password} ".format(
            name=name,
            email=email,
            password=password
            ) + '\n')


def user_search():
    users = []
    passwords = []
    with open("./archivos/usuarios.txt", "r") as f:
        for user in f:
            user_name = user[user.index("email:")+7:user.index("password:")-1:]
            user_name = user_name.strip()
            password = user[user.index("password:")+10:]
            password = password.strip()
            users.append(user_name)
            passwords.append(password)
            
        return users, passwords


def login(users, passwords):
    print("remember your email is your user")
    login_user = input("please write here your user: ")
    login_password = input("please write your password here: ")
    
    for i in range(len(users)):
        if login_user == str(users[i]) and login_password == str(passwords[i]):
            print("bienvenido ")
            break
        else:
            continue
            
            
def run():
    selection = menu()
    selection = selection.upper()
    
    if selection == "C":
        name, email, password = user_data()
        create_user(name, email, password)
    elif selection == "L":
        user_name, password = user_search()
        login(user_name, password)


if __name__ == '__main__':
    run()