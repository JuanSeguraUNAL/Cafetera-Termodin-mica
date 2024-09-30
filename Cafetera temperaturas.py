import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_excel('Datos Termo.xlsx', sheet_name='Hoja1')

I = 1
V = 120
P = I * V

Tiempo = datos.iloc[0:, 0]
Tiempo = [float(i) for i in Tiempo]

Q = [P * i for i in Tiempo]

Tinf = datos.iloc[0:, 1]
Tinf = [float(i) + 273.15 for i in Tinf]

Tmed = datos.iloc[0:, 2]
Tmed = [float(i) + 273.15 for i in Tmed]

Tsup = datos.iloc[0:, 3]
Tsup = [float(i) + 273.15 for i in Tsup]

plt.scatter(Q, Tinf, label= 'Inferior', color= 'orange')
plt.scatter(Q, Tmed, label= 'Media', color= 'blue')
plt.scatter(Q, Tsup, label= 'Superior', color= 'red')
plt.legend()
plt.xlabel('Calor suministrado (J)')
plt.ylabel('Temperatura (K)')
plt.grid()
plt.savefig('Calor vs Temperatura.png')
plt.show()
