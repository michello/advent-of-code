import csv
import os

BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.csv")

def process_file():
    intervals, digits = [], []
    with open(input_path, newline="\n") as f:
        reader = csv.reader(f)
        for row in reader:
            if not len(row): continue
            elem = row[0]

            if '-' in elem:
                elems = elem.split('-')
                lower, upper = int(elems[0]), int(elems[1])
                intervals.append((lower, upper))
            else:
                digits.append(int(elem))
        

    return sorted(intervals), digits

def flatten_intervals(intervals):
    list_of_flattened_interval = [intervals[0]]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if list_of_flattened_interval[-1][1] >= interval[0]:
            prev_interval = list_of_flattened_interval.pop()
            list_of_flattened_interval.append((
                min(interval[0], prev_interval[0]),
                max(interval[1], prev_interval[1])
            ))
        else:
            list_of_flattened_interval.append(interval)
    return list_of_flattened_interval

def is_fresh_ingredient(digit, flattened_intervals):
    lo, hi = 0, len(flattened_intervals) - 1

    while (lo <= hi):
        mid = lo + (hi - lo) // 2

        interval = flattened_intervals[mid]

        if digit >= interval[0] and digit <= interval[1]:
            return True
        elif digit > interval[0]:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

def solution():
    intervals, input_digits = process_file()    
    flattened_intervals = flatten_intervals(intervals)

    fresh_ingredients = []
    for digit in input_digits:
        if is_fresh_ingredient(digit, flattened_intervals):
            fresh_ingredients.append(digit)
    return len(fresh_ingredients)

print(solution())