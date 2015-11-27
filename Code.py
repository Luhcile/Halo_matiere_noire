import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
#from pandas import DataFrame, read_csv
#from scipy import stats
#from math import sqrt

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

def main() : 
    """ 
        Fonction principale du script python 
    """
    recuperation_donnees('Training_halos.csv')

main()
