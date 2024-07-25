import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df_normal = pd.read_csv("Forsterite hugonoit.csv")
df_root = pd.read_csv("forsterite_hugoniot_root.csv")
df_Chidester = pd.read_csv("forsterite_hugoniot_Chidester.csv")
plt.plot(df_normal.pressure, df_normal.density, label = "normal", c = "blue")
plt.plot(df_Chidester.pressure, df_Chidester.density, label = "Chidester", c = "green", ls = '--')
plt.plot(df_root.pressure, df_root.density, label = "root", c = "red", ls = ':')
plt.legend()
plt.xlabel("pressure (GPa)")
plt.ylabel("density (g/cc)")
plt.title("forsterite")
plt.show()