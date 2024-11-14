with open('database.txt', 'r') as archivo:
    contenido = archivo.read()  # Lee todo el archivo
    print(len(contenido))  # Muestra el contenido del archivo
    print(contenido[:-1])  # Muestra el contenido del archivo