import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_excel(r"C:\Users\techm\OneDrive\Bureau\log_position_SV_car2.xlsx")
x=list(df['temps'])
y=list(df['normalise'])


plt.plot(x, y, 'r-', linewidth=1)
plt.xlabel('temps en seconde')
plt.ylabel('erreur normalisée')
plt.grid()
plt.show()

