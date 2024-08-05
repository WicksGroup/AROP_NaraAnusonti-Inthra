import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
m_Fo = 140.666
m_g = 2.335815477E-22
df_Fo = pd.read_csv("forsterite_hugoniot.csv")
df_FoIII = pd.read_csv("FoIII_pressure-volume.csv")
df_Fo_weird = pd.read_csv("possible weird forsterite.csv")
v_angstrom = df_FoIII.volume
v_cc = v_angstrom*10**-24
d = m_g/v_cc
plt.plot(df_FoIII.pressure, d*4, label = "test")

plt.plot(df_Fo.pressure, df_Fo.density, label = "Fo")
plt.plot(df_FoIII.pressure, ((m_g*10**24)*4)/df_FoIII.volume, label = "FoIII")
plt.plot(df_Fo_weird.pressure, ((m_g*10**24)*4)/df_Fo_weird.volume, label = "Fo weird")
plt.legend()
plt.show()