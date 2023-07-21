arreglo = [] 

class alumnos:
    def __init__(self):
        self.matricula = ()
        self.nombre = ()
        self.edad = ()
        self.carrera = () 

def Menu():
    
    opc = 0
    while opc!= 4:

        print("\n \t --- Bienvenidos al sistema de registro --- ")
        print("UIP")
        print(" ------------------- ")
        print("1. Registrar estudiantes")
        print("2. Registro de estudiantes") 
        print("3. Buscar estudiante")
        print("4. Salir") 
        opc = int(input("\nEliga una opcion: "))

        if opc == 1:
            registrar()
        elif opc == 2:
            Listar()
        elif opc == 3:
            Buscar()
        elif opc == 4: 
            Salir() 

#Funciones
def registrar():
    print("\n --- Registritar estudiantes --- ")
    alumno = alumnos()
    alumno.matricula = input("\nIngrese la matricula del estudiante: ")
    alumno.nombre = input("Nombre del estudiante: ") 
    alumno.edad = int(input("Edad del estudiante: "))
    alumno.carrera = input("Carrera del estudiante: ")
    arreglo.append(alumno)

def Listar():
    print("\n --- Mostar estudiantes ---- ")
    for alumno in arreglo: 
        print("\nNombre:",alumno.nombre)
        print("Edad:",alumno.edad)
        print("Carrera:",alumno.carrera)     


def Buscar():
    print("\n --- Buscar estudiante --- ")
    name = input("\nNombre del estudiante: ") 
    for alumno in arreglo:
        if alumno.nombre == name: 
            print("\nNombre:",alumno.nombre)
            print("edad:",alumno.edad)
            print("Carrera:",alumno.carrera)  

def Salir():
    print("\n Vuelva pronto ") 
#.......................................................

Menu()   





    

