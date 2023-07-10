valor = 0
platinum=0
gold=0
silver=0
disponibles=set()
asistentes = ["18.923.938-4","17.510.617-9"]
asientos = 1,2,3,4,5,6,7,8,9,10,
11,12,13,14,15,16,17,18,19,20,
31,32,33,34,35,36,37,38,39,40,
41,42,43,44,45,46,47,48,49,50,
51,52,53,54,55,56,57,58,59,60,
61,62,63,64,65,66,67,68,69,70,
71,72,73,74,75,76,77,78,79,80,
81,82,83,84,85,86,87,88,89,90,
91,92,93,94,95,96,97,98,99,100
menu = """
             1. COMPRAR ENTRADAS
             2. MOSTRAR UBICACIONES DISPONILES
             3. VER LISTADO DE ASISTENTES
             4. MOSTRAR GANANCIAS TOTALES
             5. SALIR"""
 
def buyTick ():
    while True:
        try:
            r=input("Ingrese su run Sin guin,puntos ni digito verificado \n")
            if (len(r))>=8 and (len(r)) <=9:
                break
            else:
                print("Run invalido")
        except:
            print("excepcion nombre")

    while True:
        try:
            cantCompra=int(input("Ingrese cuantas entradas 1-3 \n"))
            if cantCompra >=1 and cantCompra <=3:
                break
            else:
                print("Rango Invalido")
        except:
            print("Excepcion 1")      

    for i in range (cantCompra):
        selecA=int(input("Que ubicacion desea \n"))
        if selecA >= 1 and selecA <= 20:
            if selecA in disponibles:
                print("No está disponible, ubicacion ocupada")
            else:
                print("Compra realizada con exito")
                platinum = platinum + 1
                disponibles.add(selecA)
        if selecA >= 21 and selecA <= 50:
            if selecA in disponibles:
                print("No está disponible, ubicacion ocupada")
            else:
                print("Compra realizada con exito")
                gold = gold + 1

                disponibles.add(selecA)
        if selecA >= 51 and selecA <= 100:
            if selecA in disponibles:
                print("No está disponible, ubicacion ocupada")
            else:
                print("Compra realizada con exito")
                silver = silver + 1
                disponibles.add(selecA)



#inicio funcion asientos disponibles
def showDisp ():
    print("Ubicaciones\n")
    for i in range (1,101):
        selecA=str(i).zfill(1)
        if selecA in disponibles:
            print(selecA,end=" ")
        else:
            print(selecA,end=" ")
        if i%10==0:
            print()
# fin mostrar

def total():
    print("Entradas Y dinero")
    print(f"Platinum {platinum} ${platinum*120000}")
    print(f"Gold {gold} ${gold*80000}")
    print(f"Silver: {silver} ${silver*50000}")
    print(f"Total Entradas: {platinum+gold+silver} Total Dinero: ${platinum*120000+gold*80000+silver*50000}")


#Codigo Principal
while True:

        opc=int(input(menu))
        if opc == 5:
            print("salida del sitema... Agustin Sepulveda 10/07/2023")
            break
        elif opc == 1:
            print("1. Comprar Entradas")
            buyTick()
        elif opc == 2:
            print("2. Mostrar ubicacion Disponible")
            showDisp()
        elif opc == 3:
            print("3. Mostrar Lista de asistentes")
            print(asistentes)
            input("Enter para continuar")
        elif opc == 4:
            print("4. Mostrar Ganancias Totales")
            total()
            input("Enter para continuar")
