#Funciones >>>>>>>>>>>>>>
def validar_numero(n):
    num = "1234567890"
    for i in range(len(n)):
        if n[i] not in num:
            return False
        return True
    
def validar_rut(rut):
    if rut != str(rut):
        return False
    n = "1234567890"
    k = "1234567890kK"
    # 11.111.111-5 // 1.111.111-k
    if rut == "":
        return False
    if rut[0] == "0":
        return False
    if len(rut) == 11:
        rut = "0" + rut
    if len(rut) == 12:
        if rut[0] not in n or rut[1] not in n or rut[3] not in n or rut[4] not in n or rut[5] not in n or rut[7] not in n or rut[8] not in n or rut[9] not in n:
            return False
        if rut[2] != "." or rut[6] != ".":
            return False
        if rut[10] != "-":
            return False
        if rut[-1] not in k:
            return False
        return True
    return False
    
def crear_Ficha(fichas,rut):
    ficha_temp = [[],[],[],"",[],[],[],[]]
    # nº ficha de ingreso
    ficha_temp[0].append(str(input("Ingrese fecha de atención: ")))
    ficha_temp[0].append(str(input("Ingrese hora de atención: ")))
    ficha_temp[0].append(str(input("Ingrese nombre del personal: ")))
    # identificacion del paciente
    ficha_temp[1].append(str(input("Ingrese nombre del paciente: ")))
    ficha_temp[1].append(str(input("Ingrese apellido del paciente: ")))
    x = str(rut) #validar si es un rut /// LISTO
    while not validar_rut(x):
        x = str(input("Error, rut fuera de rango, ingrese nuevamente: "))
    ficha_temp[1].append(x)
    x =(str(input("Ingrese sexo del paciente(F/M): "))) #validar si es femenino o masculino /// LISTO
    while x.upper() != "F" and x.upper() != "M":
        x = str(input("Error, vuelva a ingresar el genero del paciente(F/M): "))
    if x == "F":
        x = "Femenino"
    else:
        x = "Masculino"
    ficha_temp[1].append(x)
    ficha_temp[1].append(str(input("Ingrese estado civil del paciente: ")))
    x = str(input("Ingrese edad del paciente: "))#validar rango o que no sea negativo
    flag = True
    while flag:
        while not validar_numero(x):
            x = str(input("Error, edad fuera de rango, ingrese nuevamente: "))
        x = int(x)
        if x < 0:
            x = "XD"
        else:
            flag = False
            ficha_temp[1].append(x)
    
    #ficha_temp[1].append(int(input("Ingrese edad del paciente: "))) 
    #while ficha_temp[1][5] < 0:
    #    ficha_temp[1][5] = int(input(print("Error, edad fuera de rango, ingrese nuevamente: ")))
    
    ficha_temp[1].append(str(input("Ingrese domicilio del paciente: ")))
    ficha_temp[1].append(str(input("Ingrese grupo_sanguineo del paciente: ")))
    ficha_temp[1].append(str(input("Ingrese fono del paciente: ")))
    x = str(input("¿Asiste acompañado? (si/no): "))
    while x.upper() != "SI" and x.upper() != "NO":
        x = str(input("Error, respuesta solo puede ser (si/no): "))
    if x.upper() == "SI":
        ficha_temp[1].append("SI")
        # identificacion del acompañante
        ficha_temp[2].append(str(input("Ingrese nombre del acompañante: ")))
        ficha_temp[2].append(str(input("Ingrese apellido del acompañante: ")))
        x = str(input("Ingrese rut del acompañante: ")) #validar si es un rut /// LISTO
        while not validar_rut(x):
            x = str(input("Error, rut fuera de rango, ingrese nuevamente: "))
        ficha_temp[2].append(x)
        ficha_temp[2].append(str(input("Ingrese el grado de parentesco: ")))
        ficha_temp[2].append(str(input("Ingrese el fono del acompañante: ")))
    else:
        ficha_temp[1].append("NO")
        ficha_temp[2].append(False)
    # Motivo de la consulta
    ficha_temp[3] = str(input("Ingrese el motivo de la consulta: "))
    # Información de atención
    ficha_temp[4].append(str(input("Ingrese nombre del médico: ")))
    ficha_temp[4].append(str(input("Ingrese especialidad del médico: ")))
    ficha_temp[4].append(str(input("Ingrese los síntomas: ")))
    ficha_temp[4].append(str(input("Ingrese diagnóstico: ")))
    x = str(input("¿Necesita reposo? (si/no): "))
    while x.upper() != "SI" and x.upper() != "NO":
        x = str(input("Error, respuesta solo puede ser (si/no): "))
    if x.upper() == "SI":
        ficha_temp[4].append("SI")
        x = str(input("Ingrese cantidad de días de reposo: "))#validar valor negativo // faltaba validar que fuera un numero:
        flag = True
        while flag:
            while not validar_numero(x):
                x = str(input("Error, días fuera de rango, ingrese nuevamente: "))
            x = int(x)
            if x < 0:
                x = "XD"
            else:
                flag = False
                ficha_temp[4].append(int(x))
    else :
        ficha_temp[4].append("NO")
    x = str(input("¿Hay medicamento asignado? (si/no): "))
    if x.upper() == "SI":
        #informacion medicamento FALTA EL APPEND DEL "SI" ///// YA LO PUSE
        ficha_temp[5].append("SI")
        ficha_temp[5].append(str(input("Ingrese nombre del medicamento: ")))
        ficha_temp[5].append(str(input("Ingrese dosis del medicamento: ")))#validar valor negativo /// FALTA
        ficha_temp[5].append(int(input("Ingrese cantidad de días con el medicamento: ")))#validar valor negativo /// falta validar cuando no es un numero
        while ficha_temp[5][3] < 0:
            ##### NO SE PONE input(print()), ES SOLO INPUT
            ficha_temp[5][3] = int(input("Error, días fuera de rango, ingrese nuevamente: "))
    else:
        ficha_temp[5].append(False)
    #datos extra del medico
    x = str(input("Ingrese RUN del médico: ")) #validar si es un rut /// LISTO
    while not validar_rut(x):
        x = str(input("Error, rut fuera de rango, ingrese nuevamente: "))
    ficha_temp[6].append(x)
    ficha_temp[6].append(str(input("Ingrese horario de atención del médico: ")))
    ficha_temp[6].append(str(input("Ingrese título del médico: ")))
    ficha_temp[6].append(str(input("Ingrese institución en dónde consiguió el título el médico: ")))
    #ficha_temp[6].append(int(input("Ingrese año donde consiguió el título el médico: ")))#validar valor negativo
    x = str(input("Ingrese año donde consiguió el título el médico: "))#validar valor negativo // faltaba validar que fuera un numero:
    flag = True
    while flag:
        while not validar_numero(x):
            x = str(input("Error, año fuera de rango, ingrese nuevamente: "))
        x = int(x)
        if x < 0:
            x = "XD"
        else:
            flag = False
            ficha_temp[6].append(int(x))

    """
    while ficha_temp[6][4] < 0:
        ##### NO SE PONE input(print()), ES SOLO INPUT
        #ficha_temp[6][4] = int(input(print("Error, el año esta fuera de rango, ingrese nuevamente: ")))
        ficha_temp[6][4] = int(input("Error, el año esta fuera de rango, ingrese nuevamente: "))
    """
    
    ficha_temp[6].append(str(input("Ingrese fono del médico: ")))
    ficha_temp[6].append(str(input("Ingrese dirección del médico: ")))
    #dato extra administrativos
    ficha_temp[7].append(str(input("Ingrese nombre del administrativo: ")))
    ficha_temp[7].append(str(input("Ingrese fono del administrativo: ")))
    ficha_temp[7].append(str(input("Ingrese dirección del administrativo: ")))
    y = ficha_temp[1][2]
    fichas[y] = ficha_temp


def buscar_Ficha(rut,fichas):
    ficha = fichas[rut]
    print("DATOS PACIENTE")
    print("---------------")
    print("Rut: " + ficha[1][2])
    print("Nombre y Apellido: " + ficha[1][0] + " " + ficha[1][1])
    print("Sexo: " + ficha[1][3])
    print("Estado civil: " + ficha[1][4])
    print("Edad: " + str(ficha[1][5])) # lo puse como string para que se agregue correctamente
    print("Domicilio: " + ficha[1][6])
    print("Grupo sanguineo: " + ficha[1][7])
    print("Fono: " + ficha[1][8])
    
def buscar_Medicamento(rut,fichas):#validar
    ficha = fichas[rut]
    if ficha[5][0] == "SI":
        print("INFORMACIÓN DE MEDICAMENTO")
        print("--------------------------")
        print("Nombre del medicamento: " + str(ficha[5][1]))
        print("Dosis: " + str(ficha[5][2]))
        print("Cantidad de días: "+ str(ficha[5][3]))
    else:
        print("Al paciente no le recetaron medicamentos")
    
def eliminar_Pacientes(fichas,rut):
    del fichas[rut]
      
def listar_Pacientes(fichas):
    cont = 0
    for i in fichas:
        cont += 1 
        ficha = fichas[i]
        print("paciente numero: "+str(cont))
        print("nombre: "+str(ficha[1][0]) + " " + str(ficha[1][1]))
        print("rut: "+str(i))
        print("")

#Programa principal
fichas = {}
opcion = 0
opciones_posibles = "123456"
while opcion != 6:
    print("SERVICIO DE ATENCION MÉDICA DE URGENCIAS")
    print("-----------------------------------------")
    print("1) Ingresar Ficha del Paciente")
    print("2) Buscar Ficha por Rut")
    print("3) Buscar Medicamentos por Rut")
    print("4) Eliminar Ficha del Paciente")
    print("5) Listar Paciente Atendidos")
    print("6) Salir")
    opcion = str(input("Ingrese una opcion: "))
    flaga = True
    while flaga:
        while not validar_numero(opcion):
            opcion = input("Error, opción fuera de rango, ingrese nuevamente: ")
        if opcion not in opciones_posibles:
            opcion = "XD"
        else:
            opcion = int(opcion)
            flaga = False
    if opcion == 1 :
        rut = input("Ingrese el rut: ")
        while not validar_rut(rut):
            rut = input("Error, rut fuera de rango, ingrese nuevamente: ")  
        if rut in fichas:
            x = input("Este rut ya se encuentra registrado, ¿Desea remplazar la ficha?(si/no)")
            if x.upper() == "SI":
                (fichas,rut) #si existe el rut preguntar si desea remplazar la ficha /// LISTO
            else:
                print("La ficha no ha sido remplazada")
        else:
            crear_Ficha(fichas,rut)
    elif opcion == 2:
        rut = input("Ingrese el rut: ")
        if rut in fichas:
            buscar_Ficha(rut,fichas)
        else:
            print("El rut no se encuentra registrado")
    elif opcion == 3:
        rut = input("Ingrese el rut: ")
        if rut in fichas:
            buscar_Medicamento(rut,fichas)
        else:
            print("El rut no se encuentra registrado")
    elif opcion == 4:
        rut = input("Ingrese el rut: ")
        if rut in fichas:
            eliminar_Pacientes(fichas,rut)
        else:
            print("El rut no se encuentra registrado")
    elif opcion == 5:
        if fichas == {}:
            print("No hay ningún rut registrado")
        else:
            listar_Pacientes(fichas)

