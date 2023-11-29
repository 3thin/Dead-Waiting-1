from time import sleep
from typing import List
from termcolor import colored
import sys
import world

def get_user_input(prompt = ""):
  if prompt != "":
    print(prompt)
  print(colored("\n\n > ", 'green'), end='')
  user_input = input()
  print()
  return user_input

def get_user_num(prompt = ""):
  if prompt != "":
    print(prompt)
  print(colored("\n\n > ", 'green'), end='')
  
  while True:
    try:
      user_num = int(input())
      break
    except ValueError:
      print_conversationally(f"\n'Hold the phone,that ain't no number–at least not one I can understand. Try it again using the universal language: math!'")
      print(colored("\n\n > ", 'green'), end='')
      continue

  print()
  return user_num

def print_conversationally(line):
  for char in line:
    print(char, end='')
    sys.stdout.flush()
    if char == '.' or char == '?':
      sleep(.4)
    elif char == ',':
      sleep(.2)
    elif char == '\n':
      sleep(.5)
    elif char == '–':
      sleep(.3)
    else:
      sleep(.05)
  return ''

def menu(menu_prompt: str, menu_options: List[str]) -> str:

  # listy = ''
  
  if len(menu_options) == 0:
    raise Exception("Need to have at least one option")
  if len(menu_options) > 26:
    raise Exception("More than 26 options will distract the user")
  # if menu_options = []:
  #   listy.join(menu_options)
    
    
  
  all_letters = "abcdefghijklmnopqrstuvwxyz"

  def get_user_choice():
    print_conversationally(colored(menu_prompt, "green"))
    print()
    print()
    for index, option in enumerate(menu_options):
      if option in world.main_character.foods:
        print(colored(all_letters[index] + ') ', 'green'), option.name)
      else:
        print(colored(all_letters[index] + ') ', 'green'), option)
    choice = get_user_input()
    return choice

  valid_options = set()
  for i in range(len(menu_options)):
    valid_options.add(all_letters[i])

  choice = get_user_choice()
  while choice not in valid_options:
    print("Sorry, you must pick one of the available options")
    choice = get_user_choice()

  return menu_options[all_letters.index(choice)]
