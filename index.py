def capturar_datos():
    cedula = int(input("Digite su numero de cedula por favor: "))
    nombres_persona = input("Por favor digite sus nombres: ")
    apellidos_persona = input("Por favor digite sus apellidos: ")
    direccion = input("Por favor digite su direccion: ")
    telefono = int(input("Por favor digite su numero de telefono: "))
    
    return cedula, nombres_persona, apellidos_persona, direccion, telefono


def agregar_persona(cedula, nombres_persona, apellidos_persona, direccion, telefono):
    
    with open("./archivos/datos.txt", "a") as f:
        f.write("{cedula}  {nombres_persona}  {apellidos_persona}  {direccion}  {telefono} ".
                format(
                    cedula=cedula, 
                    nombres_persona=nombres_persona, 
                    apellidos_persona=apellidos_persona,
                    direccion=direccion,
                    telefono=telefono
                    ))


def run():
    cedula, nombres_persona, apellidos_persona, direccion, telefono = capturar_datos()
    agregar_persona(cedula, nombres_persona, apellidos_persona, direccion, telefono)


if __name__ == "__main__":
    run()