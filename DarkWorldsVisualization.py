#def PlotSkies(skynum,halos=True,estimated_positions=[]):
import numpy as np
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
import matplotlib.pyplot as plt

## Load galaxies in sky
x,y,e1,e2=np.loadtxt('Train_Skies/Training_Sky'+str(skynum)+'.csv',delimiter=',',unpack=True,usecols=(1,2,3,4),skiprows=1)
## Calculate inputs for matplotlib.patches.Ellipse
#multiply a and b by 50 for easy visualization
a = 1/(1-np.sqrt(e1**2+e2**2))*50
b = 1/(1+np.sqrt(e1**2+e2**2))*50
theta = np.degrees(np.arctan2(e2, e1)*0.5)
galaxydata = np.column_stack((x,y,a,b,theta))
## Load halo data
if halos:
    Training_halos = np.loadtxt('Training_halos.csv', unpack=False, usecols=(1,4,5,6,7,8,9), skiprows=1, delimiter=',')
    Training_halos = Training_halos[skynum-1]
    nhalo = int(Training_halos[0])
    Training_halos = np.reshape(np.delete(Training_halos,0,0),(-1,2))
## Start plotting
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
#plots galaxies
for x,y,a,b,theta in galaxydata:
    galaxy = Ellipse(xy=(x, y), width=a, height=b, angle=theta, fc='none')
    ax.add_patch(galaxy)
#plots halos
if halos:
    for i in range(nhalo):
        ax.add_patch(Circle(xy=(Training_halos[i][0], Training_halos[i][1]), fc='b', ec='none', alpha=0.5, radius=250))
#plots halos at specified positions
if len(estimated_positions) != 0:
    for i in range(len(estimated_positions)):
        ax.add_patch(Circle(xy=(estimated_positions[i][0], estimated_positions[i][1]), fc='r', ec='none', alpha=0.5, radius=250))
ax.autoscale_view(tight=True)
plt.show()


## Uses
#PlotSkies(200, halos=False)
#PlotSkies(200)
#
#import numpy as np
#PlotSkies(200,estimated_positions=np.array([[1000,1000],[2000,3000]]))


