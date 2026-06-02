import csv
import pandas as pd

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


df = pd.read_csv('data.csv')
print(df)

# run python demo_script_1.py in the terminal to execute the 
# script and see the output of the CSV file.