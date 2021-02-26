#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, getpass, subprocess

config = open('config.txt', 'r')
leer = config.readlines()
dotfiles = []

for configs in leer:
    lista = dotfiles.append(configs) 

config.close()

dotfiles = dotfiles[0]

directorioActual = os.getcwd()
user = getpass.getuser()
userdirectory = os.listdir(f"/home/{user}")
confdirectory = os.listdir(f"/home/{user}/.config")
subprocess.run([f"mkdir {directorioActual}/.config"], shell=True)

for x in userdirectory:
    if x in dotfiles:
        subprocess.run([f"rsync -ar /home/{user}/{x} {directorioActual}"], shell=True)
        subprocess.run([f"rm -rf {directorioActual}/.vim"], shell=True)
    
for y in confdirectory:
    if y in dotfiles:
        subprocess.run([f"rsync -ar /home/{user}/.config/{y} {directorioActual}/.config"], shell=True) 
        subprocess.run([f"rm -rf {directorioActual}/.config/vim"], shell=True)

