import numpy as np
import os

def recuperation_donnees (csv_file):
	"""
        Lit le fichier de donnees, en ne selectionnant que les SkiId avec 1 seul halo
         Args: csv_file (str) : nom du fichier a lire
         Returns: numpy.array : array
	"""
	data = np.loadtxt(csv_file, dtype=np.str, delimiter=',', skiprows=1)
	skyid = []
	for i in range(len(data[:,0])):
		if data[i,1]=='1' :
			skyid.append([data[i,0], data[i,2], data[i,3], data[i,4], data[i,5]])
	return skyid


def files_recuperation(folder_name, skyId):	
	
	#for name in skyId[:][0]:
	for i in range(len(skyId)):
		name = skyId[i][0]
		s = folder_name + '/Training_' + name + '.csv'
		data_name = 'data_' + name		
		#data_name = np.loadtxt(s, dtype=np.str, delimiter=',', skiprows=1)
		print s
	return data_name

def carre(data):

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
	print data
	carre(data)

main()
