from os import system, name
import sys

from gramaticas import Gramatica, Producciones
lista_nombres_Gramatica = []
lista_Gramaticas = []
lista_Automatas = []
menu_principal='''
MENU
1. Modulo Gramatica Libre de Contexto
2. Modulo Automata de Pila
0. Salir
'''
modulo_gramatica = ''''
MODULO DE GRAMATICA LIBRE DE CONTEXTO
1. Cargar Archivo
2. Mostrar Informacion General
3. Arbol de Derivacion
0. Salir
'''
error = '''**** ALGO HA SALIDO MAL, INTENTALO DE NUEVO ****'''

continuar = '''**** PRESIONA ENTER PARA CONTINUAR ****'''

selecciona_una_opcion = '''Selecciona una opcion para continuar'''

operacion = '''**** OPERACION REALIZADA CON EXITO ****'''

def borrarPantalla():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Cargar_Gramatica():
    try:
        from itertools import groupby as eliminar_repetidos
        nom = input('Escriba el nombre del archivo')
        File = open(nom+'.glc', 'r')
        x = 1
        lista_producciones = []
        lista_terminales = []
        lista_no_terminales = []
        lctxt = False
        for file in File:
            file = file.rstrip('\n')
            if x==1:
                nombre = file
                if (nombre in lista_nombres_Gramatica):
                    borrarPantalla()
                    print(f'\nALERTA: La Gramatica *** {nombre} *** sera saltada debido a que ya existe ...\n')
                    input(continuar)
                    x = '%'
                else:
                    lista_nombres_Gramatica.append(nombre)

            if x==2:
                file = file.replace(' ','')
                le = file.split(",")
                for l in le:
                    lista_no_terminales.append(l)
                
            if x==3:
                la = file.split(',')
                la.sort()
                l = list(lista for lista, _ in eliminar_repetidos(la))
                for listae in lista_no_terminales:
                    for listaa in lista_terminales:
                        if listaa == listae:
                            print('\nERROR: No fue posible crear el automata debido a que el alfabeto de entrada contiene simbolos no terminales\n')
                            lista_nombres_Gramatica.remove(nombre)
                            x = '%'
                            input(continuar)
            
            if x==4:
                einic = file
                recorrer = False
                for ee in lista_no_terminales:
                    if einic == ee:
                        recorrer = True
                if recorrer == False:
                    print('\nERROR: No fue posible crear el automata debido a que el estado inicial no es un no terminal\n')
                    lista_nombres_Gramatica.remove(nombre)
                    x = '%'
                    input(continuar)
                else:
                    einicial = False
                
            if x != '%':
                if x>=5 and file != '%':
                    files = file.split('>')
                    files2 = files[1].split()
                    if len(files2) >= 3:
                        lctxt = True

                    if ((files[0] in lista_no_terminales) and (files[1] in lista_no_terminales)):
                        lctxt = True
                    
                    if (files[0] in lista_terminales) and (files[1] in lista_terminales):
                        lctxt = True

                    if len(files2) == 1 and files2[0] in lista_no_terminales:
                        lctxt = True
                    
                    lista_producciones.append(Producciones(files[0], files2))
            
            if file == '%' and x!="%":
                if lctxt == True:
                    lista_Gramaticas.append(Gramatica(nombre, lista_no_terminales, lista_terminales, einic, lista_producciones))
                    lista_producciones = []
                    lista_terminales = []
                    lista_no_terminales = []
                    x = 0
                    lctxt = False
                else:
                    print('\nERROR: No fue posible crear la gramatica debido a que la gramatica no es libre de contexto\n')
                    lista_nombres_Gramatica.remove(nombre)
                    lista_producciones = []
                    lista_terminales = []
                    lista_no_terminales = []
                    x = 0
                    input(continuar)

            if file == '%':
                lista_producciones = []
                lista_terminales = []
                lista_no_terminales = []
                x = 0

            if x!='%':
                x+=1
        borrarPantalla()
        print(operacion)
        print(f'\nLa Gramatica *** {nombre} *** fue cargada con exito ...\n')
        input(continuar)
        borrarPantalla()
    except Exception:
        e = sys.exc_info()[1]
        print(e.args[0])
        print(error)
        input(continuar)
        borrarPantalla()


def Arbol_Gramatica():
    z = False
    while not z:
        try:
            borrarPantalla()
            print('GRAMATICAS DISPONIBLES:\n')
            y = 1
            for x in lista_nombres_Gramatica:
                print(f'{y}. {x}')
                y+=1
            print('0. Regresar')
            resp = input('Seleccione el nombre o numero de la gramatica: ')
            if resp in lista_nombres_Gramatica:
                j = lista_nombres_Gramatica(resp)
                resp = j+1
            if resp !='0' and int(resp)>0:
                from graphviz import Graph

                dot = Graph(name='GramaticaLC', encoding='utf-8', format='png', filename='GramaticasLC')

                dot.attr(rankdir='TB', layout='dot', shape='none')

                numero = -1
                listaP = []
                indice = 0
                aux = 0
                lista_Nodos = []
                r_2 = int(resp)-1
                for nodo in lista_Gramaticas[r_2].producciones:
                    aux = 0
                    if lista_Nodos[:] != []:
                        for x in lista_Nodos:
                            if nodo.origen == x:
                                indice = aux
                            aux+=1
                    else:
                        numero+=1
                        dot.node(name='nodo'+str(numero), label=nodo.origen, shape='none')
                        lista_Nodos.append(nodo.origen)
                    
                    for y in nodo.destinos:
                        numero +=1
                        dot.node(name='nodo'+str(numero), label=y, shape='none')
                        listaP.append(numero)
                        lista_Nodos.append(y)
                    for z in listaP:
                        dot.edge('nodo'+str(indice), 'nodo'+str(z))
                    listaP = []
                    aux = 0
                print('\nAbriendo el archivo generado...\n')
                dot.render('GramaticasLC/'+lista_Gramaticas[r_2].nombre, format='png' ,view=True)
                input(continuar)
            elif int(resp) <0:
                print('\nERROR: Selecciona una opcion valida\n')
                input(continuar)
            else:
                z = True
        except:
            print("\nPor favor seleccione una opción correcta...")
            input(continuar)
def GramaticasLC():
    a = True
    b = False
    while a == True:
        while b == False:
            borrarPantalla()
            print(modulo_gramatica)
            op = str(input("Selecciona una opcion para continuar \n"))
            if op == '1':
                Cargar_Gramatica()
                break
            elif op == '2':
                # MostrarInfo_Gramatica()
                break
            elif op == '3':
                Arbol_Gramatica()
                break
            elif op == '4':
                # GenerarAPE()
                break
            elif op == '0':
                a = False
                b = True
            else:
                print('Selecciona una opcion valida\n')

borrarPantalla()
x = True
y = False
while x == True:
    borrarPantalla()
    print(menu_principal)
    while y == False:
        op = str(input("Selecciona una opcion para continuar\n"))
        if op == '1':
            GramaticasLC()
            break
        else:
            print('Selecciona una opcion correcta')
