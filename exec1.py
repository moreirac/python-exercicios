#!/usr/bin/env python3

import subprocess


def criar_diretorio():
	subprocess.call(['mkdir','/root/dir02'])


def criar_arquivos():
	for i in range(1,40):
		subprocess.call(['touch','/root/dir02/{}'.format(str(i))])


def listar_arquivos():
	ls = subprocess.check_output(['ls','-lha','/root/dir02'])
	print(ls)


criar_diretorio()
criar_arquivos()
listar_arquivos()

