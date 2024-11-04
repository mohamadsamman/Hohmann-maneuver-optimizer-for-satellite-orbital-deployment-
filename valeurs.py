import numpy as np

#converting into seconds to be used to calculate a
earthDayInSeconds=60.*60*24
numberOfEarthDaysInAYear=365.25
earthYearInSeconds=earthDayInSeconds*365.25 #unused here

#Calculating T and a
T=earthDayInSeconds*(360./(360.+(360./numberOfEarthDaysInAYear))) #période en s
muT=3.9860064*1e14 #m³/s²
a = (muT*(T/(2.*np.pi))*(T/(2.*np.pi)))**(1./3) #demi-grand axe en m

#some more constants
rT=6378140. #radius of the Earth
