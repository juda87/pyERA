import pandas as pd 
import numpy as np
import math

matriz = pd.read_excel ('C:\\Users\\julio\\Documents\\PERSONAL\\JUEGO_PY\\Excel\\morfo.xlsx')



def morfometrico(Pendiente, Densidad, coeficiente):

	if Pendiente == 1:
		corte_1 = matriz ['P_1']
	elif Pendiente == 2:
		corte_1 = matriz ['P_2']
	elif Pendiente == 3:
		corte_1 = matriz ['P_3']
	elif Pendiente == 4:
		corte_1 = matriz ['P_4']
	elif Pendiente == 5:
		corte_1 = matriz ['P_5']

	# print (corte_1)

	if Densidad == 1:
		corte_2 = corte_1 [0:5]
	elif Densidad == 2:
		corte_2 = corte_1 [5:10]
	elif Densidad == 3:
		corte_2 = corte_1 [10:15]
	elif Densidad == 4:
		corte_2 = corte_1 [15:20]
	elif Densidad == 5:
		corte_2 = corte_1 [20:25]

	# print (corte_2)

	if coeficiente == 1:
		corte_3 = corte_2[0:1]
	elif coeficiente == 2:
		corte_3 = corte_2[1:2]
	elif coeficiente == 3:
		corte_3 = corte_2[2:3]
	elif coeficiente == 4:
		corte_3 = corte_2[3:4]
	elif coeficiente == 5:
		corte_3 = corte_2[4:5]
	
	print (int (corte_3))

if __name__ == '__main__':
	Pendiente = int(input('Ingrese pendiente: '))
	Densidad = int(input('Ingrese Densidad: '))
	coeficiente = int(input('Ingrese coeficiente: '))

	morfometrico(Pendiente, Densidad, coeficiente)
 	

