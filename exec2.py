#!/usr/bin/env python3

import subprocess


def criar_diretorio():
	global opa
	opa = input('Digite o nome do diretório: ')
	subprocess.call(['mkdir', opa])


def criar_arquivos():
	for i in range(1,40):
		#subprocess.call(['touch','{}/{}'.format(opa, str(i))])
		subprocess.call(['touch', str(i)], cwd=opa)


def listar_arquivos():
	ls = subprocess.check_output(['ls','-lha', opa])
	print(ls)


criar_diretorio()
criar_arquivos()
listar_arquivos()

