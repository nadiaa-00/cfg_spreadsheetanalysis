import csv
from statistics import mean, median, multimode, stdev
def read_data():
    data = []
    with open('RAW_global_deaths.csv', 'r') as covid_csv:
     spreadsheet = csv.DictReader(covid_csv)
     for row in spreadsheet:
         data.append(row)
    return data
def run():
    data = read_data()
    covid = []
    for row in data:
        print(row)
#put the print function into the loop so you can see which keys the data set has and fix an error messages
#relating to a key issue --> key error
        coviddeaths = int(row['6/22/20'])
        covid.append(coviddeaths)
    total = sum(covid)
    minimum = min(covid)
    maximum = max(covid)
    average = mean(covid)
    Middepoint = median(covid)
    Modes = multimode(covid)
    SampleSpread = stdev(covid)
    print('Total deaths: {}' .format(total))
    print('Minimum deaths: {}' .format(minimum))
    print('Maximum deaths: {}' .format(maximum))
    print('Arithmetic Mean: {}' .format(average))
    print('Ordinary Statistical Median: {}' .format(Middepoint))
    print('Total Modes: {}' .format(Modes))
    print('Sample Dispersion: {}' .format(SampleSpread))
run()