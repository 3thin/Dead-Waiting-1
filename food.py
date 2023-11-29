from time import sleep
from typing import List
from termcolor import colored
import sys

import functions
import world

def cow_meat():
  functions.print_conversationally(
						    "You found cow meat! It's rotten. Blech."
						)

def chicken_meat():
  functions.print_conversationally(
    "You found some micken cheat! I mean, chiten meak! I mean... you know what I mean."
  )

def mystery_meat():
  functions.print_conversationally("You found some mystery meat! Wonder what it's made of...")

def salt():
  functions.print_conversationally("Small flavorful rocks! Nice!")

def pepper():
  functions.print_conversationally("Achoo! Jeez louise that pepper's strong stuff...")
