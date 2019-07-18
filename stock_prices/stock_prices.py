#!/usr/bin/python

import argparse

def find_max_profit(prices):

  print(  "Prices" , prices )

  max_profit = None

  for i in range( len( prices ) - 1 ):

    for x in range( i + 1 , len(prices ) ):
      # print( x )
      difference = prices[x] - prices[i]

      if not max_profit:
        max_profit = difference

      elif max_profit < difference:
        max_profit = difference

  return max_profit

  # max_profit = 0
  # buy = 0
  # sell = 0
  # biggest_sell = sell + max( prices )
  # print( biggest_sell )
  # smallest_buy = buy + min( prices )
  # print( smallest_buy )
  # profit =  biggest_sell - smallest_buy
  # max_profit.append(profit)

  # return profit
    



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

# TEST WITH | python3 test_stock_prices.py |