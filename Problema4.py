
PATH_DATA = './src/temperaturas.txt'
PATH_DATA_OUT = './src/resumen_temperaturas.txt'
def procesamiento(data_list:list)->list:
    temperaturas = []
    for linea in data_list:
        _, temperatura=linea.strip().split(',')
        temperatura = float(temperatura)
        temperaturas.append(temperatura)
    return temperaturas

def main():
    print('Inicializando lectura de los datos ...')
    lineas = open(PATH_DATA, mode='r').readlines()
    print('Realizando Procesamiento ...')
    temperaturas= procesamiento(lineas)
    temperatura_max = max(temperaturas)
    temperatura_min = min(temperaturas)
    temperatura_promedio = sum(temperaturas)/len(temperaturas)
    print('Almacenando resultado ...')
    with open(PATH_DATA_OUT, mode='w') as file:
        file.write(f'Temperatura máxima: {temperatura_max}\n')
        file.write(f'Temperatura mínima: {temperatura_min}\n')
        file.write(f'Temperatura promedio: {temperatura_promedio:.2f}\n')
    pass

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Hubo un error en el procesamiento de los datos ..')
        print(e)
    finally:
        print('Finalizando Programa !!!')