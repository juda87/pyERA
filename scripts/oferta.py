import numpy as np

def cdc(caudal_diario):
	'''Toma una serie historica de datos y genera un diccionario con los objetos: 
	percentiles, q50, q75 y q80'''
	caudal_diario = np.array(caudal_diario)
	perc = range(0,101,1)
	percentiles = np.percentile(caudal_diario,perc)
	q50 = np.percentile(caudal_diario,50)
	q75 = np.percentile(caudal_diario,75)
	q85 = np.percentile(caudal_diario,85)
	curva_caudales = np.percentile(caudal_diario,perc)
	return({'q50':q50, 'q75':q75, 'q85':q85,'curva':curva_caudales})
	
def ia(etp,etr):
	'''Toma los datos mensuales de ETP y ETR y calcula el Indice de Aridez'''
	ia=(etp-etr)/etr
	if ia >= 0.6:
		categoria = 'Altamente deficitario de agua'
	elif ia >= 0.5:
		categoria = 'Deficitario de agua'
	elif ia >= 0.4:
		categoria = 'Entre moderado y deficitario de agua'
	elif ia >= 0.3:
		categoria = 'Moderado'
	elif ia >= 0.2:
		categoria = 'Entre moderado y excedentes de agua'
	elif ia >= 0.15:
		categoria = 'Excedentes de Agua'
	else:
		categoria = 'Altos excedentes de agua'
	return([categoria,ia])
	
def iua(dh,ohrd):
	'''Toma los datos de Demanda Hídrica (L/seg) y Oferta Hídrica(L/seg) y calcula el Indice de Uso del Agua'''
	iua=(dh/ohrd)*100
	if iua > 50:
		categoria = 'Muy Alto'
	elif iua > 20:
		categoria = 'Alto'
	elif iua > 10:
		categoria = 'Moderado'
	elif ia > 1:
		categoria = 'Bajo'
	else:
		categoria = 'Muy Bajo'
	return([categoria,iua])
		
	

	
