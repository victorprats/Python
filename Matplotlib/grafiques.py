# Test

import numpy as np
import matplotlib.pyplot as plt
 
 
def h(x):
    return np.sin(x)

g = lamdba x: np.cos(x)

x = lambda x: np.cos(x)

x = np.linspace(0, 10, 100)

plt.plot(x, h(x), 'r--', label='sinus')
plt.plot(x, g(x), label='cosinus')

plt.xlabel('temps')
plt.ylabel('posició')
plt.title('Funció sinus')
plt.legend(loc=1)
plt.text(4, 0, 'Test')
plt.grid()
