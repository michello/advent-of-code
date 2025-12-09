import csv
import os
import math


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

[1,2,3], [3,2,8], [0,5,1], [0,6,4]
[0,4,5], [0,6,4], [3,8,7]
[0,0,6]
"""
class Group:
    def __init__(self, num_of_digits):
        self.digits = [[None, None, None] * num_of_digits]
        self.operation = ""

class Operand:
    def __init__(self, operand, start_index, end_index):
        self.operand = operand
        self.start_index = start_index
        self.end_index = end_index

class Solution:
    def __init__(self):
        self.values = []

    def get_file_lines(self):
        with open(input_path, "r") as f:
            return [line.rstrip("\n") for line in f]

    def clean_row(self, row):
        str_integer = ''
        for c in row:
            if c != None: str_integer += str(c)
        print(f"this is str_int {str_integer}")

        return int(str_integer) if str_integer != '' else 0
    
    def run(self):
        lines = self.get_file_lines()
        operation_string = lines[-1]
        operations = []

        for i in range(len(operation_string)):
            potential_operand = operation_string[i]
            if potential_operand in ('*', '+'):
                operations.append(Operand(potential_operand, i, None))

                if len(operations) >= 1:
                    operations[-1].end_index = i + 2
        
        operations[-1].end_index = len(operation_string) - 1
        # print(operations)

        rows = []
        for i in range(len(lines) - 1):
            line = lines[i]
            row = []
            for operation in operations:
                array_for_operation = []
                for i in range(operation.start_index, operation.end_index + 1):
                    num = None if line[i] == " " else int(line[i])
                    array_for_operation.append(num)
                
                row.append(array_for_operation)
            
            rows.append(row)
        
        # print(rows)


        answers = []
        for i, operation in enumerate(operations):
            print(f"{i}, {operation.operand}")
            characters = [[] for _ in range(len(rows))]
            for row in rows:
                for j, c in enumerate(row[i]):
                    # print(f"this is {c}")
                    characters[j].append(c)
            clean_characters = [self.clean_row(character) for character in characters]
            print(clean_characters)

            answer = 1 if operation.operand == "*" else 0
            print("Hello here")
            # print(operation)
            if operation.operand == "*":
                # print(clean_characters)
                for character in clean_characters:
                    print(answer)
                    answer *= character
            else:
                for character in clean_characters:
                    answer += character

            answers.append(answer)
        print(answers)
        print(sum(answers))
            
            # print(characters)



        # final_nums = []
        # for i in range(len(rows[0])):
        #     curr_num = []
        #     for j in range(len(rows[i])):
        #         print(rows[i][j])
        #         curr_num.append(rows[i][j])
        #     print(curr_num)
        #     final_nums.append(self.clean_row(curr_num))

        # for i, row in enumerate(rows):
        #     for j, r in enumerate(row):
        #         row[j] = self.clean_row(r)
        
        # answers = []

        # print(rows)

        # for i, operation in enumerate(operations):
        #     curr_answer = 1 if operation == "*" else 0
        #     print(i)
        #     for row in rows:
        #         print(row[i])
        #         curr_answer = curr_answer * row[i] if operation == "*" else curr_answer + row[i]
        #     print(f"the final answer: {curr_answer}")
        #     answers.append(curr_answer)
        # print(answers)
        # return sum(answers)
        
        # print(rows)

        # for i in range(len(operations)):
        #     curr_opperation = operations[i]
        #     print(f"{curr_opperation.start_index} {curr_opperation.end_index}")
        # print(operations)

        # # for i in range(len(lines) - 1):
        # for i in range(1):
        #     curr_line = lines[i]
        #     # print(curr_line.split(" "))
        #     for c in curr_line: print(c)
            
            # for char in enumerate(curr_line):
        



s = Solution()
print(s.run())

"""
[1, 2, 3]
[3, 2, 8]
[None, 5, 1]
[6, 4, None]

"""