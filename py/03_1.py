from types import FunctionType
from typing import List

def least(ones, num_lines) -> str:
    return str(int(not ones >= num_lines / 2))
def most(ones, num_lines) -> str:
    return str(int(ones >= num_lines / 2))

def alg(lines: List[str], cmp_func: FunctionType) -> str:
    count = 0
    bit_criteria = ""
    next = []
    while (len(lines) != 1):
        for line in lines:
            count += int(line[len(bit_criteria)])

        bit_criteria += cmp_func(count, len(lines))
        for line in lines:
            if not line.startswith(bit_criteria):
                continue
            next.append(line)
        lines = next
        next = []
        count = 0
    return lines[0].strip()

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines_copy = [line for line in lines]
    
    oxygen_generator_rating = alg(lines_copy, most)
    oxygen_scrubber_rating = alg(lines, least)

    life_supporting_rate = int(oxygen_generator_rating, 2) * int(oxygen_scrubber_rating, 2)
    print(life_supporting_rate)