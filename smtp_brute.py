#!/usr/bin/python

import socket,sys,re

# Definindo códigos de cor ANSI
cor_pk = '\033[38;5;220m'  # FEB63E
cor_smtp = '\033[38;5;197m'  # F5055C
cor_erro = '\033[38;5;196m'  # E10406
cor_verde = '\033[92m'  # 00FF00
reset = '\033[0m'  # Reset para as configurações padrão de cor

if len(sys.argv) != 3:
	print ("-----------------------------------------------------------------")
	print (f' {cor_pk}Pk\'s Academy{reset} - {cor_smtp}SMTP BRUTE FORCE{reset} ')
	print ("-----------------------------------------------------------------")
	print ("Modo de uso: python3 smtpenum.py IP lista")
	print ("-----------------------------------------------------------------")
	print ("Forma de uso: python3 37.59.174.225 /home/arthurcortesr/lista.txt")
	print ("-----------------------------------------------------------------")
	sys.exit(0)

print (f'----------------------------------')
print (f'| {cor_pk}Pk\'s Academy{reset} - {cor_smtp}SMTP BRUTE FORCE{reset}| ')
print (f'----------------------------------')
print ('\n')


file = open(sys.argv[2])
for linha in file:
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((sys.argv[1],25))
	banner = tcp.recv(1024)
	tcp.send("VRFY "+linha)
	user = tcp.recv(1204)
	if re.search("252",user):
		print ("Usuario encontrado: "+user.strip("252 2.0.0"))
