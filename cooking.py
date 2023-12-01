import world
import functions
import person_class
import food

class Cookbook:
  def __init__(self):
    self.recipes = []

  def add_meal_recipe_to_cookbook(self, Meal):
    self.recipes.append(Meal)

class Meal:
  def __init__(self, name, nutrition, taste):
    self.name = name
    self.nutrition = nutrition
    self.taste = taste
    self.recipe = []
    self.cooked = False

  def add_recipe(self, Recipe):
    self.recipe.append(Recipe)

  def cook_food(self):
    self.cooked = True
    self.name = "Cooked " + self.name

class Recipe:
  def __init__(self, name, nutrition):
    self.name = name
    self.nutrition = nutrition
    self.ingrediants = []

  def add_ingrediants(self, list_of_ingrediants):
    for ingrediant in list_of_ingrediants:
      self.ingrediants.append(ingrediant)

def cook():

  current_recipe = []
  
  if world.oven not in world.main_character.current_room.furnitures:
    functions.print_conversationally("Where are you supposed to cook, huh?")
  else:
    use_stove = functions.menu("Want to use the stove?", ["Yes", "No"])
    if use_stove == "Yes":
      if len(world.main_character.foods) == 0:
        functions.print_conversationally("You gots no food to cook, fool!")
      else:
        cook_what = functions.menu("What would you like to cook?", world.main_character.foods)
        if cook_what.nutrition <1:
          functions.print_conversationally("That's not really something you can 'cook', per se.\n\n")
          cook()
        else:
          functions.print_conversationally(f"Sweet! You're cooking up some {cook_what.name}!")
          current_recipe.append(cook_what)
          world.main_character.foods.remove(cook_what)
          just_cooked = False
          if just_cooked == False:
            def add_anything():
              if len(world.main_character.foods) > 0:
                add_stuff = functions.menu("\n\nWant to add anything?", ["Yes", "No"])
                if add_stuff == "Yes":
                  with_what = functions.menu("What would you like to add?", world.main_character.foods)
                  current_recipe.append(with_what)
                  world.main_character.foods.remove(with_what)
                  functions.print_conversationally(f"Nice! You added {with_what.name}")
                # print("\n\n")
                # print(current_recipe)
                  add_anything()
                else:
                  functions.print_conversationally("Okay... should be REALLY tasty then...")
                  for i in world.cookbook.recipes:
                    for j in i.recipe:
                      for k in j.ingrediants:
                        if set(current_recipe).issubset(j.ingrediants):
                          functions.print_conversationally(f"\n\nYou cooked {j.name}!")
                          world.Food.cook_food(j)
                          # world.main_character.add_to_bag(j)
                          world.main_character.foods.append(j)
                          just_cooked = True
                          return just_cooked
                          
              else:   
                for i in world.cookbook.recipes:
                  for j in i.recipe:
                    for k in j.ingrediants:
                      if set(current_recipe).issubset(j.ingrediants):
                        functions.print_conversationally(f"\n\nYou cooked {j.name}!")
                        world.Food.cook_food(j)
                        # world.main_character.add_to_bag(j)
                        world.main_character.foods.append(j)
                        just_cooked = True
                        return just_cooked
                else:
                  functions.print_conversationally("\n\nYou cooked dogshit. Nice try asshole")
                  just_cooked = True
                  return just_cooked
            add_anything()
          else:
              pass   
    else:
      functions.print_conversationally("Then why bother asking? Please don't waste my time.")
