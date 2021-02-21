#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app_git import checkGit, questionInit, archives, questionGitignore, questionREADME



check = checkGit()


def naine():
    if archives() == False:
        questionREADME()
        questionGitignore()
    elif archives() == 'gitignore':
        questionREADME()
    elif archives() == 'readme':
        questionGitignore()
    else:
        print('adios') # crear funcion


def main():
    if check == True:
        naine()
    elif check == False:
        questionInit()
        naine()
        

main()