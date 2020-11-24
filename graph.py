import matplotlib.pyplot as plt  # to implement plots
import csv  # to read and process CSV files

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

Sales_ = list(map(int, Sales))  # convert string list of cases to integers for plotting
Expenditure_ = list(map(int, Expenditure))
plt.plot(Months, Sales_, color="#444444", linestyle="--", label="Sales",
         marker="X")  # plot the data with X as the marker for each point
plt.plot(Months, Expenditure_, color="#5a7d9a", label="Expenditure",
         marker="+")  # plot the data with + as the marker for each point

plt.title("2018")  # give a suitable title for the plot
plt.legend()  # displays legend on which line relates to which country
plt.tight_layout()  # auto adjust of plot for better viewing
plt.show()  # show the plot