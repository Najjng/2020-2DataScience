import numpy as np
import csv

birth_data = open("births.csv")
csv_reader = csv.DictReader(birth_data)
line_count = 0

for row in csv_reader:
    if line_count == 0: 
        line_count += 1
    elif line_count == 1:
        birth_arr = np.array(row)
        line_count +=1
    else:
        birth_arr = np.append(birth_arr, row)
        line_count += 1
        


