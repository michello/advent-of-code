import os
from functools import lru_cache

BASE_DIR = os.path.dirname(__file__)
# input_path = os.path.join(BASE_DIR, "sample-input.txt")
input_path = os.path.join(BASE_DIR, "input.txt")

class Solution:

    def __init__(self):
        self.tree = self.process_input()
        self.beams = [self.get_start()]
    
    def process_input(self):
        with open(input_path, "r") as f:
            return [list(line.rstrip("\n")) for line in f]
    
    def get_start(self):
        first_row = self.tree[0]
        return first_row.index('S')

    def run_part1(self):
        num_split = 0
        for i in range(1, len(self.tree)):
            curr_tree_level = self.tree[i]
            
            new_beams = set()

            for beam_index in self.beams:
                if curr_tree_level[beam_index] == "^": # gotta split
                    num_split += 1
                    if beam_index-1 in range(len(curr_tree_level)): new_beams.add(beam_index-1)
                    if beam_index+1 in range(len(curr_tree_level)): new_beams.add(beam_index+1)
                else:
                    new_beams.add(beam_index)
                curr_tree_level[beam_index] = "|"
            
            self.beams = list(new_beams)
        return num_split
    
    def run_part2(self):
        @lru_cache(maxsize=None)
        def count_timelines(row, col):
            # If we’ve left the manifold, that's one completed timeline
            if row >= len(self.tree) or col < 0 or col >= len(self.tree[row]):
                return 1

            cell = self.tree[row][col]

            if cell == "^":
                # Split: particle’s timeline forks into left and right
                left = count_timelines(row + 1, col - 1)
                right = count_timelines(row + 1, col + 1)
                return left + right
            else:
                # Empty / start / anything-not-^ : just fall straight down
                return count_timelines(row + 1, col)

        # Beam starts in the row *below* S, same as in part 1
        start_row = 1
        return count_timelines(start_row, self.get_start())


s = Solution()
# print("Part 1:", s.run_part1())  # 1560
print("Part 2:", s.run_part2())