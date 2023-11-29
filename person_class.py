from time import sleep
from typing import List
from termcolor import colored
import sys

import functions
import world

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.reputation = 70
        self.intelligence = 75
        self.rooms = []
        self.current_room = world.Room
        self.inventory = []
        self.foods = []
        self.cooked_food = []
        self.quests = []
        self.charisma = 75

    def enter_room(self, Room):
        self.rooms.append(Room.name)
        self.current_room = Room

    def side_character_enter_room(self, Room):
        self.current_room = Room
        self.current_room.persons.append(self.name)
    
    def leave_room(self, Room):
        self.current_room.persons.remove(self.name)

    def print_room(self):
        for room in self.rooms:
            return room

    def return_room(self):
        return self.current_room

    def add_to_bag(self, item):
      if len(self.inventory) >= 5:
        functions.print_conversationally("You have too many items in your bag!")
      elif item in world.main_character.current_room.foods:
        self.foods.append(item)
      else:
        self.inventory.append(item)

    def print_food(self):
        functions.print_conversationally(colored("Food:\n", "green"))
        for item in self.foods:
            functions.print_conversationally(f"{world.food.name}\n")
        if len(self.inventory) == 0:
          functions.print_conversationally("\nThere's nothing in your bag.")
        else:
          pass


      # if len(self.inventory) <= 5:
      #   self.inventory.append(item.name)
      # else:
      #   functions.print_conversationally("You have too many items in your bag!")

    def remove_from_bag(self, item):
        if item == item in self.inventory:
          self.inventory.remove(item)
          world.main_character.current_room.items.append(item)
        else:
          pass

    def use_item(self, item):
        if item == item in self.inventory:
          self.inventory.remove(item)
        else:
          pass

    def print_bag(self):
        functions.print_conversationally(colored("Bag:\n", "green"))
        for item in self.inventory:
            functions.print_conversationally(f"{item.name}\n")
        for food in self.foods:
            functions.print_conversationally(f"{food.name}\n")
        if len(self.inventory) == 0 and len(self.foods) == 0:
          functions.print_conversationally("\nThere's nothing in your bag.")
        else:
          pass
            
    def set_name(self):
        character_name = input()
        character_name = Person(character_name)

    def take_damage(self, damage):
      self.health = self.health - damage
      functions.print_conversationally(colored(f"\n\nSorry, you took {damage} damage.\n\n", "red"))
      functions.print_conversationally(colored("Health: ", "green"))
      functions.print_conversationally(f"{self.health}")

    def heal_some(self, health):
      if world.main_character.health == 100:
        functions.print_conversationally("Slow down there, bucko! You're already at full health.")
      else:
        world.main_character.health = world.main_character.health + health
        functions.print_conversationally(colored(f"\n\nNice, you healed {health} health.\n\n", "green"))
        functions.print_conversationally(colored("Health: ", "green"))
        functions.print_conversationally(f"{self.health}")


    def start_quest(self, quest):
      self.quests.append(quest.name)

    def quest_completed(self, quest):
        if quest == quest in self.quests:
          self.quest.remove(quest)
        else:
          pass
    
    def quest_log(self):
      functions.print_conversationally(colored("Quests:\n", "green"))
      for quest in self.quests:
        functions.print_conversationally(f"{quest}\n")
      if len(self.quests) == 0:
        functions.print_conversationally("\nYou have no active quests.")
      else:
        pass

    def print_quests(self):
      for quest in self.quests:
        functions.print_conversationally(f"{quest}\n")
      else:
        pass

    def print_quest_name(self, quest):
      functions.print_conversationally(f"{quest.name}\n")

    def quest_duties(self, quest):
      functions.print_conversationally(f"{quest.duties}\n")

    def eat_food(self, food):
      if world.main_character.health == 100:
        functions.print_conversationally("Chill out, fatass. I don't think you should eat any more or else those pants your sportin' might just blow wide open.")
      elif food.nutrition + world.main_character.health >= 100:
        functions.print_conversationally("Chill out, fatass. I don't think you should eat any more or else those pants your sportin' might just blow wide open.")  
      else:
        functions.print_conversationally(f"Om nom nom. You ate the {food.name.lower()}. Did it taste good?")
        world.main_character.heal_some(food.nutrition)
        world.main_character.foods.remove(food)

    def lose_charisma(self, blunder):
      self.charisma = self.charisma - blunder
      functions.print_conversationally(colored(f"\n\nSorry, not very charismatic. This blunder cost you {blunder} charisma.\n\n", "red"))
      functions.print_conversationally(colored("Charisma: ", "green"))
      functions.print_conversationally(f"{self.charisma}")

    def gain_charisma(self, affability):
      self.charisma = self.charisma + affability
      functions.print_conversationally(colored(f"\n\nHell yeah! You're smooth as hell! + {affability} charisma.\n\n", "green"))
      functions.print_conversationally(colored("Charisma: ", "green"))
      functions.print_conversationally(f"{self.charisma}")
      
