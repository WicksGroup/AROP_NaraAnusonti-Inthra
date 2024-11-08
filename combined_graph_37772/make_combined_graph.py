import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
m_MgO = 40.304
m_qtz = 60.084
m_Fo = 140.666
a = 4.762
b = 10.244
c = 5.989
aIII = 2.640
bIII = 8.596
cIII = 9.04
a_q = 4.92
c_q = 5.43
pressure = 260
reflections_MgO = [["111",1.8],["200",1],["220",1]]
reflections_Fo = [["020",2],["110",2.75],["130",1]]
reflections_FoIII = [["020",2.5],["022",1],["110",1]]
reflections_qtz = [["001",2],["100",1.5],["002",1]]
points = {"35":[2.461,0.001,"silver"],"42":[2.059,0.002,"crimson"],"50":[1.743,0.001,"darkorange"],"60":[1.491,0.001,"darkgreen"],"72":[1.249,0.001,"blue"],"76":[1.205,0.0002,"silver"]}
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
df_MgO = pd.read_csv("MgO_hugonoit.csv")
df_qtz = pd.read_csv("quartz hugoniot.csv")
df_Fo = pd.read_csv("forsterite_hugoniot.csv")
for x in reflections_MgO:
    plt.plot(df_MgO.pressure, df_MgO.density.apply(dspacing_cubic, args = (x[0],6,m_MgO,)), label = f"MgO B1, {x[0]}", lw = x[1], c = "cornflowerblue")
for x in reflections_Fo:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x[0],a,b,c,m_Fo,)), label = f"Fo, {x[0]}", ls = ':',lw = x[1], c = "salmon")
for x in reflections_FoIII:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x[0],aIII,bIII,cIII,m_Fo,)), label = f"Fo III, {x[0]}", ls = '--', lw = x[1], c = "mediumorchid")
for x in reflections_qtz:
    plt.plot(df_qtz.pressure, df_qtz.density.apply(dspacing_hexagonal, args = (x[0],a_q,c_q,m_qtz,)), label = f"Qtz, {x[0]}", ls = '-.', lw = x[1], c = "lightgreen")
for key in points.keys():
    mypoints = points[key]
    plt.scatter(pressure,mypoints[0], c = mypoints[2], marker = "d")
    plt.errorbar(pressure, mypoints[0], yerr = mypoints[1], ecolor = "black")
plt.axhline(y=2.327, c = "sandybrown", label = "LiF, 111")
plt.axhline(y=2.015, c = "sandybrown", label = "LiF, 200")
plt.axhline(y=1.425, c = "sandybrown", label = "LiF, 220")
plt.legend(loc = 'upper right')
plt.title("d-spacing MgO B1, Fo, Fo III")
plt.xlabel("pressure (GPa)")
plt.ylabel("d-spacing (a)")
plt.savefig("combined_graph_dspacing.png", dpi = 600)
plt.show()