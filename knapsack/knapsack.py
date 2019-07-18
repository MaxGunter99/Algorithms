#!/usr/bin/python

import sys
from collections import namedtuple

# LAYOUT FROM MATRIX
Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  # print( items )
  # print( len( items) )

  # INDEX [0]
  i = 0

  # SIZE [1]
  s = 0

  # VALUE [2]
  v = 0

  while i < len( items ):
    for x in items:
      three_items = 0
      if three_items <= 3:
        print( x[0] , x[1] , x[2] )
        v = v + x[2]
        s = s + x[1]
        three_items += 1
        print( "Total Size:", s , "\n" , "Total Value:" , v )
        if three_items == 3:
          three_items = 0
        return s , v

      # return its
  return s , v
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')

# TEST WITH | python3 test_knapsack.py |
# TEST INDIVISUALLY | python3 test_knapsack.py -k small |