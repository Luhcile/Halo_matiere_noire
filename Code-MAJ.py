import numpy as np
import os

def recuperation_donnees (csv_file):
	"""
        Lit le fichier de donnees, en ne sélectionnant que les SkiId avec 1 seul halo
         Args: csv_file (str) : nom du fichier a lire
         Returns: numpy.array : array
	"""
	data = np.loadtxt(csv_file, dtype=np.str, delimiter=',', skiprows=1)
	skyid = []
	for i in range(len(data[:,0])):
		if data[i,1]=='1' :
			skyid.append(data[i,0])
			skyid.append(data[i,2])
			skyid.append(data[i,3])
			skyid.append(data[i,4])
			skyid.append(data[i,5])
	return skyid


def files_recuperation(folder_name, skyId):	
	keptskies = os.listdir(folder_name)
	training_skies = []
	for name in skyId:
		s = 'Training_' + name
		if s in keptskies:
			training_skies.append(s)
			data = np.loadtxt(s, dtype=np.str, delimiter=',', skiprows=1)
			GalaxyID, x, y, e1, e2 = data[:,0], data[:,1], data[:,2], data[:,3], data[:,4]

def main() :
	"""
        Fonction principale du script python
	"""
	skyid = recuperation_donnees('Training_halos.csv')
	files_recuperation('Train_Skies', skyid)

main()



# Comparaison Prediction VS Données 

import numpy as np
import csv as c
import difflib


Data1 = np.loadtxt(' Maximum_likelihood_Benchmark.txt',dtype=np.str,delimiter=',')
Data2= np.loadtxt('skyid.txt',dtype=np.str,delimiter=',')
 
out = open("Out.txt", 'w')
 
old = open(Data1, 'r')
old_lines = list(old)
old.close()
 
new = open(Data2, 'r')
new_lines = list(new)
new.close()
 
for line in unified_diff(old_lines, new_lines, fromfile= Data1, tofile=Data2):
    out.write(line)

