#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Importamos modulos subprocess y os
import subprocess
import os

## Inicializamos las Variables para saber cual 
## es nuestro directorio actual y listarlo. 
directory = os.getcwd() 
listDirectory = os.listdir(directory)

## FUNCIONES ##

## Se comprueba si hay un repo inicializado en el directorio actual, 
## sino lo hubiera, se pregunta si se quiere iniciar.
def checkGit():
    if '.git' in listDirectory:
        return True
    else:
        return False
        
        
def questionInit():    
    while True:
        answer = input('¿Quieres inicializar un repositorio? S/n ')
        if answer == 'S':
            subprocess.run(['git init'], shell=True)
            print ('Repositorio inicializado')
            return False
        elif answer == 'n':
            print('Hasta pronto')
            break
        else:
            print('Introduce un opción valida\n')
                

## Se comprueba si existe el archivo .gitignore y README.md.
def archives():
    if '.gitignore' in listDirectory and 'README.md' in listDirectory:
        return True
    elif '.gitignore' in listDirectory and 'README.md' not in listDirectory:
        return 'gitignore'
    elif '.gitignore' not in listDirectory and 'README.md'in listDirectory:
        return 'readme'
    elif '.gitignore' not in listDirectory and 'README.md' not in listDirectory:
       return False     


## Se pregunta si quiere crear .gitignore.
def questionGitignore():
    
    while True:
        ignore = input('¿Quieres crear el archivo .gitignore? S/n ')
        if ignore == 'S':
            subprocess.run(['touch .gitignore'], shell=True)
            print('.gitignore creado')
            break
        elif ignore == 'n':
            break
        else:
            print('Introduce un opción valida')



## Se pregunta si quiere crear README.md.
def questionREADME():
    
    while True:
        readme = input('¿Quieres crear el archivo README.md? S/n ')
        if readme == 'S':
            subprocess.run(['touch README.md'], shell=True)
            print('README.md creado')
            break
        elif readme == 'n':
            break
        else:
            print('Introduce un opción valida')




# crear funcion