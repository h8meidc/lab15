import pandas as pd

import matplotlib.pyplot as plt

plt.style.use('ggplot') 

plt.rcParams['figure.figsize'] = (15, 5) 

fixed_df = pd.read_csv('comptagevelo2014.csv', 

                       sep=',', encoding='latin1',

                       parse_dates=['Date'], dayfirst=True,

                       index_col='Date')

fixed_df[:3]

fixed_df.plot(figsize=(15, 10))
monthly_counts = fixed_df.resample('M').sum()

# Знаходження місяця з найбільшою кількістю велосипедистів
popular = monthly_counts.idxmax().iloc[0].strftime('%B')

print("Найпопулярніший місяць:", popular)
plt.show()