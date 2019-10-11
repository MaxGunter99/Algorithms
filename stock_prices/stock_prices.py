#!/usr/bin/python

import argparse
import os
os.system( 'clear' )

print( '-----------' )

def find_max_profit(prices):

  # we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, 
  # but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; 
  # it can't come after it in the list of prices. 

  max_ammout_you_can_earn = None

  for i in range( len( prices ) ):

    section = prices[ i: ]

    for x in section:

      compared = x - prices[i]

      if compared == 0:
        None

      elif max_ammout_you_can_earn is None:
        max_ammout_you_can_earn = compared

      else:
        if compared >= max_ammout_you_can_earn:
          max_ammout_you_can_earn = compared



  print( max_ammout_you_can_earn )
  return max_ammout_you_can_earn
    
    
# return prices


# find_max_profit( [10, 7, 5, 8, 11, 9] ) # returns 6
# find_max_profit( [100, 90, 80, 50, 20, 10] ) # returns - 10
# find_max_profit( [1050, 270, 1540, 3800, 2] ) # returns 3530
# find_max_profit( [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79] ) # returns 94


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))