#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&ˆ*'

number = input('numero de contraseñas: ')
number = int(number)

length = input('Longitud de la contraseña: ')
length = int(length)

for p in range(number):
	password = ''
	for c in range(length):
		password += random.choice(chars)
	print(password)
