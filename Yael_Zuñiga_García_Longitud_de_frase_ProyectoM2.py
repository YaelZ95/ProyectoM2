#Inicializacion de variables
palabra = "" 
es_correcto = False #Se usa para indicar al programa que la palabra es correcta

#El programa se seguirá ejecutando mientras la palabra sea incorrecta
while es_correcto is False:
    
    #Pide al usuario ingresar una palabra
    palabra = input("Ingresa una palabra que contenga entre 4 a 8 letras\n")

    #Si la palabra está dentro del rango de 4 a 8 letras
    if len(palabra) >= 4 and len(palabra) <= 8:
        #Se marca como correcta y se cierra el programa
        print("La palabra es correcta")
        es_correcto = True
        break
    
    #Si la palabra tiene menos de 4 letras
    elif len(palabra) < 4:
        #Se imprime el aviso de que faltan letras y muestra cuantas letras tiene la palabra
        #Despues prosigue el bucle para preguntar de nuevo por la palabra
        print("Hacen falta letras, solo tiene "+str(len(palabra))+" letras")
    
    #Si la palabra tiene mas de 8 letras
    elif len(palabra) > 8:
        #Se imprime el aviso de que sobran letras y muestra cuantas letras tiene la palabra
        #Despues prosigue el bucle para preguntar de nuevo por la palabra
        print("Sobran letras, tiene "+str(len(palabra))+" letras")