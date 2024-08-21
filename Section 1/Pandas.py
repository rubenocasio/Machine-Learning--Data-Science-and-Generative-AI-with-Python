import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("PastHires.csv")
# head() is a handy way to visualize what you've loaded.
# You can pass it an integer to see some specific number of rows at the beginning of your DataFrame:
print(df.head())
print(df.head(10))
print(df.tail(4))
print(df.shape)
print(df.size)
print(len(df))
print(df.columns)
print(df['Hired'])
print(df['Hired'][:5])
print(df[['Years Experience', 'Hired']])
print(df[['Years Experience', 'Hired']][:5])
print(df.sort_values(['Years Experience']))

degree_counts = df['Level of Education'].value_counts()
print(degree_counts)

print(degree_counts.plot(kind='bar'))
plt.show()