import numpy as np
import matplotlib.pyplot as plt


g = lambda x: np.cos(x)
h = lambda x: np.sin(x)

x = np.linspace(0, 10, 100)

plt.plot(x, g(x), label='cosinus')
plt.plot(x, h(x), 'r--', label='sinus')

plt.xlabel('Temps')
plt.ylabel('Posicio')
plt.title('Funcions')
plt.legend(loc=1)
plt.text(4, 0, 'Test')
plt.grid()
plt.show()
