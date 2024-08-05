import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
import random
pressure = 260
m_Fo = 140.666
m_g = 2.335815477E-22
a = 4.762
b = 10.244
c = 5.989
aIII = 2.640
bIII = 8.596
cIII = 9.04
points_higher = {"42":[2.059,0.002],"50":[1.743,0.001],"60":[1.491,0.001],"72":[1.249,0.001]}
def density_orthorhombic(x,a0,b0,c0,m,d):
    v0 = a0*b0*c0
    h = eval(x[0])
    k = eval(x[1])
    l = eval(x[2])
    c_r = c0/a0
    b_r = b0/a0
    cc = c_r**2
    bc = b_r**2
    a_calc = math.sqrt(((d**2)*((h**2)*cc*bc+(k**2)*cc+(l**2)*bc))/(cc*bc))
    print (a_calc)
    r = a0/a_calc
    r3 = r**3
    v = v0/r3
    return m/v
    '''v0 = a0*b0*c0
    h = eval(x[0])
    k = eval(x[1])
    l = eval(x[2])
    v = m/rho
    p0 = v0/v
    p = p0**(1/3)
    a = a0/p
    b = b0/p
    c = c0/p
    return 1/math.sqrt(eval(h)**2/a**2+eval(k)**2/b**2+eval(l)**2/c**2)'''
df_Fo = pd.read_csv("forsterite_hugoniot.csv")
df_FoIII = pd.read_csv("FoIII_pressure-volume.csv")
plt.plot(df_Fo.pressure, df_Fo.density, label = "Fo")
plt.plot(df_FoIII.pressure, ((m_g*10**24)*4)/df_FoIII.volume, label = "FoIII")
points_Fo = [[2.059,"020","42"],[2.059,"110","42"],[1.743,"110","50"],[1.249,"130","72"]]
points_FoIII = [[2.059,"020","42"],[1.491,"022","60"]]
for x in points_Fo:
    plt.scatter(pressure,density_orthorhombic(x[1],a,b,c,m_Fo,x[0]), marker = "o",label = f"Fo, {x[2]} 2-theta, {x[1]}", c = (random.random(),random.uniform(0.5,1),random.uniform(0,0.5)))
for x in points_FoIII:
    plt.scatter(pressure,density_orthorhombic(x[1],a,b,c,m_Fo,x[0]), marker = "d",label = f"FoIII, {x[2]} 2-theta, {x[1]}", c = (random.uniform(0.5,1),0,random.random()))
plt.legend()
plt.title("Fo p-rho")
plt.xlabel("pressure (GPa)")
plt.ylabel("density (g/cc)")
plt.savefig("combined_graph_p-rho.png", dpi = 600)
plt.show()
'''m_MgO = 40.304
m_Fo = 140.666
a = 4.762
b = 10.244
c = 5.989
aIII = 2.640
bIII = 8.596
cIII = 9.04
pressure_lower = 150
pressure_higher = 260
reflections_MgO = [["111",1.8],["200",1],["220",1]]
reflections_Fo = [["020",2],["110",2.75],["130",1]]
reflections_FoIII = [["020",2.5],["022",1],["110",1]]
points_lower = {"49":[1.774,0.0002],"59":[1.506,0.0002],"64":[1.387,0.01],"69":[1.307,0.001],"74":[1.236,0.0001]}
points_higher = {"42":[2.059,0.002],"50":[1.743,0.001],"60":[1.491,0.001],"72":[1.249,0.001]}
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
df_Fo = pd.read_csv("forsterite_hugoniot.csv")
for x in reflections_MgO:
    plt.plot(df_MgO.pressure, df_MgO.density.apply(dspacing_cubic, args = (x[0],6,m_MgO,)), label = f"MgO B1, {x[0]}", lw = x[1], c = "cornflowerblue")
for x in reflections_Fo:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x[0],a,b,c,m_Fo,)), label = f"Fo, {x[0]}", ls = ':',lw = x[1], c = "salmon")
for x in reflections_FoIII:
    plt.plot(df_Fo.pressure, df_Fo.density.apply(dspacing_orthorhombic, args = (x[0],aIII,bIII,cIII,m_Fo,)), label = f"Fo III, {x[0]}", ls = '--', lw = x[1], c = "mediumorchid")
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
plt.show()'''