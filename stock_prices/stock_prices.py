#!/usr/bin/python

import argparse

def find_max_profit(prices):
  print( prices )
  max_profit = 0
  buy = 0
  sell = 0
  sell = sell + min( prices )
  buy = buy + max( prices )
  max_profit = sell - buy
  print( max_profit )
  return max_profit
    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# TEST WITH | python3 test_stock_prices.py |