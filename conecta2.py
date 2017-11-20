#!/usr/bin/python

import sys
import os

usuario = raw_input("Usuario: ")
clave = raw_input("Clave: ")
basedatos = raw_input("Base de datos: ")
cadena = "mysql -u " + usuario + " -p" + clave + " " + basedatos
print cadena
os.system (cadena)
