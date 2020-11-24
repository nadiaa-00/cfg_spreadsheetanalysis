import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("sales.csv")

df['Sales Difference'] = df.Sales.diff()
df['Percentage Difference'] = (df['Sales Difference'] / df['Sales'].shift())*100

print(df[['Month', 'Percentage Difference']])

df.plot(kind='scatter', x='Month',y='Percentage Difference',color='red')
df.plot(kind='bar',x='Month',y='Percentage Difference')
plt.title("2018")  # give a suitable title for the plot
plt.legend()  # displays legend on which line relates to which country
plt.tight_layout()  # auto adjust of plot for better viewing
plt.show()
