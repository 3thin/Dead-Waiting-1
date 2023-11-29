import functions
import world
import person_class
import objects
import bonepart_program

def bathroom_dance():

  now_do_what = functions.menu("\n\nHow would you like to respond?", ["I really need to get in there!", "How much longer will it take?", "Get out!"])

  if now_do_what == "I really need to get in there!":
    if world.main_character.charisma > 69:
      charismatic_bathroom_dance()
    else:
      functions.print_conversationally("'Well, I really need to be in here. Tough luck, bud.'")

  elif now_do_what == "How much longer will it take?":
    if world.main_character.charisma > 69:
      charismatic_bathroom_dance()
    else:
      functions.print_conversationally("'I don't know! A couple minutes? Just give me some privacy, I can't go with you talking to me.")


  else:
    if world.main_character.charisma > 84:
      charismatic_bathroom_dance()
    else:
      functions.print_conversationally("'I'm going to pretend you didn't say that. But disrespect me again and you will never get in this bathroom.'")

def charismatic_bathroom_dance():
  functions.print_conversationally(f"A pause. Then you hear the voice ask, '{world.main_character.name}? Is that you?'\n\nOf course. It's {world.waitress.name}, the waitress. How is it that she's always in here?\n\n")

  world.waitress.name = "Fanny"

  what_say = functions.menu("What do you say?", [f"Yeah, {world.waitress.name}, it's me. I just need to grab the matches.", f"You put on a passable {world.bonepart.name} impression. 'No, it's {world.bonepart.name}. What the fuck is taking you so long?'", "Can you hurry the fuck up? I've gotta get in there!"])

  if what_say == f"Yeah, {world.waitress.name}, it's me. I just need to grab the matches.":
      functions.print_conversationally(f"'Oh shoot! Sorry, my stomach feels like Pompeii. Give me a sec.'\n\nA moment. You hear shuffling and a cabinet opening then closing. The door opens a smidge and a pack of matches slide into the {world.main_character.current_room.name}.\n\n")
      world.waitress.add_to_bag(world.Item(world.matches))
      world.waitress.current_room.remove_item(world.matches)
      world.main_character.current_room.add_item(world.matches)
      if world.matches in world.main_character.current_room.items:
        objects.matches()
        take_matches = functions.menu("\n\nAdd to bag?", ["Yes", "No"])
        if take_matches == "Yes":
          world.main_character.add_to_bag(world.Item(world.matches))
          functions.print_conversationally("You added some matches!")
          world.main_character.current_room.remove_item(world.matches)
        elif take_matches == "No":
          functions.print_conversationally(
          "Forget that! What else do you wanna do?")
    
  elif what_say == f"You put on a passable {world.bonepart.name} impression. 'No, it's {world.bonepart.name}. What the fuck is taking you so long?'":
    functions.print_conversationally("'Oh, shit! Chef! Um, sorry, I think I have food poisoning or something––'\n\n")
    bonepart_impression = functions.menu("", ["'Are you saying my food poisoned you?'", f"'Oh, I'm sooo sorry my food poisoned you, {world.waitress.name}!'"])
    functions.print_conversationally("'I'm so sorry, sir! I didn't mean––")
    impression_bone_parttwo = functions.menu("", ["'Get out, now.'", f"'It's okay, {world.waitress.name}, I'm only fucking with you! It's {world.main_character.name}!'"])
    if impression_bone_parttwo == "'Get out, now.'":
      functions.print_conversationally(f"You hear pants zipping and a toilet flushing. The door swings open and in walks {world.waitress.name}. You grin at her.\n\n'You forgot to wash your hands.'\n\n'You dick!'\n\n'Sorry, {world.waitress.name}, I couldn't resist. Bonepart's in the meat locker. I thought I'd mess with you while I had the chance.'\n\n'I'll get you back you know.'\n\n{world.waitress.name} brushes past your shoulder as she exits the room.")
      world.waitress.leave_room(world.bathroom)
      world.waitress.enter_room(world.meatLocker)
      bonepart_and_waitress_scene = 1
    else:
      functions.print_conversationally(f"'What the fuck, {world.main_character.name}? You're a dick.'\n\nNice going, idiot. Maybe you thought you were harmlessly flirting but you actually hurt {world.waitress.name}'s feelings.")
      world.main_character.lose_charisma(10)
      functions.print_conversationally(f"\n\n{world.waitress.name} stalks out of the bathroom and stares you in the eyes.\n\n'Fuck with me again, {world.main_character.name}, and you'll regret it.'\n\n{world.waitress.name} brushes past your shoulder and exits the room.")
      world.waitress.leave_room(world.bathroom)
      world.waitress.enter_room(world.meatLocker)

  else:
    functions.print_conversationally("'Why, what's so urgent?'")
    what_is_urgent = functions.menu("", ["I have to poo, really bad.", "I just need to get the matches", "Bonepart's been calling for you and is starting to get pissed."])

    if what_is_urgent == "I have to poo, really bad.":
      functions.print_conversationally("'How bad?'")
      how_bad = functions.menu("", ["Real bad. I have IBS.", "Not like THAT bad..."])

      if how_bad == "Real bad. I have IBS.":
        functions.print_conversationally(f"'Jesus, {world.main_character.name}, I didn't realize...'\n\nYou hear flushing and the zipping of pants. {world.waitress.name} steps out of the bathroom, a look of pity in her eye.\n\n'I won't tell anyone. I swear.' \n\nShe steps aside and allows you to enter the bathroom.")
        world.waitress.leave_room(world.bathroom)
        world.waitress.enter_room(world.meatLocker)
        world.main_character.enter_room(world.bathroom)
        functions.print_conversationally(f"You are now in the {world.main_character.current_room.name}.")
      else:
        functions.print_conversationally("'Well, just give me a couple more minutes and I'll be out.")
    elif what_is_urgent == "I just need to get the matches":
      functions.print_conversationally(f"'Well, why didn't you say so?'\n\nYou hear flushing and the zipping of pants, then {world.waitress.name} walks out of the bathroom.\n\n'What, forget to wash your hands?'\n\n{world.waitress.name} squints at you. 'Ha ha. Now if you'll excuse me, I'm going to find Bonepart.'")

      world.waitress.leave_room(world.bathroom)
      world.waitress.enter_room(world.meatLocker)
    else:
      functions.print_conversationally(f"'Really? Oh shit...'\n\nYou hear the zipping of pants and the toilet flushing. {world.waitress.name} runs out of the bathroom, bumps into your shoulder, and heads for the back.\n\nYou call out, 'You forgot to wash your hands!' But she's already gone. That shoulder bump actually really hurt...")
      world.waitress.leave_room(world.bathroom)
      world.waitress.enter_room(world.meatLocker)
      world.main_character.take_damage(5)
      bonepart_and_waitress_scene = 2
