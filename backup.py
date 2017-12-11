#!/usr/bin/python

import os
import sys

print "Usuario"
usuario=raw_input()

print "Contraseña"
password=raw_input()

print "Bae de Datos"
bd=raw_input()

print "Nombre del dichero backup"
backup=raw_input()

os.system('mysql --user=' + usuario + ' --password=' + password + ' ' + bd + ' | gzip > ' + backup '.sql.gz')
