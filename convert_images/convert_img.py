#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
from pathlib import Path
import os, glob




def wordpress():
    directorio = Path(input('Ruta al directorio de imágenes: '))

    for img in directorio.glob("*.png"):
        file, ext = os.path.splitext(img)
        image = Image.open(img)
        imageRgb = image.convert('RGB')
        imagenReducida = imageRgb.resize((850, 550))
        imagenReducida.save(file + ".jpg", "JPEG", quality=80)


def cambiarTipoImagen():
    imagen = input('Ruta a la imagen: ')
    formato = input('¿A que formato convertimos la imagen?: ')

    file, ext = os.path.splitext(imagen)
    image = Image.open(imagen)
    imageRgb = image.convert('RGB')
    imageRgb.save(file + f".{formato}", quality=80)


def cambiarTamañoImagen():
    imagen = input('Ruta a la imagen: ')
    formato = int(input('¿A que tamaño de alto convertimos la imagen?: '))
    formato0 = int(input('¿A que tamaño de ancho convertimos la imagen?: '))

    file, ext = os.path.splitext(imagen)
    image = Image.open(imagen)
    imagenReducida = image.resize((formato, formato0))
    imagenReducida.save(file + ext)



def rotarImagen():
    imagen = input('Ruta a la imagen: ')
    grados = int(input('¿Cuantos grados rotamos la imagen?: '))

    file, ext = os.path.splitext(imagen)
    image = Image.open(imagen)
    rotar = image.rotate(grados)

    rotar.save(file + ext)




def menu():
    while True:
        pregunta = input(""" (1) Optimizar para WordPress por lotes (Default)\n (2) Cambiar tipo de imagen\n (3) Cambiar tamaño imagen 
 (4) Rotar imagen\n (5) Agregar marca de agua\n (6) Voltear imagen\n Elige una opción (1/6) o Intro para Default:\n """)
        if pregunta == '1':
            wordpress()
            break
        elif pregunta == '2':
            cambiarTipoImagen()
            break
        elif pregunta == '3':
            cambiarTamañoImagen()
            break
        elif pregunta == '4':
            rotarImagen()
            break
        elif pregunta == '5':
            print("Agregar marca")
            break
        elif pregunta == '6':
            print("Voltear imagen")
            break
        elif pregunta == '':
            wordpress()
            break
        else:
            print("Introduce una opción valida")








menu()