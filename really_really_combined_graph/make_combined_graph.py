import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
import random
m_MgO = 40.304
m_Fo = 140.666
a = 4.762
b = 10.244
c = 5.989
aIII = 2.640
bIII = 8.596
cIII = 9.04
pressure_lower = 150
pressure_higher = 260
reflections_MgO = [["200",1.5],["202",0.5],["311",0.5]]
reflections_Fo = [["002",1.1],["130",1.6],["022",1.2],["112",1.9]]
reflections_FoIII = [["022",1.75],["110",1],["112",0.75]]
points_lower = {"51":[1.734,0.025],"60":[1.485,0.002],"65":[1.387,0.02],"74":[1.234,0.03]}
points_higher = {"42":[2.059,0.003],"50":[1.743,0.03],"60":[1.491,0.01],"72":[1.249,0.001]}
#points = for higher {"35":[2.461,0.001,"silver"],"42":[2.059,0.002,"crimson"],"50":[1.743,0.001,"darkorange"],"60":[1.491,0.001,"darkgreen"],"72":[1.249,0.001,"blue"],"76":[1.205,0.0002,"silver"]}
#points = for lower {"49":[1.774,0.0002,"crimson"],"59":[1.506,0.0002,"darkorange"],"64":[1.387,0.01,"darkgreen"],"69":[1.307,0.001,"blue"],"74":[1.236,0.0001,"purple"]}
def dspacing_cubic(rho,x,orientation,m):
    h = x[0]
    k = x[1]
    l = x[2]
    return math.sqrt((orientation*m*1.661/rho)**(2/3)/(eval(h)**2+eval(k)**2+eval(l)**2))
def dspacing_orthorhombic(rho,x,a0,b0,c0,m):
    v0 = a0*b0*c0
    h = x[0]
    k = x[1]
    l = x[2]
    v = (m/rho)*1.661
    p0 = v0/v
    p = p0**(1/3)
    a = a0/p
    b = b0/p
    c = c0/p
    return 1/math.sqrt(eval(h)**2/a**2+eval(k)**2/b**2+eval(l)**2/c**2)
df_MgO = pd.read_csv("MgO_hugonoit.csv")
df_Fo = pd.read_csv("forsterite_hugoniot.csv")
df_FoIII = pd.read_csv("forsteriteIII_hugoniot.csv")
for x in reflections_MgO:
    plt.plot(df_MgO.pressure, df_MgO.density.apply(dspacing_cubic, args = (x[0],6,m_MgO,)), label = f"MgO B1, {x[0]}", lw = x[1], c = "cornflowerblue")
for x in reflections_Fo:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x[0],a,b,c,m_Fo,)), label = f"Fo, {x[0]}", ls = ':',lw = x[1], c = "salmon")
for x in reflections_FoIII:
    plt.plot(df_FoIII.pressure, df_FoIII.density.apply(dspacing_orthorhombic, args = (x[0],aIII,bIII,cIII,m_Fo,)), label = f"Fo III, {x[0]}", ls = '--', lw = x[1], c = "mediumorchid")
for key in points_lower.keys():
    mypoints = points_lower[key]
    plt.scatter(pressure_lower,mypoints[0], marker = "d",label = f"{key} 2-theta, {pressure_lower} GPa", c = (random.uniform(0.5,1),0,random.random()))
    plt.errorbar(pressure_lower, mypoints[0], yerr = mypoints[1], ecolor = "black")
for key in points_higher.keys():
    mypoints = points_higher[key]
    plt.scatter(pressure_higher,mypoints[0], marker = "o",label = f"{key} 2-theta, {pressure_higher} GPa", c = (random.random(),random.uniform(0.5,1),random.uniform(0,0.5)))
    plt.errorbar(pressure_higher, mypoints[0], yerr = mypoints[1], ecolor = "black")
plt.legend(loc = 'upper right')
plt.title("d-spacing MgO B1, Fo, Fo III")
plt.xlabel("pressure (GPa)")
plt.ylabel("d-spacing (a)")
plt.savefig("combined_graph_dspacing.png", dpi = 600)
plt.show()
