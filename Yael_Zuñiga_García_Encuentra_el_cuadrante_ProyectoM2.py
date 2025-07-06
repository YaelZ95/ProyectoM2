#Declaracion de variables
coordenada = {
    "X": 0,
    "Y": 0
}

direccion = ["derecha", "arriba"] #Apoyo para definir el cuadrante donde se ubican las coordenadas
es_valido = False #Verificador de datos validos


#Mientras el dato no es valido preguntará de nuevo por el valor de la coordenada
while es_valido is False:

    #Pide al usuario el valor de la coordenada X
    coordenada["X"] = input("Ingrese el valor de la coordenada X\n")
    
    #Verifica si la coordenada es un numero
    try: 
        float(coordenada["X"])
    except:
        #Si no es un numero, se vuelve a preguntar por el valor de la coordenada
        print("La coordenada debe ser un numero positivo o negativo")
        continue

    #Verifica si la coordenada no es 0
    if float(coordenada["X"]) > 0 or float(coordenada["X"]) < 0:
        es_valido = True
        break
    else:
        #Si es 0, imprime un aviso de error y vuelve a preguntar por el valor de la coordenada
        print("No se puede ubicar un cuadrante si el valor de la coordenada es 0")

#Resetea el verificador para las comprobaciones de la proxima coordenada
es_valido = False

#Repite las verificaciones pero ahora para la Coordenada Y
while es_valido is False:

    #Pide al usuario el valor de la coordenada Y
    coordenada["Y"] = input("Ingrese el valor de la coordenada Y\n")

    #Verifica si la coordenada es un numero
    try: 
        float(coordenada["Y"])
    except:
        #Si no es un numero, se vuelve a preguntar por el valor de la coordenada
        print("La coordenada debe ser un numero positivo o negativo")
        continue

    #Verifica si la coordenada no es 0
    if float(coordenada["Y"]) > 0 or float(coordenada["Y"]):
        es_valido = True
        break
    else:
        #Si es 0, imprime un aviso de error y vuelve a preguntar por el valor de la coordenada
        print("No se puede ubicar un cuadrante si el valor de la coordenada es 0")
    
#Si el valor de la coordenada X es positivo quiere decir que el cuadrante está a la derecha
if float(coordenada["X"]) > 0:
    direccion[0] = "derecha"
else: #De lo contrario, está a la izquierda
    direccion[0] = "izquierda"

#Si el valor de la coordenada Y es positivo quiere decir que el cuadrante está arriba
if float(coordenada["Y"]) > 0:
    direccion[1] = "arriba"
else: #De lo contrario, está abajo
    direccion[1] = "abajo"

#Con las direcciones comprueba en que cuadrante se ubica las coordenadas
if direccion[0] == "derecha" and direccion[1] == "arriba": #Derecha y arriba = Cuadrante 1
    print("Las coordenadas se encuentran en el cuadrante I")
elif direccion[0] == "izquierda" and direccion[1] == "arriba": #Izquierda y Arriba = Cuadrante 2
    print("Las coordenadas se encuentran en el cuadrante II")
elif direccion[0] == "izquierda" and direccion[1] == "abajo": #Izquierda y Abajo = Cuadrante 3
    print("Las coordenadas se encuentran en el cuadrante III")
elif direccion[0] == "derecha" and direccion[1] == "abajo": #Derecha y Abajo = Cuadrante 4
    print("Las coordenadas se encuentran en el cuadrante IV")