import os

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

    def run(self):
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

s = Solution()
print(s.run()) # 1560