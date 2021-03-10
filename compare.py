import time
import random
import numpy as np
from sortlib import *

# values in hundeds
NUM_INTS = [100, 1000, 10000, 20000]
MAX_VALUE = 999999

SORTS = {
  'Default': sorted,
  'Bubble': bubble_sort,
  'Heap': heap_sort,
  'Insertion': insertion_sort,
  'Pigeon': pigeonhole_sort,
  'Shell': shell_sort,
}

def run_sort(arr, sort_func):
  t = time.process_time()
  sort_func(arr)
  return 1000 * (time.process_time() - t)

for count in NUM_INTS:
  random_ints = [random.randint(0, MAX_VALUE)] * count * 100
  print("Count:", count)
  for label, sort in SORTS.items():
    print("  Sort:", label, "-", run_sort(random_ints[:], sort))
