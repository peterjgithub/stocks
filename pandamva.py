import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

product = {'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
'demand': [290, 260, 288, 300, 310, 303, 329, 340, 316, 330, 308, 310]
}

df = pd.DataFrame(product)

df['SMA_2'] = df.iloc[:,1].rolling(window=2).mean()
df['SMA_4'] = df.iloc[:,1].rolling(window=4).mean()
df['SMA_6'] = df.iloc[:,1].rolling(window=6).mean()

plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['demand'],label='data')
plt.plot(df['SMA_2'],label='SMA 2 Months')
plt.plot(df['SMA_4'],label='SMA 4 Months')
plt.legend(loc=2)
<matplotlib.legend.Legend at 0x11fe15080>

# print(df.head())
print(df)

 