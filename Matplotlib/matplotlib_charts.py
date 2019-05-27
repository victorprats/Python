# https://matplotlib.org/
# -------------
#   Example 1
# -------------

import numpy as np
import matplotlib.pyplot as plt


g = lambda x: np.cos(x)
h = lambda x: np.sin(x)

x = np.linspace(0, 10, 100)

plt.plot(x, g(x), label='cosinus')
plt.plot(x, h(x), 'r--', label='sinus')


plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Functions')
plt.legend(loc=1)
plt.text(4, 0, 'Test')
plt.grid()
plt.show()

# -------------
#   Example 2
# -------------

x1 = (1, 2, 4, 6, 8, 10, 13)
y1 = (3, 5, 2, 7, 2, 18, 5)

x2 = (1, 3, 5, 7, 9, 10, 12)
y2 = (8, 5, 6, 8, 6, 2, 6)


plt.plot(x1, y1,  marker='^', markerfacecolor='yellow', label='line 1')
plt.plot(x2, y2,  marker='^', markerfacecolor='blue', label='line 2', markersize='10', linewidth='2', linestyle='-.')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line chart')
plt.legend(loc=1)
plt.grid()
plt.show()

# -------------
#   Example 3
# -------------
x1 = (1, 2, 4, 6, 8, 10, 12, 13, 15, 17, 19, 22, 23, 24, 27)
y1 = (3, 5, 12, 7, 14, 5, 6, 4, 3, 7, 16, 8, 12, 9, 13)

plt.scatter(x1, y1, marker='*', s=50, color='deeppink')

plt.title('Scatter plot')
# plt.grid()
plt.show()

# -------------
#   Example 4
# -------------
x = [5, 2, 9, 4, 7, 3, 8, 6]
y = [10, 5, 8, 4, 2, 9, 7, 11]

# Function to plot the bar
plt.bar(x, y)

plt.title('Bar chart')
plt.show()
