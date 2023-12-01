from time import sleep
from typing import List
from termcolor import colored
import sys

import functions
import world
import person_class

def knife():
  functions.print_conversationally("You have discovered a knife! Nice. This could come in handy. Just be careful not to–OUCH! You cut yourself on it...")
  world.main_character.take_damage(12)
  take_knife = functions.menu("\n\nAdd to bag?", ["Yes", "No"])
  if take_knife == "Yes":
      world.main_character.add_to_bag(world.Item(world.knife))
      functions.print_conversationally("You added a knife!")
      world.kitchen.remove_item(world.knife)
  elif take_knife == "No":
      functions.print_conversationally("Forget that! What else do you wanna do?")

def candle():
  functions.print_conversationally("You found a candle! But no matches... This is pretty fucking useless, huh?")

def matches():
  functions.print_conversationally("Matches! Awesome! Can't wait to commit arson.")

def notepad():
  world.main_character.add_to_bag(notepad)
  functions.print_conversationally("Sick! A notepad. If only you had a pen to write on it...")
