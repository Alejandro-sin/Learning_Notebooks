# Regresión lineal, que peudo correr en collab.
import numpy as np
import matplotlib.pyplot as plt




# Esto son la variabel independiente
x = np.array([0,1,2,4 ])

# Esta es mi dependiente, resutlado de experimentos
y = np.array([1,3,4,5])

# Me permite tomar ecnontrar los cefiioentes lienales para neustra función lineal.
coeffs = np.polyfit(x, y, 1)
a = coeffs[0]
b = coeffs[1]
estimado_y = (a *x) +b

# Me permite hacer el gráfico linea
plt.plot(x, estimado_y)
# Me permite ver los datos sctaer
plt.scatter(x,y)
plt.show()