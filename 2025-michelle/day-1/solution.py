import csv
import os

BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.csv")

def solution():
    lock_range = range(100)
    curr = 50
    num_of_rotations_on_zero = 0

    with open(input_path, newline="\n") as f:
        reader = csv.reader(f)
        for row in reader:
            row_char = row[0]
            direction = row_char[0]
            num_times = int(row_char[1:len(row_char)])

            if num_times > 100: num_times = num_times % 100

            curr = curr + num_times  if direction == "R" else curr - num_times

            if curr not in lock_range:
                curr = 100 + curr if curr < 0 else curr - 100
            
            if curr == 0: num_of_rotations_on_zero += 1

    return num_of_rotations_on_zero

print(solution())   # 1059