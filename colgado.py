# -*- coding: cp1252 -*-
from os import system
from paq.monito import *

global l1, l2, d1 
l1, l2, d1 = list(), list(), dict()


system('cls')

def vaciarTodo():

	c1 = 0

	while len(l1) > 0:

		l1.pop()

	while len(l2) > 0:

		l2.pop()

	d1.clear()



def game():

	

	terGame = False
	felic = False
	gameOver = False

	cprin = 0

	dd3 = "   "

	while terGame == False:

		v = 7
		cprin += 1

		if cprin > 1:

			vaciarTodo()
			frase()
			felic = False
			gameOver = False

		while felic == False and gameOver == False:

			s = ""

			while s == "":

				print ""
				print ""
				print "Le quedan", v, "vidas"
				if v > 0:

					animation(v)
				print ""
				pp = ""
				cl2 = 0

				for a in l2:

					cl2 += 1
					pp += a

				print pp

				print ""
				de = " _"
				ca = -1
				cfin = 0

				for a in l2:

					ca += 1

					if l2[ca] != de:

						cfin += 1


				if cfin == cl2:

					felic = True
					break

			
				s = raw_input("Ingrese una letra: ")
				system('cls')

			c = -1
			existeLetra = False
			contClave = -1
			cl = 0
			vc = ""

			for clave in d1:

				contClave += 1

			for a in l1:

				c += 1

				for clave in d1:

					vc += d1[clave]

				for clave in d1:

					if d1[clave] == s or vc == s:

						existeLetra = True
						cl += 1

						if clave == c:

							ss = " " + s

							l2[c] = ss

						elif vc == s:

							ct = -1

							for lr in s:

								ct += 1
								ss = " " + lr

								l2[ct] = ss

					elif cl == 0:

						existeLetra = False

			if existeLetra == False:

				v -= 1

				if v == 0:

					gameOver = True

			

		if felic == True:

			print ""
			print "-----------------------------"
			print "Felicitaciones! Has ganado :)"
			print "-----------------------------"
			print ""

		elif gameOver == True:

			dr = ""

			for a in l1:

				dr += a

			animation(v)

			print ""
			print "La frase era:", dr


		print ""
		print ""
		print ""

		system('pause')
		jugar = ""
		cposi = jugar != "1" and jugar != "si" and jugar != "SI" and jugar != "Si" and jugar != "sI"
		cnega = jugar != "2" and jugar != "no" and jugar != "NO" and jugar != "No" and jugar != "nO"


		while cposi == True and cnega == True:

			system('cls')

			print "¿Desea seguir jugando?"
			print "---------------------"
			print "1) Si"
			print "2) No"
			print "---------------------"
			jugar = raw_input("Opcion: ")
			cposi = jugar != "1" and jugar != "si" and jugar != "SI" and jugar != "Si" and jugar != "sI"
			cnega = jugar != "2" and jugar != "no" and jugar != "NO" and jugar != "No" and jugar != "nO"

		if cposi == False and cnega == True:

			terGame = False

		elif cposi == True and cnega == False:

			terGame  = True

		system('cls')

	if terGame == True:

		print ""
		print "-----------------------------"
		print "Gracias por jugar con nostros"
		print "le saluda PowerX producciones"
		print "-----------------------------"
		print ""
		s = raw_input("Presione ENTER para salir")

def frase():

	p = raw_input ("Ingrese frase: ")
	c, cd = 0, 0
	ca = -1
	d2 = " _"
	d3 = "  "
	ca = -1

	for a in p:

		ca += 1
		d1[ca] = a

		l1.append(a)
		
		if a != " ":

			l2.append(d2)

		elif a == " ":

			l2.append(d3)

	system('cls')

	# Revisar diccionario --> for a in d1:

	# 						      print a, ": ", d1[a]

frase()
game()


