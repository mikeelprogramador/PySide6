class Empresa:
    def __init__(self):
        self.nombreEmpresa = input("Empresa \n")
        self.valorFactura()

    def valorFactura(self):
        while True:
            try:
                self.valor = float(input("Valor de la factura \n"))
                break
            except ValueError:
                print("El dato que ingreaste es invalido")



def saveData():
    baseDatos = Empresa()
    datosFactura = vars(baseDatos)
    save = ""
    archivo = open('database.txt', 'a')
    for clave, valor in datosFactura.items():
        save += f"{clave}: {valor} , "
    save = save[:-2]
    archivo.write(f" {save}\n")
    return "Los datos se Guardaron correctamente"

def idAutoIncrement():
    archivo = open('database.txt', 'r')
    lineas = archivo.readlines() 
    archivo.close()  
    
    if lineas:
        id = int(lineas[-1].split(',')[0].split(':')[1].strip()) 
        id += 1  
    else:
        id = 0  
    
    archivo = open('database.txt', 'a')
    archivo.write(f"ID: {id} ,")  
    archivo.close()  


def menu():
    idAutoIncrement()
    saveData()

menu()