import csv
import pandas as pd

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Intentional conflict to demonstrate GitHub collaboration. This line will be changed in the other branch.

# run python demo_script_1.py in the terminal to execute the 
# script and see the output of the CSV file.