
age = input('Entre sua idade: ')
age = int(age)
have_own_car = input('Tem carro próprio (s/n): ')

if (age > 21) and (have_own_car == 's'):
	print('> 21 e tem carro')

if (age > 21) and (have_own_car == 'n'):
	print('> 21 e não tem carro')

if (age == 21) and (have_own_car == 's'):
        print('Tem 21 e tem carro')

if (age == 21) and (have_own_car == 'n'):
        print('Tem 21 e não tem carro')

if (age < 21) and (have_own_car == 's'):
        print('< 21 e tem carro')

if (age < 21) and (have_own_car == 'n'):
        print('< 21 e não tem carro')


