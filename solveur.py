'''L'idée est d'avoir toutes les valeurs importantes dans un fichier, les formules importantes dans 
un autres (probablement une image parceque la fleme) et un fichier solveur'''
import numpy as np
import scipy.optimize as op
from valeurs import *


#To calculate the speed with a given radius r
def speed(r):
    return (muT*((2./r) - (1./a)))**(1./2)

#test speed
print(speed(36000000+rT),np.sqrt(muT/(36000000+rT)))