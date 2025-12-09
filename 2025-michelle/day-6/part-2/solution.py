import csv
import os
import math
from typing import List


""""

[[[1, 2, 3], [3, 2, 8], [None, 5, 1], [6, 4, None]], 
 [[None, 4, 5], [6, 4, None], [3, 8, 7], [2, 3, None]], 
 [[None, None, 6], [9, 8, None], [2, 1, 5], [3, 1, 4]]]

"""

BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.txt")

"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

1 * 24 * 356
356 * 24 * 1 = 8544


"""

class Index:
    def __init__(self, start, end = None):
        self.start = start
        self.end = end

class OperationBoundary:
    def __init__(self, operation: str, index: Index):
        self.operation = operation
        self.index = index
        self.numbers : List[int] = []
    
    def set_index_end(self, end):
        self.index.end = end

class Solution:
    def __init__(self):
        self.input_size = 3

        # raw data
        self.data = self.get_file_lines()
        self.number_data = self.data[:len(self.data) - 1]
        self.operations_data = self.data[len(self.data) - 1]

        # repurposed data
        self.column_to_operations = self.get_column_to_operations_data()
    
    def get_file_lines(self):
        with open(input_path, "r") as f:
            return [line.rstrip("\n") for line in f]
    
    def get_column_to_operations_data(self):
        column_to_operations = {}


        operations_data_array_index = 0


        for i, op in enumerate(self.operations_data):
            if op == " ": continue

            column_to_operations[operations_data_array_index] = OperationBoundary(op, Index(i))
            

            if operations_data_array_index > 0:
                column_to_operations[operations_data_array_index-1].set_index_end(i)

            operations_data_array_index += 1
        
        column_to_operations[operations_data_array_index-1].set_index_end(len(self.operations_data) + 1)

        return column_to_operations
    
    def process_number(self, number_arr):
        return int(''.join([num for num in number_arr if num != '']))

    
    def populate_column_to_operations_data(self):
        for op in self.column_to_operations.keys():
            
            op_boundary = self.column_to_operations[op]

            start_index = op_boundary.index.start
            end_index = op_boundary.index.end

            for index in range(start_index, end_index-1): # each index == number
                number = []
                for row in range(len(self.number_data)): # each digit of a number

                    number.append(self.number_data[row][index])
                
                self.column_to_operations[op].numbers.append(self.process_number(number))

            
                
    def perform_operations(self):
        answers = []
        for op in self.column_to_operations.keys():
            numbers = self.column_to_operations[op].numbers
            operation = self.column_to_operations[op].operation
            if operation == "+": answers.append(sum(numbers))
            if operation == "*": answers.append(math.prod(numbers))
        return sum(answers)



    def run(self):
        self.populate_column_to_operations_data()
        return self.perform_operations()



s = Solution()
print(s.run())