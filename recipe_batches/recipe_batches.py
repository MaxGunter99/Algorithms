#!/usr/bin/python
import os
import math
os.system( 'clear' )

def recipe_batches(recipe, ingredients):
  recipename = list( recipe.keys() )
  recipequantity = list( recipe.values() )
  ingredientname = list( ingredients.keys() )
  ingredientquantity = list( ingredients.values() )

  recipeList = []
  ingredientList = []
  
  for i in range( len( recipename ) ):
    recipeList.append( [ recipename[ i ] , recipequantity[ i ] ] )

  for i in range( len( ingredientname ) ):
    ingredientList.append( [ ingredientname[ i ] , ingredientquantity[ i ] ] )

  if len( ingredientList ) < len( recipeList ):
    print( 'You are missing an Ingredient!' )
    return 0

  quantity = []

  for i in range( len( recipeList ) ):
    # print( f'Recipe: {recipeList[i]} , Ingredients: {ingredientList[i]}' )
    if recipeList[ i ][0] == ingredientList[i][0]:
      if ingredientList[i][1] // recipeList[ i ][1] == 0:
        return 0
      else:
        quantity.append( ingredientList[i][1] // recipeList[ i ][1] )
      
    else:
      print( 'Not the same ingredients!' )

  most_you_can_make = quantity[ len( quantity ) - 1 ]

  for i in range( len( quantity ) ):
    if quantity[i] < most_you_can_make:
      batches = quantity[i]
      most_you_can_make = batches

  print( most_you_can_make )
  return most_you_can_make


# recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }) # returns 0
# recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }) # returns 1
# recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }) # returns 2
# recipe_batches({ 'milk': 2 }, { 'milk': 200}) # returns 100


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))