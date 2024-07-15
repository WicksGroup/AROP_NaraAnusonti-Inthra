import pandas as pd
from pdb import set_trace
from scipy import interpolate
import matplotlib.pyplot as plt 
df = pd.read_csv("MgO_hugonoit.csv",header = None)
plt.plot(df[1],df[0],'b-',label='data')
#plt.show()
f = interpolate.interp1d(df[1],df[0], fill_value = 'extrapolate')
fint=[]
for ix in df[1]:
    fint.append(f(ix))
    print(ix,f(ix))
plt.plot(df[1],fint,'r--',label="interpolated")
plt.scatter(260,f(260), label="extrapolated", c = "purple", marker = "D")
plt.xlabel('Pressure (GPa)')
plt.ylabel('Density (a)')
plt.grid('--')
plt.legend()
plt.show()
#print (f(260),fill_value = 'extrapolate', bounds_error = False)
