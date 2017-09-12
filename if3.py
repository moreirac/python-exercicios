#!/usr/bin/env python3

age = input('Entre sua idade: ')
age = int(age)
have_own_car = input('Tem carro próprio (s/n): ')

if (age >= 21):
	if (have_own_car == 's'):
        	print('Tem 21 e tem carro')
	else:
		print('Tem 21 e não tem carro')

else:
	if (have_own_car == 's'):
	        print('< 21 e tem carro')
	else:
		print('< 21 e não tem carro')


