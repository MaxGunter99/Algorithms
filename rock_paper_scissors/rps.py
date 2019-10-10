#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  rps = [ 'rock' , 'paper' , 'scissors' ]

  answer = []

  # maybe try recursion?

  if n == 0:
    return [[]]

  elif n == 1:

    for i in range( len( rps ) ):
      solution = [ rps[i] ]
      answer.append( solution )

  elif n == 2:

    for i in range( len( rps ) ):
      for x in range( len( rps ) ):
        answer.append( [rps[i] , rps[x]] )
  elif n == 3:

    for i in range( len( rps ) ):
      for x in range( len( rps ) ):
        for y in range( len( rps ) ):
          answer.append( [rps[i] , rps[x] , rps[y]] )

  elif n == 4:
    for i in range( len( rps ) ):
      for x in range( len( rps ) ):
        for y in range( len( rps ) ):
          for z in range( len( rps ) ):
            answer.append( [rps[i] , rps[x] , rps[y] , rps[z]] )

  elif n == 5:
    for i in range( len( rps ) ):
      for x in range( len( rps ) ):
        for y in range( len( rps ) ):
          for z in range( len( rps ) ):
            for u in range( len( rps ) ):
              answer.append( [rps[i] , rps[x] , rps[y] , rps[z] , rps[u]] )

  return answer
      

  

rock_paper_scissors(1)
# [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')