######################################################################################
#                                   Projet UE 5.2                                    #
#                               Halo de matiere noire                                #
# Autors :  ERARD Thibault, MARIE JOSEPH Bernadette, MONNIER Heloise et VARIN Lucile #
# Date of creation : 06/11/15                                                        #
# Date derniere modification : 11/12/15                                              #
######################################################################################

import numpy as np
import os
import csv as c

def recuperation_donnees (csv_file):
	"""
        Lit le fichier de donnees, en ne selectionnant que les SkiId avec 1 seul halo
        :Args csv_file (str) : nom du fichier a lire
        :Returns skyid (liste de liste)
	"""
	data = np.loadtxt(csv_file, dtype=np.str, delimiter=',', skiprows=1)
	skyid = []
	for i in range(len(data[:,0])):
		if data[i,1]=='1' :
			skyid.append([data[i,0], data[i,2], data[i,3], data[i,4], data[i,5]])
	return skyid

def files_recuperation(folder_name, skyId):	
	"""
	Fonction permettant de réccupérer dans une liste (data_name) l'ensemble des noms de fichiers dont le skiID contient 1 halo. 
	:Args folder_name, skyId
	:Return data_name
	"""
	data_name = []
	for i in range(len(skyId)):
		name = skyId[i][0]
		data_name.append(folder_name + '/Training_' + name + '.csv')		
	return data_name


def carre(data):
	"""
	Fonction permettant de sélectionner un carré de 1680x1680 proche d'un halo et loin. 
	Creer une liste de liste (carre_proche) des galaxies étant à +/- 840 en x et y du halo 
	Creer une liste de liste (carre_loin) des galaxies étant à une distance x2 des coordonnées du halo
	:Args data
	:Return carre_loin, carre_proche
	"""

	carre_proche = {}
	carre_loin = {}
	for file_name in data:
		file = np.loadtxt(file_name, dtype=np.str, delimiter=',', skiprows=1)
		GalaxyID, x, y, e1, e2 = file[:,0],file[:,1], file[:,2], file[:,3], file[:,4]
		for i in range(len(GalaxyID)):
			if (float(e1[i])-840 <= float(x[i])) and (float(e1[i])+840 >= float(x[i])) and (float(e2[i])-840 <= float(y[i])) and (float(e2[i])+840 > float(y[i])):
				if file_name not in carre_proche:
					carre_proche[file_name] = [GalaxyID[i], e1[i], e2[i]]
				else:
					carre_proche[file_name] = carre_proche[file_name] + [GalaxyID[i], e1[i], e2[i]]
			elif (float(x[i]) >= float(e1[i])*2) and (float(x[i]) < float(e1[i])*2 > float(x[i])) and (float(e2[i])*2 < float(y[i])) and (float(e2[i])+840 > float(y[i])):
				if file_name not in carre_loin:
					carre_loin[file_name] = [GalaxyID[i], e1[i], e2[i]]
				else:
					carre_loin[file_name] = carre_proche[file_name] + [GalaxyID[i], e1[i], e2[i]]
	return carre_proche, carre_loin


def ellipticite (carre_loin, carre_loin):
	"""
	Fonction qui calcul l ellipticite en fonction de e1 et e2 de chaqeu galaxie
	:Args carre_loin, carre_proche
	:Return 
	"""
	

def prediction ():
	"""
	à compléter
	:Args 
	:Return 
	"""
	Data1 = np.loadtxt('Maximum_likelihood_Benchmark.txt',dtype=np.str,delimiter=',')
	Data2= np.loadtxt('Training_halos.txt',dtype=np.str,delimiter=',')
	tab1 = []
	tab2 = []
	for i in range(len(Data1)) :
		diff_x1 = float(Data1[i][1]) - float(Data2[i][2])
		diff_y1 = float(Data1[i][2]) - float(Data2[i][3])
		tab1.append(diff_x1)
		tab2.append(diff_y1)
	tabx = np.savetxt('DifferenceDesx.txt',tab1)
	taby = np.savetxt('DifferenceDesy.txt',tab2)
	return tabx,taby

def main() :
	"""
        Fonction principale du script python
	: intégrer prediction 
	"""
	skyid = recuperation_donnees('Training_halos.csv')
	
	data_files = files_recuperation('Train_Skies', skyid)
	print carre(data_files)
main()
