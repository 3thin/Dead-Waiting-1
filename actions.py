from time import sleep
from typing import List
from termcolor import colored
import sys

import functions
import world
import person_class

def light_candle():
  if world.candle_is_lit == 1:
    functions.print_conversationally("Using your matches, you light the candle. Suddenly, you're a little bit less anxious. ")
    world.main_character.heal_some(5)
    world.main_character.use_item(world.matches)
    world.main_character.use_item(world.candle)

    world.main_character.add_to_bag(world.lit_candle)
    functions.print_conversationally(colored(f"\n\nCongratulations! You added the {world.lit_candle.name} to your bag.", "green"))

    world.candle_is_lit = 2

table_is_lit = 0

def set_the_mood():
  functions.print_conversationally("You set the lit candle on the table. The room grows brighter. It's almost inviting")
  world.mood_set = 1
  table_is_lit = 2
  functions.print_conversationally(colored("\n\nCongratulations! You lit the dining room with a candle. If this game was further developed, you'd get a point or something!", "green"))

  world.table.add_item_to_furniture(world.lit_candle)

  world.main_character.use_item(world.lit_candle)
