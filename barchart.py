import matplotlib.pyplot as plt  # to implement plots
import csv  # to read and process CSV files
import numpy as np

Months = []  # x-axis 1 data
Sales = []  # y-axis 1 data
Expenditure = []  # y-axis 2 data

# open CSV file
with open('sales.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    next(csvReader)# file handler

    for row in csvReader:  # loop through file handler
        Months.append(row[1])
        Sales.append(row[2])
        Expenditure.append(row[3])

Sales_int = list(map(int, Sales))  # convert string list of cases to integers for plotting
Expenditure_int = list(map(int, Expenditure))
x = np.arange(len(Months))  # the label locations

fig, ax = plt.subplots()  # this wrapper is useful to create custom layouts
width = 0.35  # the width of the bars
bar1 = ax.bar(x - width / 2, Sales_int, width, label='Sales', color='#625FE9')
bar2 = ax.bar(x + width / 2, Expenditure_int, width, label='Expenditure', color='#E45240')

ax.set_ylabel('£')  # axis setting of Y label
ax.set_xlabel('2018')  # axis setting of X label
ax.set_xticks(x)  # axis setting of X ticks
ax.set_xticklabels(Months)  # axis setting of X tick labels
ax.legend()  # used to include information on titles of bars.

ax.set_title("2018 Sales and Expenditure")  # give a suitable title for the plot
plt.show()

