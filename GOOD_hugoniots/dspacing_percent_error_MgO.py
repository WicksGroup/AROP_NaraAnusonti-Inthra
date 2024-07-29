from matplotlib import pyplot as plt 
import pandas as pd 
from scipy import interpolate
import math

#THINGS TO CHANGE:
pressure = 260
#write as [approx 2-theta, observed d-spacing, predicted orientation]
dspacing_actual = [["42",2.059,"111"],["50",1.743,"200"],["72",1.249,"220"]]

m = 40.304

def dspacing_cubic(rho,x,orientation,m):
    h = x[0]
    k = x[1]
    l = x[2]
    return math.sqrt((orientation*m/rho)**(2/3)/(eval(h)**2+eval(k)**2+eval(l)**2))

df = pd.read_csv("MgO_hugonoit.csv")
#best fit equation
f = interpolate.interp1d(df.pressure,df.density, fill_value = 'extrapolate')
#add an extra space for readability
print()
#print all the data
for x in dspacing_actual:
    dspacing_predicted = dspacing_cubic(f(pressure),x[2],6,m)
    print(f"percent error: {round((abs(x[1]-dspacing_predicted)/dspacing_predicted)*100,2)}% \nobserved d-spacing: {x[1]} \n2-theta: {x[0]} \norientation: {x[2]} \n")