from matplotlib import pyplot as plt 
import pandas as pd 
from scipy import interpolate
import math

#THINGS TO CHANGE:
pressure = 260
#write as [approx 2-theta, observed d-spacing, predicted orientation]
dspacing_actual = [["42",2.059,"100"],["72",1.249,"002"]]

m = 60.084
a = 4.92
c = 5.43

def dspacing_hexagonal(rho,x,a0,c0,m):
    v0 = math.sqrt(3)*a0**2*c0/2
    h = x[0]
    k = x[1]
    l = x[2]
    v = m/rho
    p0 = v0/v
    p = p0**(1/3)
    a = a0/p
    c = c0/p
    return 1/math.sqrt((4/3)*((eval(h)**2+eval(h)*eval(k)+eval(k)**2)/a**2)+eval(l)**2/c**2)

df = pd.read_csv("quartz hugoniot.csv")
#best fit equation
f = interpolate.interp1d(df.pressure,df.density, fill_value = 'extrapolate')
#add an extra space for readability
print()
#print all the data
for x in dspacing_actual:
    dspacing_predicted = dspacing_hexagonal(f(pressure),x[2],a,c,m)
    print(f"percent error: {round((abs(x[1]-dspacing_predicted)/dspacing_predicted)*100,2)}% \nobserved d-spacing: {x[1]} \n2-theta: {x[0]} \norientation: {x[2]} \n")