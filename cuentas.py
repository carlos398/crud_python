def calculadora():
    total_descuentos = 0
    nombre_usuario = input('por favor digite su nombre: ')
    print('bienvenido {} '.format(nombre_usuario))
    
    salario = int(input('Digite cual es su salario mensual: '))
    pregunta = input('Desea hacer un descuento? S/n : ')
    pregunta = pregunta.upper()
    nombre_devengos = []
    dinero_devengo = []
    
    while pregunta == 'S':
        nombre = input('Que nombre lleva este descuento?: ')
        cantidad = int(input('Cuanto dinero debe descontarse?: '))
        nombre_devengos.append(nombre)
        dinero_devengo.append(cantidad)
        total_descuentos = total_descuentos + cantidad
        salario = salario - cantidad
        
        print('Se han descontado {} como gasto de {} a su salario'.format(cantidad,nombre))
        print('Su salario actual es {salario}'.format(salario=salario))
        
        pregunta = input('Desea hacer otro descuento? S/N : ')
        pregunta = pregunta.upper()
        
    print('Gracias por usar nuestra calculadora de devengos =D ')
    print('\n'+'\n'+'\n'+'*'*30 + 'Ticket' + '*'*30)
    
    for i in range(len(nombre_devengos)):
        print('| se descontaron.... {dinero} que se gastaran en.... {nombre} '.format(
            dinero=dinero_devengo[i],
            nombre=nombre_devengos[i]
            ))
        
    print('\n se descontaron en total.... {total_descuentos} \n su salario actual es.... {salario} '.format(
            total_descuentos=total_descuentos,
            salario=salario
        ))
    
    print('*'*30 + 'Ticket' + '*'*30)


def run():
    calculadora()


if __name__ == '__main__':
    run()