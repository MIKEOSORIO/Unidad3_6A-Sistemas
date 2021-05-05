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
    # =============================================================================
    temporalCero = ""
    for i in p:
        suma += 1
        if i == "(" or i == ")":
            # STRING TEMPORAL CERO
            # TEMPORALCERO = VARIABLE | OPERANDO 1 | VARIABLE
            temporalCero = "_t0 = " + p[suma - 4] + " " + p[suma - 3] + " " + p[suma - 2] + " " + p[suma - 1] + " " + p[
                suma]
                # en este apartado se hizo el cambio de variables en los temporales ya que salia invertido
    # =============================================================================
    temporalUno = ""
    for i in p:
        if i == "*" or i == "/":
            if p[4] == "(":
                temporalUno = "_t1 =" + " _t0 " + p[suma - 5] + " " + p[suma - 6] + " "
            else:
                temporalUno = "_t1 = " + " _t0 " + p[suma - 3] + " " + p[suma - 2] + " "
    # =============================================================================
    temporalDos = ""
    for i in p:
        if i == "+" or i == "-":
            if p[4] == "(":
                temporalDos = "_t2 = " + " _t1 " + p[suma - 7] + " " + p[suma - 8] + " "
            else:
                temporalDos = "_t2 = " + " _t1 " + p[suma - 1] + " " + p[suma] + " "

    #apartado de impresion--------------------------
    inicio = Inicio()
    print(Fore. MAGENTA +espacio + temporalCero)
    print(Fore. MAGENTA +espacio +temporalUno)
    print(Fore. MAGENTA +espacio +temporalDos)
    fin = Fin()

#===========================================================================================================
elif x==4: # Este apartado es de los tipos de triplos de  3 simbolos aritmeticos con parentesis
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
        valor = contents #asignamos los valor del .txt a la varible valor
        pila = []
        resultado = []
        resultado_f = []
        resultado_ff = []
        contador = -1
        if valor != " ":
            for i in valor:
                if i != " ":
                    pila.append(i)

        for i in pila:
            contador += 1

            if i == "(":
                resultado.append(pila[contador])
                resultado.append(pila[contador + 1])
                resultado.append(pila[contador + 2])
                resultado.append(pila[contador + 3])
                resultado.append(pila[contador + 4])
                resultado.append(pila[contador + 5])
                resultado.append(pila[contador + 6])
                resultado.append(pila[contador + 7])
                resultado.append(pila[contador + 8])
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)
                pila.pop(contador)

        if pila[-1] == "*" or pila[-1] == "/":
            resultado_f.append([pila[-1], pila[-2]])
            pila.pop()
            pila.pop()
        else:
            resultado_f.append([pila[-2], pila[-3], pila[-4]])
            pila.remove(pila[-2])
            pila.remove(pila[-2])
            pila.remove(pila[-2])

        resultado.remove(resultado[0])
        resultado.pop()

        contador = -1
        for i in resultado:
            contador += 1
            if i == "(":
                resultado_ff.append([resultado[contador + 1], resultado[contador + 2], resultado[contador + 3]])
                resultado.remove(resultado[contador])
                resultado.remove(resultado[contador])
                resultado.remove(resultado[contador])
                resultado.remove(resultado[contador])
                resultado.remove(resultado[contador])

        valor_t0 = "t0 = " + " ".join(resultado_ff[0])
        valor_t1 = "t1 = t0 " + " ".join(resultado)
        valor_t2 = "t2 = " + " ".join(resultado_f[0])
        valor_t3 = "t3 = t2 " + pila[-1] + " t1"
        
        # hubo una modificacion, en los valores ya que tenia los operandos invertidos

        # Espacio de impresion de Resultados

        inicio = Inicio()
        print(Fore.MAGENTA + espacio + valor_t0)
        print(Fore.MAGENTA + espacio + valor_t1)
        print(Fore.MAGENTA + espacio + valor_t2)
        print(Fore.MAGENTA + espacio + valor_t3)
        fin = Fin()
