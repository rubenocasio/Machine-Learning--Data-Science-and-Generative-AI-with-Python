import matplotlib.pyplot as plt
import numpy as np

incomes = np.random.normal(100.0, 50.0, 10000)

plt.hist(incomes, 10000)
incomes.std()
incomes.var()

plt.show()