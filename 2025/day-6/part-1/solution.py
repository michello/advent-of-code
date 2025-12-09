import csv
import os
import math

BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.csv")

class Solution:
    def __init__(self):
        self.values = []
    
    def process_file(self):
        values = []
        final_values = []
        with open(input_path, newline="\n") as f:
            reader = csv.reader(f)
            for row in reader:
                row_arr = row[0].split()
                if not values:
                    for cell in row_arr:
                        values.append([int(cell)])
                elif row_arr[0] not in ('*', '+'):
                        for i in range(len(row_arr)):
                            values[i].append(int(row_arr[i]))
                else:
                    for i, op in enumerate(row_arr):
                        if op == '*': final_values.append(math.prod(values[i]))
                        else: final_values.append(sum(values[i]))
        return sum(final_values)
    
    def run(self):
        print(self.process_file())

solution = Solution()
solution.run()