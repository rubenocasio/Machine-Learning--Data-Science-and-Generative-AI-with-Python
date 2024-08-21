import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# mean (average)
incomes = np.random.normal(27000, 15000, 10000)
print(np.mean(incomes))

plt.hist(incomes, 50)
# plt.show()

# compute the median
print(np.median(incomes))

incomes = np.append(incomes, [1000000000])
print(np.median(incomes))
print(np.mean(incomes))

## Mode
ages = np.random.randint(18, high=90, size=500)
print(ages)

print(stats.mode(ages))

incomes = np.random.normal(100.0, 50.0, 10000)
plt.hist(incomes, 50)
plt.show()

print(incomes.std())
print(incomes.var())