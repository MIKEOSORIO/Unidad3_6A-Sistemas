import re
from colorama import init, Fore

print("Elige el caso \n" + "CASO 1: 2 símbolos aritméticos con diferente prioridad.\n" +
                           "CASO 2: 3 símbolos aritméticos con diferente prioridad.\n" +
                           "CASO 3: 2 símbolos aritméticos con paréntesis\n" +
                           "CASO 4: 3 Símbolos aritméticos con paréntesis\n" +
                           "CASO 5: Al menos 2 símbolos aritméticos con anidamiento de paréntesis\n")

x=int(input("Seleccione una opcion: "))

class LeeTxt:
        print(
            Fore.CYAN + "-----------------------------INICIO LECTURA DEL ARCHIVO .TXT-----------------------------------------")
        with open('./Prueba.txt') as file_object:
            global contents
            contents = file_object.read()
            print(Fore.GREEN + "                                      " + contents)
        print(
            Fore.CYAN + "-----------------------------FIN DE LECTURA DEL ARCHIVO .TXT-----------------------------------------")

def Inicio():

    print(Fore.RED + "-----------------------------INICIO DE CÓDIGO INTERMEDIO-----------------------------\n")

def Fin():
    print(Fore.RED + "\n-----------------------------FIN DE CÓDIGO INTERMEDIO-----------------------------")

    # LOS CASOS SON SIN CORCHETES  SOLO SON LISTAS, SOLO SE TRABAJA SOLO CON UN DIGITO Y 
#CARACTER
#========================================================================================================
if x==1:
    #CASO UNO SIN USO DE CORCHETES, CON LISTAS.
    lectura = LeeTxt()
    p = []
    vs = []
    valor = contents
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]  #LA EN LA LISTA SOLO SE DESGLOSA LA EXPRESION POR PARRES 
            p.remove(p[suma]) # SE ELIMINA "*" PARA QUE PUEDA CONTINUAR CON LA SIGUIENTE FUNCION 
            p.remove(p[suma-1]) #SE ELIMINA EL "5" CONTINUAA CON LA EJECUCION
            p.remove(p[suma-1]) #SE ELIMINA EL "Y" Y TERMINA ELIMINDO EL ULTIMO PARA QUE TERMINE EL PROCESO DE TEMPORAL 0
    inicio = Inicio()

    espacio = "                                    "
    print(Fore.MAGENTA + espacio + temporalCero)
    temporalUno = ""    # EN ESTE PARTE RESULEVE LO QUE ES EL TEMPORAL 1 LA CUAL ES AL CONTINUACION DE LA SIGUIENTE OPERACION
    for i in p:
        if i == "+" or i == "-": # SUMA O RESTA 
            if p[-1] == "+" or p[-1]=="-":
                temporalUno = "_t1 ="+ p[0] + " "+ p[-1] + " " +"_t0"
                # EN ESTE PARTE LO QUE HACE EL TEMPORAL 1 ES LEER EL CARACTER QUE TIENE QUE EJECUTAR Y DESPUES SE LE IMPLEMENTA EL TEMPORAL 0
            else:
                temporalUno = "_t1 = "+ p[-1] + " "+ p[-2] + " " +"_t0"  # AQUI  SE COMPONE LO QUE ES EL TEMPORAL 1 Y EL 0

    print(Fore.MAGENTA + espacio +  temporalUno)
    fin = Fin()
#=====================================================================================================
elif x==2:
    espacio = "                                    "
    p = []
    vs = []
    lectura = LeeTxt
    valor =(contents)
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    temporalCero = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] 
            p.remove(p[suma-1])
            p.remove(p[suma])
            p.remove(p[suma-1])
            break 
        else: 
                if i == "/":
                    temporalCero = "_t0 = " + p[suma-1] + " " +  p[suma] + " " + p[suma+1]
                    p.remove(p[suma-1])
                    p.remove(p[suma])
                    p.remove(p[suma-1])
                    break
    inicio = Inicio()
    print(Fore.MAGENTA + espacio + temporalCero)


    #======================================================================================================
   # AQUI EMPIEZA LA EJECUCION DEL TEMPORAL UNO 
    temporalUno = ""
    for i in p: # AQUI EVALUA SI ES UNA DIVICION O UNA MULTIPLICACION
        if p[3] =="+": #
            if p[suma-4]=="/" or p[suma-4]=="*": #AQUI EVALUCIA CUAL OPERACION ES LA MAS CONFIABLE DEPENDIENDO DE LA DECLARACION
                 temporalUno = "_t1 = " + p[suma-5] + " " +  p[suma-4] + " " + p[suma-3] #DEPSUES SE POSCIONA CUAL ES Y PONE LOS CARACTERES CORRESPODIENTES
            elif p[suma-4]  != "/" or p[suma-4] !="*":# AQUI SE MUESTRA LOS DOS TIPOS DE OPERACIONES PRIMORDIALES QUE TIENE QUE ELEJIR 
                if p[suma-4] == "+" or p[suma-4]=="-": # AQUI APARECE LAS OTRAS DOS OPERACIONES SECUNDARIAS QUE EJECUTARA O VERE CUAL DE LAS DOS ES PRIMORDIAL
                    temporalUno = "_t1 = " + p[suma-3] + " " +  p[suma-2] + "_t0"
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO ES EL QUE TOMA LA PRIMERA POCION Y DESPUES SE PONE LO QUE ES EL TEMPORAL DOS 
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                temporalUno = "_t1 = " + p[suma] + " " +  p[suma+1] + " " + p[suma+2]   
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    temporalUno = "_t1 = _t0 " + p[suma-1] + " " +  p[suma]  # AQUI ES DONDE YA SE JUNTAN LOS DOS TEMPORALES EL CUAL ES EL TEMPORAL 0 Y EL TEMPORAL 1 
    
    print(Fore.MAGENTA + espacio + temporalUno)

    #==========================================================================

    temporalDos = ""
    for i in p: # MULTIPLICACION O DIVISION SON LAS VARIABLES A CONSIDERAR 
        if p[3] =="+":
            if p[suma-4]=="/" or p[suma-4]=="*": # SE CHECA CUAL ES LA PRIMORDIAL O CUAL ES LA QUE OFRECE LA OPERACION
                 temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-4] + " " + temporalUno[0:3]
            elif p[suma-4]  != "/" or p[suma-4] !="*":
                if p[suma-4] == "+" or p[suma-4]=="-":
                    temporalDos = "_t2 = " + p[suma-5] + " " +  p[suma-4] + "_t1" # AQUI ES DONDE SE JUNTAN LOS DOS TEMPORALES PRINCIPALES Y SE ANEXA EL TEMPORAL DOS EL CUAL ES LA SUMA DE LOS ANTERIORES 
        elif p[3] !="+":
            if p[suma+1]=="/" or p[suma+1]=="*":
                #STRING TEMPORAL CERO
                # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
                temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-1] + " " + temporalUno[0:3]  
            elif p[suma+1]  != "/" or p[suma+1] !="*":
                if p[suma+1] == "+" or p[suma+1]=="-":
                    temporalDos = "_t1 = _t0 " + p[suma+1] + " " +  p[suma+2] # AQUI SE MUESTRA LA IMCORPORACION DE LOS DOS TEMPORALES INICIALES Y MAS LA INTEGRACION DEL TEMPORAL 2 
    print(Fore.MAGENTA + espacio + temporalDos)
    fin =  Fin()
#======================================================================================================
elif x==3: # En esta parte convierte a triplos los ejercicios dados en parentesis
    espacio = "                                    "
    p = []
    vs = []
    valor = contents
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)

    #=============================================================================
    inicio = Inicio()
    temporalCero = ""
    for i in p: 
        suma +=1
        if i =="(" or i == ")":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE SON LOS PASOS QUE SE NECESITAN PARA QUE EL TEMPORAL 0 FUNCIONE CORRECTAMENTE
            temporalCero = "_t0 = " + p[suma-4] + " " +  p[suma-3] + " " + p[suma-2] + " " + p[suma-1] + " " + p[suma]
            
    #===========================================================================================
    temporalUno = ""
    for i in p:
        if i == "*" or i == "/":
            if p[4] == "(" :
                #EN ESTE APARTADO VUELVE A SUCEDER LA INCORPORACION DE LOS DOS TEMPORLES DEPENDIENDO DE SU 
                temporalUno = "_t1 ="+ " _t0 " + p[suma-5] + " " +  p[suma-6] + " " 
            else:
                temporalUno = "_t1 = " + p[suma-2] + " " +  p[suma-3] + " " +  "_t0"
    #================================================================================================
    temporalDos = ""
    for i in p:
        if i == "+" or i == "-": 
            if p[4] == "(" :
                temporalDos = "_t2="+ " _t1 " + p[suma-7] + " " +  p[suma-8] + " " 
            else:
                temporalDos = "_t2 = " + p[suma] + " " +  p[suma-1] + " " +  "_t1"
    print(Fore.MAGENTA + espacio + temporalCero)
    print(Fore.MAGENTA + espacio +temporalUno)
    print(Fore.MAGENTA + espacio +temporalDos)
    fin = Fin()
#===========================================================================================================
elif x==4: # Este apartado es de los tipos de troplos de  3 simbolos aritmeticos con parentesis 
    espacio = "                                    "
    p = []
    vs = []
    valor = contents
    suma = -1
    for i in valor:
        if i != " ":
            p.append(i)
    inicio = Inicio()
    temporalCero = "" # Aqui  empieza la eleccion del primer simblo a tomar y fromar el temporal 0
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2] 
            p.remove(p[suma-1])
            p.remove(p[suma])
            p.remove(p[suma-1])
            break 
        else:  # estas dos partes depende del tipo de eleccion haya tomado el temporal elige si es divion o multiplicacion
                if i == "+" or i=="-":
                    temporalCero = "_t0 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2]
                    p.remove(p[suma-1])
                    p.remove(p[suma])
                    p.remove(p[suma-1])
                    break      


#============================================================================================================================
    temporalUno = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            # despues de la eleccion del teporal 0 empieza la ejecucion del temporal dos tomando el segundo simbolo aritmetico
            try:
                temporalUno = "_t1 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2] 
                p.remove(p[suma-1])
                p.remove(p[suma])
                p.remove(p[suma-1])
            except: # si el temporal uno no encuentra un simblo aritmetico mandara esta falla 
                IndexError: temporalUno = 'null'
                print("===============================================================================")
                print("ERROR")
                print("caso invalido")
                print("===============================================================================")
            break 
        else: # pero si encuentra un simblo continua y ejecuta su funcion y froma el temporal 
                if i == "+" or i=="-":
                        try:
                            temporalUno = "_t1 = " + p[suma-2] + " " + p[suma-1] + " " +  p[suma] + " " + p[suma+1] + " " + p[suma+2] 
                            p.remove(p[suma-1])
                            p.remove(p[suma])
                            p.remove(p[suma-1])
                        except: #si el temporal uno no encuentra un simblo aritmetico mandara esta falla 
                            IndexError: temporalUno = 'null'
                            print("===============================================================================")
                            print("ERROR")
                            print("caso invalido")
                            print("===============================================================================")
                        break


#=========================================================================================================================================
    temporalDos = ""
    for i in p: # MULTIPLICACION O DIVISION
        suma +=1
        if i =="*" or i=="/":
            #STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-6] + " " + temporalUno[0:3]
            break 
        else: 
                if i == "+" or i=="-":
                    temporalDos = "_t2 = " + temporalCero[0:3] + " " +  p[suma-6] + " " + temporalUno[0:3]
                    break
    #Zona de impresión de resultados
    print(Fore.MAGENTA + espacio + temporalCero)
    print(Fore.MAGENTA + espacio +temporalUno)
    print(Fore.MAGENTA + espacio +temporalDos)
    fin = Fin()

#================================================================================================================
elif x==5: # Al menos 2 símbolos aritméticos con anidamiento de paréntesis
    espacio = "                                    "
    p = []
    S = []
    TC= []
    valor = contents
    suma = -1
    suma2 = -1
    for i in valor:
        if i != " ":
            p.append(i)

    #=============================================================================
    inicio = Inicio()
    for i in p: 
        suma +=1
        if i =="(" or i ==")":
            if i =="(" or i ==")":
                p.remove(p[suma-13])
                TC.append(p[suma-12])
                p.remove(p[suma-12])
                TC.append(p[suma-11])
                p.remove(p[suma-11])
                TC.append(p[suma-10])
                p.remove(p[suma-10])
                TC.append(p[suma-9])
                p.remove(p[suma-9])
                TC.append(p[suma-8])
                p.remove(p[suma-8])
                TC.append(p[suma-7])
                p.remove(p[suma-7])
                TC.append(p[suma-6])
                p.remove(p[suma-6])
                p.remove(p[suma-5])
                #TC = p[suma-12] + " " + p[suma-11] + " " + p[suma-10] + " " + p[suma-9] + " " + p[suma-8] + " " +  p[suma-7] + " " + p[suma-6]
                break
    #================================================================================
    #print(p)
    #print(TC)
    #print(S)


    temporalCero = ""
    for x in TC:  # El temporal cero lo que hace es ejecutar o tomar el primevalor el cual se encuentra dentro del parentesis 
        suma +=1
        if x =="(" or x ==")":
            if TC[0]=="(":
                temporalCero = "_t0 = " + TC[suma2-6] + " " +  TC[suma2-5] + " " + TC[suma2-4] + " " + TC[suma2-3] + " " + TC[suma2-2]
                #temporalCero = "_t0 = " + TC[suma2-4] + " " +  TC[suma2-3] + " " + TC[suma2-2] + " " + TC[suma2-1] + " " + TC[suma2]
            else:
                temporalCero = "_t0 = " + TC[suma2-4] + " " +  TC[suma2-3] + " " + TC[suma2-2] + " " + TC[suma2-1] + " " + TC[suma2]

    #=====================================================================================================
    temporalUno = "" # Este temporal es la suma con el temporal cero pero primero toma la variable la cual dependiendo si es una suma o otra simbolo
    for x in TC: 
        suma2 +=1
        if x =="+" or x =="-" or x =="*" or x =="/":
            if TC[0]=="(":
                temporalUno = "_t1 = t0 "  + TC[suma2-7] + " " +  TC[suma2-6]  
            else:
                temporalUno = "_t1 = t0 "  + TC[suma2-3] + " " +  TC[suma2-4]    

            #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]    


    #============================================================================================
    temporalDos = "" # Este temporal toma el siguiente simblo y forma el temporal 
    for i in p: 
        suma +=1
        if p[0]=="-" or p[0]=="+" or p[0]=="*" or p[0]=="/":
            temporalDos = "_t2 = " + p[1] +  " " + p[2] + " " + p[3]  
            break
        else:
            temporalDos = "_t2 = " + " " +p[0]  + " " + p[3] + " " + p[1] 
            break
                #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]    


    temporalTres = ""# En este temporal hace la suma o junta los dos temporales los cuales son el temporal uno y el temporal dos
    for i in p: 
        suma +=1
        if p[0]=="-" or p[0]=="+" or p[0]=="*" or p[0]=="/":
            temporalTres = "_t3 = " + temporalUno[0:3] +  " " + p[0] + " " + temporalDos[0:3]
            break
        else:
            temporalTres = "_t3 = " + temporalUno[0:3] +  " " + p[2] + " " + temporalDos[0:3]
            break
                #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]    

 
 #=====================================================================================================
   

            #temporalCero = "_t1 = " + TC[suma-8] + " " +  TC[suma-7] + " " +  TC[suma-6] + " " +  TC[suma-5] + " " +  TC[suma-4]
    #zona de impresion de resultados

    print(Fore.MAGENTA + espacio + temporalCero)
    print(Fore.MAGENTA + espacio +temporalUno)
    print(Fore.MAGENTA + espacio +temporalDos)
    print(Fore.MAGENTA + espacio +temporalTres)
    fin = Fin()