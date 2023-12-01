from __future__ import annotations
from termcolor import colored
from collections import defaultdict

import functions
import food
import objects
import actions
import bonepart_program
import person_class
import hostess_program
import waitress_program
import manager_program
import cooking

class WorldBuilder:
    def __init__(self):
        self.world = World()

class World:
    def __init__(self):
        # Maps from the name of a room to the Room object.
        self.rooms = defaultdict(Room)

    def add_room_oneway(self, start, end):
        self.rooms[start].add_neighbor(end)

    def add_room_twoway(self, a, b):
        self.rooms[a].add_neighbor(b)
        self.room_map[a].append(b)
        self.room_map[b].append(a)


class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Room:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.items = []
        self.foods = []
        self.persons = []
        self.furnitures = []

    def add_neighbor(self, direction: str, room: Room):
        if direction in self.neighbors:
            raise Exception(f"Sorry, {direction} is already in neighbors")
        self.neighbors[direction] = room

    def get_neighbor_in_direction(self, direction: str) -> Room:
        if direction not in self.neighbors:
            raise Exception(f"Sorry, {direction} is not in neighbors")
        return self.neighbors[direction]

    def print_neighbors(self):
        for direction, room in self.neighbors.items():
            print(f"\n{direction} leads to {room.name}")
        return ''

    def add_item(self, item):
        self.items.append(item)

    def add_food(self, food):
      self.foods.append(food)

    def remove_item(self, item):
        if item == item in self.items:
            # print(f"removing {item}")
            self.items.remove(item)
        else:
          pass

    def remove_food(self, food):
        if food == food in self.foods:
            # print(f"removing {item}")
            self.foods.remove(food)
        else:
          pass

    def print_items(self):
        functions.print_conversationally(colored("Items:\n", "green"))
        for item in self.items:
            functions.print_conversationally(f"{item.name}\n")
        for food in self.foods:
            functions.print_conversationally(f"{food.name}\n")
        if len(self.items) and len(self.foods) == 0:
          functions.print_conversationally("None.")
        else:
          pass

    def print_persons(self):
        functions.print_conversationally(colored("People:\n", "green"))
        for person in self.persons:
          functions.print_conversationally(f"{person}\n")
        if len(self.persons) == 0:
          functions.print_conversationally("There are no other people.")
        else:
          pass

    def print_description(self):
        self.print_neighbors()
        self.print_items()
        self.print_persons()

    def add_person(self, person):
        self.persons.append(person)

    def add_furniture(self, furniture):
      self.furnitures.append(furniture)

    def print_items_on_furniture(self, furniture):
        functions.print_conversationally(colored(f"Items on the {furniture.name}:\n", "green"))
        for item in furniture.items:
            print(item.name)
        if len(furniture.items) == 0:
          functions.print_conversationally(f"\nThere's nothing on the {furniture.name}.")
        else:
          pass

    def print_furniture(self):
        functions.print_conversationally(colored("Furniture:\n", "green"))
        for furniture in self.furnitures:
          functions.print_conversationally(f"{furniture.name}\n")
        if len(self.furnitures) == 0:
          functions.print_conversationally("There is no furniture.")
        else:
          pass

class Quest:
  def __init__(self, name, duties):
    self.name = name
    self.duties = duties

class Food:
    def __init__(self, name, nutrition, taste):
        self.name = name
        self.nutrition = nutrition
        self.taste = taste
        self.cooked = False

    def get_eaten(self, person):
        # Do something to the person
        person.health = person.health + self.nutrition
        functions.print_conversationally(colored("Health: ", "green"))
        functions.print_conversationally(f"{person.health}\n")

    def cook_food(self):
      self.cooked = True


class Furniture:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item_to_furniture(self, item):
      self.items.append(item)

    def remove_from_furn(self, item):
        if item == item in self.items:
          self.items.remove(item)
        else:
          pass

class Game:
    def __init__(self):
        self.world = World()

    def print_introductory_message(self):
        functions.print_conversationally(
        "Hey loser. Welcome to the game. Now, you might be wondering how to play and that is perfectly natural albeit pretty fucking dumb. Just use your intuition, okay wittle baby? Or type HELP for help... idiot..."
          ""
        )

    def start(self):

        self.print_introductory_message()
        while (True):
            # Read in user input
            user_input = functions.get_user_input().upper()
            # Update the world / do something with the input

            if user_input == "HELP":
                functions.print_conversationally(
                    "It's not hard, just type what you want to do. Want to see the room? Ask to look around. Want to examine an object? Ask to EXAMINE it. Want to leave? THEN JUST LEAVE. The only rules are the ones your dumb brain imposes on you."
                )

            elif user_input == "LOOK AROUND" or user_input == "ROOM":
              functions.print_conversationally(f"You are in the {main_character.current_room.name}. Here is what you see:\n\n") 

              main_character.current_room.print_items()
              print("\n")
              main_character.current_room.print_persons()
              print("\n")
              main_character.current_room.print_furniture()

            elif bonepart_intro == 1 and "HAT"  in user_input or "MAN" in user_input and main_character.current_room == bonepart.current_room:
              if bonepart_intro != 1:
                functions.print_conversationally(f"Did you mean to talk to {bonepart.name}?")
              else:
                bonepart_program.bonepart()
                main_character.start_quest(quest_1)

            elif bonepart_intro == 2 and "BONEPART" in user_input or "CHEF" in user_input and main_character.current_room == bonepart.current_room:
                if mood_set == 0:
                  functions.print_conversationally("'The fuck you still doing here? Go light the candles you monkey's ass.'")
                elif mood_set == 1:
                  functions.print_conversationally("What do you want a cookie!? We open in 10 minutes, go finish your duties.")
                  main_character.quest_completed(quest_1)
                  functions.print_conversationally(colored("\n\nCongratulations, you won!", "green"))
                  functions.print_conversationally(colored("\n\nGAME OVER", "red"))
                else:
                  pass

            elif main_character.current_room == hostess.current_room and  hostess_level == 1 and "WOMAN" in user_input or "BEAUTIFUL" in user_input:
                hostess_program.hostess()

            elif "JOANNE" in user_input and main_character.current_room == hostess.current_room and hostess_level == 2:
                if joanne_mood == 0:
                  functions.print_conversationally("'Fuck off.'")
                elif joanne_mood == 1:
                  functions.print_conversationally(f"{main_character.name}! We open in like five minutes! Go light the candles then help me set the tables.")


            elif main_character.current_room == manager.current_room and "MAN" in user_input or "OILY" in user_input or "LARGE" in user_input or "BALD" in user_input:
              if manager_level == 1:
                manager_program.manager()
              else:
                functions.print_conversationally("Sorry, I don't understand.")

            elif main_character.current_room == manager.current_room and "MANAGER" in user_input or "RUSSELL" in user_input or "DICKSWAB" in user_input and manager_level == 2:
                functions.print_conversationally("Waddaya want, a cookie? Get to work! We got customers coming.")

            elif "COW" in user_input and beef in main_character.current_room.foods:
              food.cow_meat()
              take_cow_meat = functions.menu("\n\nAdd to bag?",
               ["Yes", "No"])
              if take_cow_meat == "Yes":
                main_character.add_to_bag(beef)
                functions.print_conversationally("You added Cow Meat!")
                main_character.current_room.remove_food(beef)
              elif take_cow_meat == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")

            elif "COW" in user_input and beef not in main_character.current_room.foods and "DROP" not in user_input and "EAT" not in user_input:
              functions.print_conversationally(f"Keep it movin' pal. You've already got the only cow meat available. Don't be greedy.")

            elif "CHICKEN" in user_input and chicken in main_character.current_room.foods:
              food.chicken_meat()
              take_chicken = functions.menu("\n\nAdd to bag?",
               ["Yes", "No"])
              if take_chicken == "Yes":
                main_character.add_to_bag(chicken)
                functions.print_conversationally("You added Chicken Meat!")
                main_character.current_room.remove_food(chicken)
              elif take_chicken == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")

            elif "CHICKEN" in user_input and chicken not in main_character.current_room.foods and "DROP" not in user_input and "EAT" not in user_input:
              functions.print_conversationally(f"Keep it movin' pal. You've already got the only chicken meat available. Don't be greedy.")
  
            elif "MYSTERY" in user_input and mystery_meat in main_character.current_room.foods:
              food.mystery_meat()
              take_mystery_meat = functions.menu("\n\nAdd to bag?",
               ["Yes", "No"])
              if take_mystery_meat == "Yes":
                main_character.add_to_bag(mystery_meat)
                functions.print_conversationally("You added Mystery Meat!")
                main_character.current_room.remove_food(mystery_meat)
              elif take_mystery_meat == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")

            elif "MYSTERY" in user_input and mystery_meat not in main_character.current_room.foods and "DROP" not in user_input and "EAT" not in user_input:
              functions.print_conversationally(f"Keep it movin' pal. You've already got the only mystery meat available. Don't be greedy.")

            elif "COOK" in user_input:
              cooking.cook()
          
            elif "COUNTER" in user_input and counter in main_character.current_room.furnitures:
              main_character.current_room.print_items_on_furniture(counter)
              main_character.current_room.add_item(knife)
              main_character.current_room.add_food(salt)
              main_character.current_room.add_food(pepper)
              counter.remove_from_furn(knife)
              counter.remove_from_furn(salt)
              counter.remove_from_furn(pepper)

            elif "STOVE" in user_input and stove in main_character.current_room.furnitures:
              print("It's a stove.")

            elif "SINK" in user_input and sink in main_character.current_room.furnitures:
              print("It's a sink.")

            elif "OVEN" in user_input and oven in main_character.current_room.furnitures:
              print("It's an oven.")

            elif "KNIFE" in user_input and knife in main_character.current_room.items:
              objects.knife()
#enumerables! or object?/hash/map
            elif "KNIFE" in user_input and "DROP" not in user_input and knife not in main_character.current_room.items and knife in main_character.inventory:
              functions.print_conversationally(f"Seriously? You want another knife? God damn...")

            elif "CANDLE" in user_input  and candle in main_character.current_room.items:
              objects.candle()
              take_candle = functions.menu("\n\nAdd to bag?",
               ["Yes", "No"])
              if take_candle == "Yes":
                main_character.add_to_bag(candle)
                functions.print_conversationally("You added the candle!")
                dining_room.remove_item(candle)
              elif take_candle == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")

            elif "CANDLE"  in user_input and "DROP" not in user_input and "LIGHT" not in user_input and candle not in main_character.current_room.items and candle  in main_character.inventory:
              functions.print_conversationally(f"No way you maniac. Leave some candle for the rest of us.")

            elif "TABLE" in user_input and table in main_character.current_room.furnitures:
              if lit_candle in main_character.inventory:
                mood_lighting = functions.menu("Would you like to put the candle on the table?", ["Yes", "No"])
                if mood_lighting == "Yes":
                  actions.set_the_mood()
                else:
                  functions.print_conversationally("Okay. But careful, keeping a lit candle in your bag could backfire eventually.")
              else:
                main_character.current_room.print_items_on_furniture(table)
                if candle in table.items:
                  main_character.current_room.add_item(candle)
                  table.remove_from_furn(candle)
                else:
                  pass

            elif "CUPBOARD" in user_input:
              main_character.current_room.print_items_on_furniture(cupboard)
              main_character.current_room.add_item(matches)

            elif "MATCHES" in user_input and "LIGHT" not in user_input and matches in main_character.current_room.items:
              objects.matches()
              take_matches = functions.menu("\n\nAdd to bag?",
               ["Yes", "No"])
              if take_matches == "Yes":
                main_character.add_to_bag(matches)
                functions.print_conversationally("You added some matches!")
                bathroom.remove_item(matches)
              elif take_matches == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")

            elif "MATCHES" in user_input and "DROP" not in user_input and "LIGHT" not in user_input and matches not in main_character.current_room.items and matches in main_character.inventory:
              functions.print_conversationally(f"More matches? Damn dude, I was kidding about the arson...")

            elif "LIGHT" in user_input and matches in main_character.inventory and candle in main_character.inventory:
              actions.light_candle()

            elif "QUEST" in user_input:
              main_character.quest_log()
              # know_more = functions.menu("\nWanna know more?", ["Yes", "No"])
              # if know_more == "Yes":
              #   which_quest = functions.menu("Which quest?", [f"{main_character.print_quests()}"])
              #   if which_quest == main_character.print_quest_name(Quest):
              #     functions.print_conversationally(main_character.quest_duties(Quest))
              #   else:
              #     pass
              # elif know_more == "Yes":
              #   functions.print_conversationally("Oh, so Your Majesty knows exactly what to do then?")

            elif "BAG" in user_input:
              look_in_bag = functions.menu(
                  "Want to know what's in your bag?", ["Yes", "No"])
              if look_in_bag == "Yes":
                main_character.print_bag()
              elif look_in_bag == "No":
                functions.print_conversationally(
                  "Okay then, we won't do that. Was there something else you wanted to do?"
                  )

            elif "DROP" in user_input:
              if "COW" in user_input:
                main_character.remove_from_bag(beef)
                functions.print_conversationally("You dropped the cow meat!")
              elif "KNIFE" in user_input:
                main_character.remove_from_bag(knife)
                functions.print_conversationally("You dropped the knife!")
              elif "CANDLE" in user_input:
                main_character.remove_from_bag(candle)
                functions.print_conversationally("You dropped the candle!")
              elif "MATCHES" in user_input:
                main_character.remove_from_bag(matches)
                functions.print_conversationally("You dropped the matches!")
              elif "CHICKEN" in user_input:
                main_character.remove_from_bag(chicken)
                functions.print_conversationally("You dropped the chicken meat!")
              else:
                functions.print_conversationally("What do you want to drop?")

            elif "EAT" in user_input and len(main_character.foods) > 0:
                eat_what = functions.menu("Eat what?", 
                                          main_character.foods)
                if eat_what in main_character.foods:
                  if eat_what.cooked == True:
                    main_character.eat_food(eat_what)
                  else:
                    functions.print_conversationally("blech! That shit's raw fool!")
                else:
                  pass

            elif "DO I HAVE FOOD" == user_input:
              main_character.print_food()

            elif "SALT" in user_input and salt in main_character.current_room.foods:
              food.salt()
              take_salt = functions.menu("\n\nAdd to bag?", ["Yes", "No"])
              if take_salt == "Yes":
                main_character.add_to_bag(salt)
                functions.print_conversationally("You added salt!")
                main_character.current_room.remove_food(salt)
              elif take_salt == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")

            elif "PEPPER" in user_input and pepper in main_character.current_room.foods:
              food.pepper()
              take_pepper = functions.menu("\n\nAdd to bag?", ["Yes", "No"])
              if take_pepper == "Yes":
                main_character.add_to_bag(pepper)
                functions.print_conversationally("You added pepper!")
                main_character.current_room.remove_food(pepper)
              elif take_pepper == "No":
                functions.print_conversationally(
                  "Forget that! What else do you wanna do?")
            
            elif user_input == "LEAVE":

              functions.print_conversationally("\nWhere would you like to go?\n")

              functions.print_conversationally( main_character.current_room.print_neighbors())

              def room_change():
                room_change = False

                where_to = functions.get_user_input().upper()

                if where_to == "KITCHEN":
                  main_character.enter_room(kitchen)
                  room_change = True
                elif where_to == "DINING ROOM":
                  main_character.enter_room(dining_room)
                  room_change = True
                elif where_to == "MEAT LOCKER":
                  main_character.enter_room(meatLocker)
                  room_change = True
                elif where_to == "BATHROOM":
                  if len(bathroom.persons) >= 1:
                    functions.print_conversationally("'Sorry! Someone's in here.'")
                    functions.print_conversationally(f"\n\nYou are still in the {main_character.current_room.name}")
                    waitress_program.bathroom_dance()
                  else:
                    main_character.enter_room(bathroom)
                    room_change = True
                else:
                  pass

                if room_change == True:
                  functions.print_conversationally(f"You are now in the {main_character.current_room.name}.")
                else:
                  pass

              room_change()

            else:
              functions.print_conversationally("\nSorry, I don't understand.")


meatLocker = Room("Meat Locker")

kitchen = Room("Kitchen")

dining_room = Room("Dining room")

bathroom = Room("Bathroom")


meatLocker.add_neighbor("West", kitchen)

kitchen.add_neighbor("South", dining_room)
kitchen.add_neighbor("East", meatLocker)

dining_room.add_neighbor("North", kitchen)
dining_room.add_neighbor("East", bathroom)

bathroom.add_neighbor("West", dining_room)

#FURNITURE
stove = Furniture("Stove")
sink = Furniture("Sink")
oven = Furniture("Oven")
table = Furniture("Table")
cupboard = Furniture("Cupboard")
counter = Furniture("Counter")

# MEATLOCKER
beef = Food("Cow meat", 5, "beefy")
meatLocker.add_food(beef)  
chicken = Food("Chicken meat", 3, "chickeny")
chicken.cook_food()
meatLocker.add_food(chicken)
mystery_meat = Food("Mystery meat", 10, "addicting")
meatLocker.add_food(mystery_meat)

# KITCHEN
knife = Item("Knife")
salt = Food("Salt", 0.5, "salty")
pepper = Food("Pepper", 0.5, "peppery")
notepad = Item("Notepad")
# kitchen.add_item(knife)
kitchen.add_furniture(stove)
kitchen.add_furniture(sink)
kitchen.add_furniture(oven)
kitchen.add_furniture(counter)
counter.add_item_to_furniture(knife)
counter.add_item_to_furniture(salt)
counter.add_item_to_furniture(pepper)


# DINING ROOM
candle = Item("Candle")
# dining_room.add_item(candle)
table.add_item_to_furniture(candle)
dining_room.add_furniture(table)
candle_is_lit = 1
lit_candle = Item("Lit candle")

# BATHROOM
matches = Item("Matches")
# bathroom.add_item(matches)
cupboard.add_item_to_furniture(matches)
bathroom.add_furniture(cupboard)

#CHARACTERS
main_character = person_class.Person("Main Character", 00)
main_character.enter_room(meatLocker)

# meatLocker.print_persons()

bonepart = person_class.Person("A man with a chef hat", 52)
bonepart.side_character_enter_room(meatLocker)
bonepart_intro = 1

hostess = person_class.Person("The most beautiful woman you've ever seen", 23)
hostess.side_character_enter_room(dining_room)
hostess_level = 1

waitress = person_class.Person("Fanny", 38)
waitress.side_character_enter_room(bathroom)
waitress_intro = 1

manager = person_class.Person("A large, bald, oily looking man", 42)
manager.side_character_enter_room(kitchen)
manager_intro = 1
manager.add_to_bag(notepad)
manager_level = 1

#COOKBOOK
cookbook = cooking.Cookbook()

#COOKING
steak = cooking.Meal("Steak", 15, "Steaklike")
steak_recipe = cooking.Recipe("Steak", 15)

steak_recipe.add_ingrediants([beef, salt, pepper])
steak.add_recipe(steak_recipe)

cookbook.add_meal_recipe_to_cookbook(steak)

roasted_chicken = cooking.Meal("Roasted Chicken", 10, "Chickeny")
roasted_chicken_recipe = cooking.Recipe("Roasted Chicken", 10)

roasted_chicken_recipe.add_ingrediants([chicken, salt, pepper])
roasted_chicken.add_recipe(roasted_chicken_recipe)

cookbook.add_meal_recipe_to_cookbook(roasted_chicken)

# print(steak_recipe.ingrediants)
# for i in steak_recipe.ingrediants:
#   print(i.name)
# print(steak.recipe)

# if set(['a', 'b']).issubset(['a', 'b', 'c']):
#   print("True")
# else:
#   print("false")

# for i in cookbook.recipes:
#   print(i)
#   print(i.name)
#   print(i.recipe)
#   for j in i.recipe:
#     print(j.name)
#     print(j.ingrediants)
#     print(j.ingrediants)
#     for k in j.ingrediants:
#       print(k.name)

# for h in steak.recipe:
#   for i in cookbook.recipes:
#     for j in i.recipe:
#       for k in j.ingrediants:


# if set(steak_recipe.ingrediants).issubset(cookbook.recipes):
#   print("true")
# else:
#   print("fuck")



# if main_character.current_room == hostess.current_room:
#   print("fuck me")

#QUESTS
quest_1 = Quest("Light the Candle", "Find the candle, find something to light it, actually light it, then put it back.")
quest_2 = Quest("Opening Duties", "Idk like roll the silverware or something")
quest_3 = Quest("Learn to Fight", "Duck and weave baby")

# main_character.start_quest(quest_2)
# main_character.start_quest(quest_3)

# main_character.print_quests()

mood_set = 0
joanne_mood = 0
game = Game()
game.start()
