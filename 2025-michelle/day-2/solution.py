import csv
import os

BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.csv")

def is_invalid(num):
    str_num = str(num)
    str_num_length = len(str_num)

    if str_num_length == 1: return False
    if str_num_length == 2: return str_num[0] == str_num[1]

    str_num_length_half = str_num_length // 2
    
    first_half = str_num[:str_num_length_half]
    second_half = str_num[str_num_length_half:]

    return first_half == second_half

def solution():
    invalid_ids = []
    with open(input_path) as f:
        line = f.read().strip()
        ranges = line.split(",")
        for r in ranges:
            start, end = r.split("-")
            start_int, end_int = int(start), int(end)
            for i in range(start_int, end_int + 1):
                if is_invalid(i): invalid_ids.append(i)

    return sum(invalid_ids)
        
print(solution())

