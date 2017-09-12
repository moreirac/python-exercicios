#!/usr/bin/env python3

import docker
import argparse
import sys
from datetime import datetime


def logando(mensagem, e='', logfile='docker-cli.log'):
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(logfile, 'a') as log:
        texto = '%s \t %s \t %s \t\n' % (data_atual, mensagem, str(e))
        log.write(texto)


def criar_container(args):
    try:
        client = docker.from_env()
        executando = client.containers.run(args.imagem, args.comando)
        print(executando)
        return executando
    except docker.errors.ImageNotFound as e:
        logando('Erro: Essa imagem nao existe!', e)
    except docker.errors.NotFound as e:
        logando('Erro: Esse comando nao existe!', e)
    except Exception as e:
        logando('Erro! Favor verificar o comando digitado', e)
    finally:
        print('Comando executado!')


def listar_containers(args):
    try:
        client = docker.from_env()
        get_all = client.containers.list(all=True)

        for cada_container in get_all:
            #print(cada_container)
            conectando = client.containers.get(cada_container.id)
            print("O container %s utiliza a imagem %s rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))
    except Exception as e:
        logando('Erro! Favor verificar o comando digitado', e)


def procurar_container(args):
    try:
        client = docker.from_env()
        get_all = client.containers.list(all=True)
        imagem = args.imagem

        for cada_container in get_all:
            #print(cada_container)
            conectando = client.containers.get(cada_container.id)
            if str(imagem).lower() in str(conectando.attrs['Config']['Image']).lower():
                print("Achei o container %s que contem a palavra %s no nome de sua imagem: %s" % (conectando.short_id, imagem, conectando.attrs['Config']['Image']))
    except Exception as e:
        logando('Erro! Favor verificar o comando digitado', e)


def remover_container(args):
    try:
        client = docker.from_env()
        get_all = client.containers.list(all=True)

        for cada_container in get_all:
            conectando = client.containers.get(cada_container.id)
            ports = conectando.attrs['HostConfig']['PortBindings']

            tem_porta = False
            if not ports is None:
                for port in ports:
                    for bind in ports[port]:
                        if int(bind['HostPort']) <= 1024:
                            print('Remover...')
                            print(bind)
                            tem_porta = True

            if tem_porta:
                conectando.remove(force=True)
    except Exception as e:
        logando('Erro! Favor verificar o comando digitado', e)


def remover_container2():
    try:
        client = docker.from_env()
        get_all = client.containers.list(all=True)

        for cada_container in get_all:
            conectando = client.containers.get(cada_container.id)
            portas = conectando.attrs['HostConfig']['PortBindings']

            if isinstance(portas, dict):
                for porta, porta1 in portas.items():
                    porta1 = str(porta1)
                    porta2 = ''.join(filter(str.isdigit, porta1))
                    if int(porta2) <= 1024:
                        print('Removendo o container %s que esta escutando na porta %s e bindando no host na porta %s' % (cada_container.id, porta, porta2))
                        removendo = cada_container.remove(force=True)
    except Exception as e:
        logando('Erro! Favor verificar o comando digitado', e)


parser = argparse.ArgumentParser(description='docker-cli criado na aula de python')
subparser = parser.add_subparsers()
criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem', required=True)
criar_opt.add_argument('--comando', required=True)
criar_opt.set_defaults(func=criar_container)

criar_opt = subparser.add_parser('listar')
criar_opt.set_defaults(func=listar_containers)

criar_opt = subparser.add_parser('procurar')
criar_opt.add_argument('--imagem', required=True)
criar_opt.set_defaults(func=procurar_container)

criar_opt = subparser.add_parser('remover')
criar_opt.set_defaults(func=remover_container)

cmd = parser.parse_args()
cmd.func(cmd)


#listar_containers()
#criar_container("alpine", "echo VAIIII")
#print('-----')
#procurar_container('alp')
#remover_container() # Remover todos os containers que estao bindando portas baixas no host | < 1024
#remover_container2()







