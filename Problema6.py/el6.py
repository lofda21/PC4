import sys
import os

os.chdir(os.path.dirname(__file__))

def main():
    file_name = input('Ingrese el nombre del archivo: ').strip()
    if not file_name.endswith('.py'):
        print('Not a Python file')
        sys.exit(1) 

    try:
        lines= open(file_name, encoding='utf-8').readlines()
    except FileNotFoundError:
        print('File does not exist')
        sys.exit(1)

    count = 0
    for line in lines:
        if line.strip().startswith('#') or line.strip()=='':
            continue
        count +=1
    print(count)

if __name__ == '__main__':
    main()