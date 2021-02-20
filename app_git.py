
# -*- coding: utf-8 -*-

import subprocess
import os


def check():
    directory = os.getcwd() 
    listDirectory = os.listdir(directory)

    if '.git' in listDirectory:
        salida = subprocess.check_output(['git status'])
        return salida
    else:
        print ('Este directorio no contiene un repositorio Git')
        answer = input('¿Quieres inicializar un repositorio? S/n ')

        if answer == 'S' or answer == 's':
            subprocess.run(['git init'], shell=True)
        elif answer == 'N' or answer == 'n':
            print('Hasta pronto')
            exit(0)

output = check()

def add():
    if output == 0:
        subprocess.run(['git add .'], shell=True)
    else:
        exit()

add()