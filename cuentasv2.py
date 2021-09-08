def data():
    discounts = []
    salary = int(input("Digite la cantidad de dinero que tiene: "))
    question = input("desea realizar un descuento a su salario? S/N: ").upper()
    while question == 'S':
        discount = int(input("Digite la cantidad que sera descotada: "))
        discounts.append(discount)
        salary = salary - discount
        question = input("desea realizar otro a su salario? S/N: ").upper()


def run():
    data()


if __name__ == '__main__':
    run()