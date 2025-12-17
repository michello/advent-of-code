import os

# BASE_DIR = os.path.dirname(__file__)
# input_path = os.path.join(BASE_DIR, "sample-input.txt")
# input_path = os.path.join(BASE_DIR, "input.txt")

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calculate_rectangle(self, coordinate):
        return abs(coordinate.x - self.x) * abs(coordinate.y - self.y)

class Solution:
    def __init__(self):
        self.coordinates = None
        self.base_dir = os.path.dirname(__file__)
    
    def process_input(self, input_file):
        coordinates = []
        input_path = os.path.join(self.base_dir, input_file)
        with open(input_path, "r") as f:
            for line in f:
                coordinate_arr = line.rstrip("\n").split(",")
                coordinates.append(Coordinate(int(coordinate_arr[0]), int(coordinate_arr[1])))
        return coordinates


    def run_part1(self, input_file = "sample-input.txt"):
        self.coordinates = self.process_input(input_file)

        largest_area = float('-inf')
        visited_coordinates = [self.coordinates[0]]

        for i in range(1, len(self.coordinates)):
            curr_coordinate = self.coordinates[i]

            for previous_coordinate in visited_coordinates:
                curr_area = curr_coordinate.calculate_rectangle(previous_coordinate)
                largest_area = max(curr_area, largest_area)
            
            visited_coordinates.append(curr_coordinate)
        
        return largest_area

solution = Solution()
assert(solution.run_part1() == 50)