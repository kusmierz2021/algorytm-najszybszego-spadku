from gradient_descent import gradient_descent
import numpy as np
import matplotlib.pyplot as plt



result, way = gradient_descent(
    gradient=lambda x: 2*x,          # gradient
    start=-18.5,                     # start point
    learning_rate=0.95               # learning rate (changing for tests)
)


x = np.arange(-20, 20, 0.1)          # comfortable size
y = x**2                             # our function
plt.plot(x, y)                       # drawing graph of the function

x_from_way = way
y_from_way = [x*x for x in x_from_way]
plt.plot(x_from_way, y_from_way, "o:", linewidth=1.5)          # drawing graph of the way to the result

plt.xlabel('learning rate = 0.95, needed iterations = ?')
plt.title('x^2 function')
plt.show()


# print(result)                      # useful while checking if algorithm works properly
# print(way)
