def opciones():
    
    """
    Esta funcion solicita que se ingrese la opcion de lo que la persona desea hacer
    """
    
    print("Digite la letra segun lo que desee hacer: ")
    print("M = MOSTRAR TODOS LOS REGISTROS ")
    print("C = CREAR PERSONA ")
    opcion = input("por favor digitw su opcion: ")
    opcion = opcion.upper()
    
    return opcion


def capturar_datos():
    
    """
    Esta funcion captura los datos solicitados para almacenar en el archivo de texto
    """
    
    cedula = input("Digite su numero de cedula por favor: ")
    nombres_persona = input("Por favor digite sus nombres: ")
    apellidos_persona = input("Por favor digite sus apellidos: ")
    direccion = input("Por favor digite su direccion: ")
    telefono = input("Por favor digite su numero de telefono: ")
    
    return cedula, nombres_persona, apellidos_persona, direccion, telefono


def validador_campos():
    
    """
    Esta funcion valida que los campos no esten vacios y solicita que se ingrese un dato
    """
    
    cedula, nombres_persona, apellidos_persona, direccion, telefono = capturar_datos()
    while cedula == "":
        cedula = input("Digite su numero de cedula por favor: ")
    while nombres_persona == "":
        nombres_persona = input("Por favor digite sus nombres: ")
    while apellidos_persona == "":
        apellidos_persona = input("Por favor digite sus apellidos: ")
    while direccion == "":
        direccion = input("Por favor digite su direccion: ")
    while telefono == "":
        telefono = input("Por favor digite su numero de telefono: ")
    
    return cedula, nombres_persona, apellidos_persona, direccion, telefono
    
    
def agregar_persona(cedula, nombres_persona, apellidos_persona, direccion, telefono):
    
    """
    funcion que inserta los datos capturados en un archivo de texto
    """
    with open("./archivos/datos.txt", "a") as f:
        f.write("{cedula}  {nombres_persona}  {apellidos_persona}  {direccion}  {telefono} ".
                format(
                    cedula=cedula, 
                    nombres_persona=nombres_persona, 
                    apellidos_persona=apellidos_persona,
                    direccion=direccion,
                    telefono=telefono
                    ))
        f.write("\n")
        

def mostrar_personas():
    
    """
        esta funcion muestra todos los registros de la tabla
    """        
    with open("./archivos/datos.txt", "r") as f:
        for persona in f:
            print (" {persona} ".format(persona=persona))


def run():
    
    opcion = opciones()
    
    if opcion == "M":
        mostrar_personas()
    elif opcion == "C":
        cedula, nombres_persona, apellidos_persona, direccion, telefono = validador_campos()
        agregar_persona(cedula, nombres_persona, apellidos_persona, direccion, telefono)


if __name__ == "__main__":
    run()