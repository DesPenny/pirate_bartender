import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

called = ["slippery ballsack", "wet minge", "riding cowgirl", "Irish car bomb", "baby kilkenny"]

def bartender_asks():
  preferences = {}
  for k, v in questions.iteritems():
    print v
    preferences[k] = raw_input() in ["y", "yes"]
  return preferences
  
      
def create_drink(preferences):
  drink = []
  for k, v in preferences.iteritems():
    if not v:
      continue
    drink.append(random.choice(ingredients[k]))
  return drink

def named_drink():
  called2 = (random.choice(called))
  return called2

def main():
  preferences = bartender_asks()
  drink = create_drink(preferences)
  drink_name = named_drink()
  print "Here try this. It's made of:"
  for ingredient in drink:
    print "A {}".format(ingredient)
  print "I call it the {}".format(drink_name)
    
if __name__ == '__main__':
  main()
  