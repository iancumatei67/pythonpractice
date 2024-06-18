from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    with open(filename) as opened_file:
       min_val = None
       max_val = None

       for line in opened_file:
           num = int(line.strip())

           if min_val is None or num < min_val:
               min_val = num
           if max_val is None or num > max_val:
               max_val = num

    return min_val, max_val

print(get_min_max('filename'))