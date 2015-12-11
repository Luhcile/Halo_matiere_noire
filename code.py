######################################################################################
#                                   Projet UE 5.2                                    #
#                               Halo de matiere noire                                #
# Autors :  ERARD Thibault, MARIE JOSEPH Bernadette, MONNIER Heloise et VARIN Lucile #
# Date of creation : 06/11/15                                                        #
# Date derniere modification : 11/12/15                                              #
######################################################################################

import numpy as np
import os

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
	carre_proche = []
	carre_loin = []
	GalaxyID, x, y, e1, e2 = data[:,0], data[:,1], data[:,2], data[:,3], data[:,4]
	for galaxy in GalaxyID:
		if (data[:,4]-840 <= x) and (data[:,4]+840 >= x) and (data[:,5]-840 <= y) and (data[:,5]+840 > y):
			carre_proche.append([GalaxyID, x , y, e1, e2])
		
		elif (x >= data[:,4]*2) and (x < data[:,4]*2 > x) and (data[:,5]*2 < y) and (data[:,5]+840 > y):
			carre_loin.append([GalaxyID, x, y, e1, e2])

def main() :
	"""
        Fonction principale du script python
	"""
	skyid = recuperation_donnees('Training_halos.csv')
	data = files_recuperation('Train_Skies', skyid)
	carre(data)

main()
