import csv


# Read the data from the spreadsheet

def open_dataset(file_name):
    from csv import reader
    open_file = open(file_name)
    read_file = reader(open_file)
    dataset = list(read_file)
    return dataset


# create list with month and sales data
def data_list(y):
    output_data = []
    for x in y:
        values = x[1:3]
        output_data.append(values)
    return output_data


# Output a summary of the results to a spreadsheet
def create_sheet(new_sheet):
    import csv
    with open('new1_sheet.csv', 'w+') as new_file1:
        csv_writer = csv.writer(new_file1)
        csv_writer.writerows(new_sheet)
    return csv_writer


# Collect all of the sales from each month into a single list
def total_sales(file_name):
    monthly_sale = []
    for rows in file_name:
        name = int(rows[2])

        monthly_sale.append(name)
    return monthly_sale


# Open file and separate header
sales = open_dataset('sales.csv')
sales_with_header = sales
sales = sales[1:]
print(sales)
print('\n')

# month and sales list
months_and_sales = data_list(sales_with_header)
print('Months and sales data: {}'.format(months_and_sales))
# new sheet
sheet = create_sheet(months_and_sales)

# Collect all of the sales from each month into a single list
all_sales = total_sales(sales)

print('\n')
# sales from each month into a single list
print('Sales from each month : {}'.format(all_sales))

# Output total sales across all months
total = sum(all_sales)
total_sales = 'Total sales = {}'.format(total)
print(total_sales)

# Calculate the following:

# the average
avg_sales = sum(all_sales) / len(all_sales)
print('Average sale = {}'.format(avg_sales))
# months with the highest
highest_sales = max(all_sales)
print('Highest_sale = {}'.format(highest_sales))
# and lowest sales
lowest_sales = min(all_sales)
print('Lowest_sale = {}'.format(lowest_sales))
