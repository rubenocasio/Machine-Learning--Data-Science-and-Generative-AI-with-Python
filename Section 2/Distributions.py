import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

## Uniform Distribution
values = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(values, 50)
plt.show()

## Normal / Gaussian
x = np.arange(-3, 3, 0.001)
plt.plot(x, norm.pdf(x))
plt.show()

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

## Exponential PDF / "Power Law"
x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))
plt.show()

## Binomial Probability Mass Function
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))
plt.show()

## Poisson Probability Mass Function
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()