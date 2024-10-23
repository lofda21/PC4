import os
BIENVENIDA = '='*20 + " Bienvenido al Menu Interactivo " + '='*20

OPCIONES = """ Seleccione una de las siguiente opciones:
    1) Crear tabla n
    2) Leer tabla n
    3) Leer tabla n y leer linea m
    4) Salir

OPCION: """
FILE_NAME = './src/tabla-{n}.txt'

def get_n(msg: str)-> int:
    """Get an int 'n' between 1 and 10 """
    try:
        n = int(input(msg))
        assert n>=1 and n<=10
        return n
    except:
        return get_n(msg)
def opcion1():
    n = get_n("Introduce un número entero entre 1 y 10: ")
    
    lines = [ f'{n} x {i} = {n*i}\n' for i in range(1, 13)]
    
    file_name =  FILE_NAME.format(n=n)
    if os.path.isfile(file_name):
        os.remove(file_name)
    open(file_name, mode='w').writelines(lines)
    pass
def opcion2():
    n = get_n("Introduce un número entero entre 1 y 10: ")
    
    file_name = FILE_NAME.format(n=n)
    try:
        with open(file_name, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', n)
def opcion3():
    n = get_n("Introduce un número entero entre 1 y 10: ")
    m = int(input('Introduce un número entero entre 1 y 12: '))
    
    file_name = FILE_NAME.format(n=n)
    try:
        with open(file_name, 'r') as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', n)
    
    print(lineas[m-1])
    

def main():
    print(BIENVENIDA)
    while True:
        opcion = input(OPCIONES)
        if opcion=='1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            break
        else:
            print('Opción Invalida! Vuelva a seleccionar una opción.')

if __name__ == '__main__':
    main()