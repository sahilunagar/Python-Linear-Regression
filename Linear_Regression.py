# numpy and matplotlib modules should be installed
# necessary imports

import numpy as np                #for numpy arrays
from statistics import mean       #to get mean values of arrays
import matplotlib.pyplot as plt   #for plotting
import random                     #for generating a random data

#function to create a random dataset of 'n' data

def dataset(n, varience, step = 1, correlation = False):
    xs = [i for i in range(n)]
    val = 1
    ys = []
    for i in range(n):
        y = val + random.randrange(-varience, varience)
        ys.append(y)
        if correlation and correlation=='positive':
            val += step
        elif correlation and correlation=='negative':
            val -= step
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)
  
xs, ys = dataset(100, 50, step=2, correlation='positive')

# plotting the generated data

plt.scatter(xs, ys, color='g')
plt.show()

# Function to calculate best fit slope and intercept of the given data

def best_fit_slope_intercept(x, y):
    m = ((mean(x)*mean(y)) - mean(x*y)) / ((mean(x)**2) - mean(x*x))
    b = mean(y) - (m * mean(x))
    return m,b
  
m, b = best_fit_slope_intercept(xs, ys)
print('best fit slope = ',m,'\nintercept = ',b)

regression_line = [m*i+b for i in xs]

#plotting regression line along with data

plt.scatter(xs, ys, color='g', label='data')
plt.plot(xs, regression_line, color='b', label='regression line')
plt.legend()
plt.show()
