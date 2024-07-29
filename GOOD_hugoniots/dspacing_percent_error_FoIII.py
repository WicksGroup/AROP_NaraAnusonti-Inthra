from matplotlib import pyplot as plt 
import pandas as pd 
from scipy import interpolate
import math

#THINGS TO CHANGE:
pressure = 260
#write as [approx 2-theta, observed d-spacing, predicted orientation]
dspacing_actual = [["42",2.059,"020"],["60",1.491,"022"],["72",1.249,"110"]]

m = 140.666
a = 2.640
b = 8.596
c = 9.04

def dspacing_orthorhombic(rho,x,a0,b0,c0,m):
    v0 = a0*b0*c0
    h = x[0]
    k = x[1]
    l = x[2]
    v = m/rho
    p0 = v0/v
    p = p0**(1/3)
    a = a0/p
    b = b0/p
    c = c0/p
    return 1/math.sqrt(eval(h)**2/a**2+eval(k)**2/b**2+eval(l)**2/c**2)

df = pd.read_csv("forsterite_hugoniot.csv")
#best fit equation
f = interpolate.interp1d(df.pressure,df.density, fill_value = 'extrapolate')
#add an extra space for readability
print()
#print all the data
for x in dspacing_actual:
    dspacing_predicted = dspacing_orthorhombic(f(pressure),x[2],a,b,c,m)
    print(f"percent error: {round((abs(x[1]-dspacing_predicted)/dspacing_predicted)*100,2)}% \nobserved d-spacing: {x[1]} \n2-theta: {x[0]} \norientation: {x[2]} \n")
    