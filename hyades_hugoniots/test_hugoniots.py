import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df_normal = pd.read_csv("MgO_hugonoit.csv")
df_hyades = pd.read_csv("MgO_hugoniot_better.csv")
df_russsian = pd.read_csv("Mgo_hugoniot_russian.csv")
plt.plot(df_normal.pressure, df_normal.density, label = "normal", c = "blue")
plt.plot(df_hyades.pressure, df_hyades.density, label = "hyades", c = "red", ls = ':')
plt.plot(df_russian.pressure, df_russian.density, label = "russian", c = "green", ls = '--')
plt.lengend()
plt.xlabel("pressure (GPa)")
plt.ylabel("density (g/cc)")
plt.title("MgO")
plt.show()
