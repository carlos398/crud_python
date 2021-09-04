def user_data():
    name = input("write your name here please: ")
    email = input("write your email here please: ")
    password = input("write your password here: ")

    return name, email, password

def write_data_function(name, email, password):
    with open("./archivos/usuarios.txt", "a") as f:
        f.write(" name: {name} email: {email} password: {password} ".format(
            name=name,
            email=email,
            password=password
            ) + '\n')


def user_search():
    with open("./archivos/usuarios.txt", "r") as f:
        for user in f:
            user_name = user[user.index("email:")+7:user.index("password:")-1:]
            user_name = user_name.strip()
            password = user[user.index("password:")+10:]
            password = password.strip()
            
            return user_name, password


def login(user, password):
    print("remember your email is your user")
    login_user = input("please write here your user: ")
    login_password = input("please write your password here: ")
    
    if login_user == user and login_password == password:
        print("bienvenido ")
    else:
        print("wrong username or password")


def run():
    user_name, password = user_search()
    login(user_name, password)


if __name__ == '__main__':
    run()