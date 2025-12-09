import csv
import os
from collections import deque

BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.csv")

def solution():
    jolts = []
    with open(input_path, newline="\n") as f:
        reader = csv.reader(f)
        for row in reader:
            
            num = row[0]
            deque_of_nums = deque()

            for index, i in enumerate(num):
                int_i = int(i)
                if len(deque_of_nums) == 2: 
                    if deque_of_nums[1] < int_i:
                        deque_of_nums.pop()
                        deque_of_nums.append(int_i)

                if not(len(deque_of_nums)):
                    deque_of_nums.append(int_i)

                elif deque_of_nums[0] < int_i:
                    if index < len(num) - 1:
                        while len(deque_of_nums):
                            deque_of_nums.popleft()
                    deque_of_nums.append(int_i)

                elif len(deque_of_nums) == 1:
                    deque_of_nums.append(int_i)

                elif deque_of_nums[1] < int_i:
                    deque_of_nums.pop()
                    deque_of_nums.append(int_i)


            char_digit = int(str(deque_of_nums[0]) + str(deque_of_nums[1]))

            jolts.append(char_digit)
            
        return sum(jolts)

print(solution()) # 17435


# import csv
# import os
# from collections import deque

# BASE_DIR = os.path.dirname(__file__)
# input_path = os.path.join(BASE_DIR, "input.csv")

# def solution():
#     jolts = []
#     with open(input_path, newline="\n") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             first_digit, second_digit = 0, 0
#             set_second_digit = False
#             num = row[0]
#             deque_of_nums = deque()
            
#             for index, i in enumerate(num):
#                 int_i = int(i)

#                 if set_second_digit:
#                     second_digit = int_i
#                     set_second_digit = False
#                     continue

#                 if int_i > first_digit and index < len(num) - 1:
#                     first_digit = int_i
#                     set_second_digit = True
#                     continue

#                 if second_digit < int_i:
#                     second_digit = int_i
            
#             char_digit = int(str(first_digit) + str(second_digit))

#             jolts.append(char_digit)
            
#         return sum(jolts)

# print(solution())