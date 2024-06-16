# Importamos las 2 librerías que necesitaremos para este proyecto
import requests
import pyfiglet

# Nos valdremos de Pyfiglet para crear un Banner para nuestro programa
banner = pyfiglet.figlet_format("Russoski Tools \n Directory Enum")
print(banner)

# Creamos una variable en la que preguntar al usuario por un Dominio (ejemplo: youtube.com)
dominio = input("-> Introduce un Dominio para enumerar: ")
print("-> Estamos comprobando todo...")

# La variable Archivo se encargará de almancenar y leer el contenido del diccionario
# La variable Directorios contendrá el contenido de Archivo pero dividido en líneas
archivo = open("common.txt").read()
directorios = archivo.splitlines()

# Iniciamos un bucle For que recorrerá cada línea del diccionario en busca de Directorios válidos
for directorio in directorios:
    # Realizaremos en cada vuelta una petición web con el Dominio que ingrese
    # el usuario y la línea del diccionario correspondiente a dicha vuelta
    linea_enumeracion = f"https://{dominio}/{directorio}" 
    respuesta = requests.get(linea_enumeracion)
    # Si el código de respuesta que arroja la petición es 404 (Not Found), se ignora dicha línea
    if respuesta.status_code==404: 
        pass
    # De lo contrario, significa que el Directorio existe y se mostrará por pantalla
    else:
        print("--------------------------------------------------------------------------")
        print("<MARTA> encontró un Directorio válido: " + linea_enumeracion)
print("--------------------------------------------------------------------------")