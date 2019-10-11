#!/usr/bin/python

import sys
import os
os.system( 'clear' )

def making_change(amount, denominations):

  # print( amount , denominations , '\n' )

  if amount == 0:
    print( 'answer' , 1 )
    return 1

  answer = []

  possible_coins = []

  for i in denominations:
    if i == amount:
      possible_coins.append( i )
    elif i < amount:
      possible_coins.append( i )

  # print( possible_coins )

  # while total < amount:
  if [possible_coins[0]] * amount not in answer:
    answer.append( [possible_coins[0]] * amount )

  total = 0

  for i in range( len( answer ) ):
    for x in range( len( answer[i] ) ):
      if len( possible_coins ) > 1:
        if answer[i][x] * possible_coins[1] + possible_coins[1] == amount:
          tot = []
          for y in range( possible_coins[1] ):
            temp = answer[i][x]
            tot.append( temp )
          tot.append( possible_coins[1] )
          if tot not in answer:
            answer.append( tot )
          else:
            tot2 = []
            tot2.append( possible_coins[1] )
            for y in range( possible_coins[1] ):
              temp = answer[i][x]
              tot2.append( temp )
            if tot2 not in answer:
              answer.append( tot2 )

  for i in range( len( possible_coins ) ):
    double = possible_coins[i] + possible_coins[i]
    if double == amount:
      if [ possible_coins[i] , possible_coins[i] ] not in answer:
        answer.append( [possible_coins[i] , possible_coins[i]] )
    elif possible_coins[i] == amount:
      if possible_coins[i] not in answer:
        answer.append( [possible_coins[i]] )
            



  print( answer )
  print( 'answer' , len(answer) )


making_change(0, [1, 5, 10, 25, 50] )
making_change(1, [1, 5, 10, 25, 50] )
making_change(5, [1, 5, 10, 25, 50] )
making_change(10, [1, 5, 10, 25, 50] )
making_change(20, [1, 5, 10, 25, 50] )
making_change(30, [1, 5, 10, 25, 50] )

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")