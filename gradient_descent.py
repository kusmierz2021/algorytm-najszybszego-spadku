import numpy as np


def gradient_descent(gradient, start, learning_rate, max_iterations=1000000, tolerance=1e-06):
    number_of_iterations = 0                                # used as additional stop condition
    way = []                                                # to check vector changes
    vector = start
    while True:
        number_of_iterations += 1
        if isinstance(vector, (int, float)):                # if / else in lines 10 - 12 is caused by my helplessness
            way.append(vector)                              # while testing - it is not obvious element of algorithm
        else:
            way.append((vector[0], vector[1]))
        diff = - learning_rate * gradient(vector)           # calculating difference using learning rate and gradient
        if np.all(np.abs(diff) <= tolerance) or number_of_iterations >= max_iterations:
            break                                           # stop conditions - max_iterations was just useful during
        vector += diff                                      # testing implementation
    print("iterations: ", number_of_iterations)             # let know how many iterations needed to reach result
    return vector, way                                      # return result vector and way needed to reach that
