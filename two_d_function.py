from gradient_descent import gradient_descent
import numpy as np
import matplotlib.pyplot as plt


result, way = gradient_descent(
    gradient=lambda x: np.array([(x[0]+8) * (2 + (50 * np.sin(10 * ((x[0] + 8)**2 + (x[1] - 8)**2)**(1/2))) /
                                             (((x[0] + 8)**2 + (x[1] - 8)**2)**(1/2))), (x[1]-8) * (2 +
                                              (50 * np.sin(10 * ((x[0] + 8)**2 + (x[1] - 8)**2)**(1/2))) /
                                                            (((x[0] + 8)**2 + (x[1] - 8)**2)**(1/2)))]),
    start=np.array([-9.31, 8.78]),                          # gradient, start vector
    learning_rate=0.002,                                    # learning rate (changing for test)
    # max_iterations=5000,                                  # max number of iteration - used while testing
    tolerance=1e-6                                          # tolerance - used while testing
)


x = np.arange(-9.32, -8.95, 0.001)
y = np.arange(8.62, 8.79, 0.001)                            # comfortable size
xx, yy = np.meshgrid(x, y, sparse=True)
z = ((xx+8)**2 + (yy-8)**2) - 5 * np.cos(10 * ((xx+8)**2 + (yy-8)**2)**(1/2))            # our function
h = plt.contourf(x, y, z)                                                                # drawing graph of the function
plt.colorbar()

x_from_way = [x[0] for x in way]
y_from_way = [y[1] for y in way]
# plt.plot(x_from_way, y_from_way)
plt.plot(x_from_way, y_from_way, "o:", linewidth=1.5)       # drawing graph of the way to the result

plt.xlabel('learning rate = 0.002, needed iterations = ?')
plt.title('(x+8)^2 + (y-8)^2) - 5 * cos(10 * ((x+8)^2 + (y-8)^2)^(1/2) function')
plt.show()

# print(result)                                             # useful while checking if algorithm works properly
# print(way)
