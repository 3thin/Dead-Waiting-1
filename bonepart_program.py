from time import sleep
from typing import List
from termcolor import colored
import sys

import functions
import world
import person_class

def bonepart():
    world.bonepart.leave_room(world.meatLocker)
    world.bonepart.name = "Chef Bonepart"
    world.bonepart.side_character_enter_room(world.meatLocker)
    world.bonepart_intro = 2
    functions.print_conversationally("You approach the man in the chef hat. He stares at you. \n\n 'What the fuck do you want?'")
    what_do_you_want = functions.menu("\n\nWhat do you want?", ["Nothing, stop asking, go away.", "I just want to know what the hell is going on!", "Less crippling anxiety.", "Your pants."])

    if what_do_you_want == "Nothing, stop asking, go away.":
      functions.print_conversationally("'Don't you ever tell me what to do you arrogant neanderthal.'\n\nThe man gives you a lopsided grin.")
    elif what_do_you_want == "I just want to know what the hell is going on!":
      functions.print_conversationally("'Wittle baby wants to know what's going on? Wittle baby's confused about the unpredicatable and at times irrational nature of their world? Wittle baby's scared? Well, don't worry wittle baby. You're about be fired, THAT'S what's happening.'\n\nThe man laughs at the look on your face.")
    elif what_do_you_want == "Less crippling anxiety.":
      functions.print_conversationally("'I can understand that. It's a difficult world we must traverse. But please, whatever's bothering you, leave it at the door. I'm trying to run a business here.'\n\nHe gives you a knowing look.")
    elif what_do_you_want == "Your pants.":
      functions.print_conversationally("'Are you coming onto me? Because if so baby save it for later.' He winks.")

    functions.print_conversationally("\n\n'Okay, enough playing around. For real, who the fuck are you?'")

    user_name = functions.get_user_input("\n\nEnter your name:").capitalize()

    functions.print_conversationally(
    f"'Right, right, right. {user_name}. You're new? Jesus, you're old to be working this job. How old are you?'"
      )
  
    user_age = functions.get_user_num()

    world.main_character = person_class.Person(user_name, user_age)

    world.main_character.enter_room(world.meatLocker)

    joke_age = str(int(world.main_character.age) + 10)
    
    functions.print_conversationally(
    f"'No shit? Really? You look terrible. I thought you were at least... I dunno... {joke_age}?'\n\n'Anyways, Cumrade {world.main_character.name}ova, if you don't get your ass out of this locker and start working, then I'm going to destroy you. Now go!'"
      )

    one_last_thing = functions.menu("", ["Wait, who are you?", "Wait, what should I do?", "I don't like the way you're talking to me.", "Yes sir, right away sir, absolutely sir!"])

    if one_last_thing == "Wait, who are you?":
      functions.print_conversationally("'You seriously don't know? The name's Bonepart. I'm the motherfucking chef.'")
    elif one_last_thing == "Wait, what should I do?":
      functions.print_conversationally(f"God dammit, {world.main_character.name}. You need me to do your job for you? Go light the fucking candles. Let me know when you're done.'")
    elif one_last_thing == "I don't like the way you're talking to me.":
      functions.print_conversationally("'I don't give a fuck. I'm Chef motherfucking Bonepart. Do your job or find a new one.'")
    elif one_last_thing == "Yes sir, right away sir, absolutely sir!":
      functions.print_conversationally("'You're a fucking smartass, you know that?'")
