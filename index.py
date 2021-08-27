def opciones():
    
    """
    Esta funcion solicita que se ingrese la opcion de lo que la persona desea hacer
    """
    
    print("Digite la letra segun lo que desee hacer: ")
    print("M = MOSTRAR TODOS LOS REGISTROS ")
    print("C = CREAR PERSONA ")
    print("B = BUSCAR PERSONA ")
    print("E = ELIMINAR PERSONA ")
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
                    )+"\n")
        

def mostrar_personas():
    
    """
        esta funcion muestra todos los registros de la tabla
    """        
    
    with open("./archivos/datos.txt", "r") as f:
        for persona in f:
            print (" {persona} ".format(persona=persona))
            

def buscar_persona():
    
    """
        esta funcion busca a una persona exacta en el programa
    """        
    
    busqueda = input("Digite la cedula de la persona: ")
    with open("./archivos/datos.txt", "r") as f:
        for persona in f:
            patron_de_busqueda = persona[:10]
            if patron_de_busqueda == busqueda:
                print (persona)
                break
            else:
                continue
            

def eliminar_persona():
    
    """
        esta funcion busca a una persona exacta en el programa
    """        
    
    personas = []
    busqueda = input("Digite la cedula de la persona que desea eliminar: ")
    
    with open("./archivos/datos.txt", "r+") as f:
        for datos in f:
            personas.append(datos)
            
        for indice_personas in  range(len(personas)):
            persona = personas[indice_personas]
            patron_de_busqueda = persona[:10]
            
            if patron_de_busqueda == busqueda:
                print("El usuario que desea eliminar es: ")
                print (" {persona} ".format(persona=persona))
                eliminar = input("Si desea eliminarlo escriba S de lo contrario ponga N: ")
                eliminar = eliminar.upper()
                
                if eliminar == "S":
                    personas.pop(indice_personas)
                    print(personas)
                    break
            else:
                continue
            
        with open("./archivos/datos.txt", "w") as data:
            for datos_personas in personas:
                    data.write("{datos_personas} ".format(datos_personas=datos_personas)+"\n")
            

def run():
    
    opcion = opciones()
    
    if opcion == "M":
        mostrar_personas()
    elif opcion == "C":
        cedula, nombres_persona, apellidos_persona, direccion, telefono = validador_campos()
        agregar_persona(cedula, nombres_persona, apellidos_persona, direccion, telefono)
    elif opcion == "B":
        buscar_persona()
    elif opcion == "E":
        eliminar_persona()

if __name__ == "__main__":
    run()