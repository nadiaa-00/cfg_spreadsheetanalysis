import csv
from statistics import mean, median, multimode, stdev
def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
     spreadsheet = csv.DictReader(sales_csv)
     for row in spreadsheet:
         data.append(row)
    return data
def run():
    data = read_data()
    sales = []
    for row in data:
        print(row)
#put the print function into the loop so you can see which keys the data set has and fix an error messages
#relating to a key issue --> key error
        sale = int(row['Sales'])
        sales.append(sale)
    total = sum(sales)
    minimum = min(sales)
    maximum = max(sales)
    average = mean(sales)
    Middepoint = median(sales)
    Modes = multimode(sales)
    SampleSpread = stdev(sales)
    print('Total sales: {}' .format(total))
    print('Minimum sales: {}' .format(minimum))
    print('Maximum sales: {}' .format(maximum))
    print('Arithmetic Mean: {}' .format(average))
    print('Ordinary Statistical Median: {}' .format(Middepoint))
    print('Total Modes: {}' .format(Modes))
    print('Sample Dispersion: {}' .format(SampleSpread))
run()
