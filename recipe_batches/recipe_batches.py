#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  print( "Recipe" , recipe , "Ingredients" , ingredients )

  recipe_requirements = []
  given_ingreds = []

  for i in recipe.values():
    # print("ING" , ing)
    recipe_requirements.append( i )

  for i in ingredients.values():
    given_ingreds.append(i)


  if len( given_ingreds ) < len( recipe_requirements ):
    new_given_ingreds = given_ingreds
    new_given_ingreds.append( 0 )
    given_ingreds = new_given_ingreds
    pass_test = [ x//y for x,y in zip( given_ingreds ,recipe_requirements ) ]
    answer = pass_test.sort()
    answer = pass_test[:1]
    for i in answer:
      return i
  elif len( recipe_requirements ) < len( given_ingreds ):
    recipe_requirements.append( 0 )
  
  else:
    new_given_ingreds = given_ingreds
    new_given_ingreds.append( 0 )
    given_ingreds = new_given_ingreds
    pass_test = [ x//y for x,y in zip( given_ingreds ,recipe_requirements ) ]
    answer = pass_test.sort()
    answer = pass_test[:1]
    for i in answer:
      return i

  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# TEST WITH | python3 test_recipe_batches.py |