import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

m_MgO = 40.304
m_LiF = 25.939
m_Fo = 140.666
a = 4.762
b = 10.244
c = 5.989
aIII = 2.640
bIII = 8.596
cIII = 9.04

pressure = 260
reflections_MgO = ["110","002"]
reflections_LiF_B1 = ["001","200"]
reflections_LiF_B2 = ["111","200"]
reflections_Fo = ["001","100","111","121"]
reflections_FoIII = ["020","100"]
points = {"35":[2.461,0.001,"red"],"37":[2.351, 0.001,"darkorange"],"42":[2.059,0.002,"darkgoldenrod"],"50":[1.743,0.001,"darkgreen"],"60":[1.491,0.001,"blue"],"72":[1.249,0.001,"purple"],"76":[1.205,0.0002,"deeppink"]}
def dspacing_cubic(rho,x,orientation,m):
    h = x[0]
    k = x[1]
    l = x[2]
    return math.sqrt((orientation*m/rho)**(2/3)/(eval(h)**2+eval(k)**2+eval(l)**2))
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
df_MgO = pd.read_csv("MgO_hugonoit.csv")
df_LiF = pd.read_csv("LiF hugonoit.csv")
df_Fo = pd.read_csv("Forsterite hugonoit.csv")
for x in reflections_MgO:
    plt.plot(df_MgO.pressure, df_MgO.density.apply(dspacing_cubic, args = (x,6,m_MgO,)), label = f"MgO B1, {x}", c = "blue")
for x in reflections_LiF_B1:
    plt.plot(df_LiF.pressure, df_LiF.density.apply(dspacing_cubic, args = (x,6,m_LiF,)), label = f"LiF B1, {x}", c = "red", linestyle = "dotted")
for x in reflections_LiF_B2:
    plt.plot(df_LiF.pressure, df_LiF.density.apply(dspacing_cubic, args = (x,8,m_LiF,)), label = f"LiF B2, {x}", c = "green", linestyle = "dashed")
for x in reflections_Fo:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x,a,b,c,m_Fo,)), label = f"Fo, {x}", c = "green", linestyle = "dashdot")
for x in reflections_FoIII:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x,aIII,bIII,cIII,m_Fo,)), label = f"Fo III, {x}", c = "green", linestyle = (0, (3,10,1,10)))
for key in points.keys():
    mypoints = points[key]
    plt.scatter(pressure,mypoints[0],label = f"point at {key} 2-theta", c = mypoints[2], marker = "d")
    plt.errorbar(pressure, mypoints[0], yerr = mypoints[1], ecolor = "black")
plt.legend(loc = 'upper right', bbox_to_anchor = (1.0,1.0), ncol = 4)
plt.title("d-spacing MgO B1")
plt.xlabel("pressure (GPa)")
plt.ylabel("d-spacing(a)")
plt.savefig("MgO_B1_dspacing.png")
plt.show()
