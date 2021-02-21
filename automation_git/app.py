#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app_git import checkGit, questionInit, archives, questionGitignore, questionREADME, seguimiento



check = checkGit()


def condition():
    if archives() == False:
        questionREADME()
        questionGitignore()
    elif archives() == 'gitignore':
        questionREADME()
    elif archives() == 'readme':
        questionGitignore()
    else:
        seguimiento()



def invoked():
    if check == True:
        condition()
    else:
        if questionInit() == False:
            condition()
        else:
            pass

    
        
invoked()