import pandas as pd
from pdb import set_trace
from scipy import interpolate
import matplotlib.pyplot as plt
input_pressure = input("What pressure? ")
df = pd.read_csv("forsterite_hugoniot.csv")
plt.plot(df.pressure,df.density,'b-',label='data')
#plt.show()
f = interpolate.interp1d(df.pressure,df.density, fill_value = 'extrapolate')
fint=[]
for ix in df.pressure:
    fint.append(f(ix))
plt.plot(df.pressure,fint,'r--',label="interpolated")
plt.scatter(input_pressure,f(input_pressure), label="extrapolated", c = "purple", marker = "D")
plt.xlabel('Pressure (GPa)')
plt.ylabel('Density (a)')
plt.legend()
#plt.show()
print(f(input_pressure))

