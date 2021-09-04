def user_data():
    name = input("write you'r name here please: ")
    email = input("write you'r email here please: ")
    password = input("write you'r password here: ")

    return name, email, password

def write_data_function(name, email, password):
    with open("./archivos/usuarios.txt", "a") as f:
        f.write(" name: {name} email: {email} password: {password} ".format(
            name=name,
            email=email,
            password=password
            ) + '\n')


def login():
    with open("./archivos/usuarios.txt", "r") as f:
        for usuario in f:
            user_name = usuario[usuario.index("email:")+7:usuario.index("password:")-1:]
            password = usuario[usuario.index("password:")+10:]
            password = password.strip()
            print(user_name)
            

def run():
    login()

if __name__ == '__main__':
    run()