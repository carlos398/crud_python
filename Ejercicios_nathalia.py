def area_rectangulo():
    lado1 = int(input("Por favor digite el valor del lado 1: "))
    lado2 = int(input("Por favor digite el valor del lado 2: "))
    
    area = lado1 * lado2
    
    print(area)


def run():
    area_rectangulo()


if __name__ == "__main__":
    run()