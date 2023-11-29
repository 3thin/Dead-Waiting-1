import functions
import world
import person_class

def hostess():
    world.hostess.leave_room(world.dining_room)
    world.hostess.name = "Joanne"
    world.hostess.side_character_enter_room(world.dining_room)
    world.hostess_intro = 2
    functions.print_conversationally(f"Standing in front of you is the most absolutely stunning woman you've ever seen. You recognize her from earlier. Joanne. Her name shoots off fireworks in your mind. You stumble towards her, your words caught in your throat. She turns her gaze on you and your heart stops. Behind those dark, hooded eyes you get the sense that she is better than you.\n\n 'You're staring again, {world.main_character.name}. Can you please fuck off?'")

    functions.print_conversationally("\n\nWow! She knows your name!")

    please_fuck_off = functions.menu("\n\nHow do you respond?", ["I'm not staring, I'm looking.", "I was just going to ask if we have any reservations.", "Where can I find the matches?", "Wow, I did NOT mean to stare, I was just hoping you might be able to help me with something."])

    if please_fuck_off == "I'm not staring, I'm looking.":
      functions.print_conversationally("'You're a dirty little child.' She steps forward and slaps you. Her nails leave deep scratches in your cheek.")

      world.main_character.take_damage(5)

      functions.print_conversationally("\n\nJoanne turns away like you never even existed.")

      world.main_character.lose_charisma(15)

      world.hostess_level = 2

    elif please_fuck_off == "I was just going to ask if we have any reservations.":
      functions.print_conversationally("Your lies don't deceive her. She scoffs and turns away. 'I guess you'll just have to find out for yourself, won't you?'")

      what_do = functions.menu("\n\nWhat next?", ["Apologize for staring and ask for help", "Leave"])

      if what_do == "Apologize for staring and ask for help":
        functions.print_conversationally("Fine, creep. What do you need help with?")

        world.joanne_mood = 1

        how_can_she_help = functions.menu("\n\nWhat can she help you with?", ["Finding the matches", "Finding the candle"])

        if how_can_she_help == "Finding the matches":
          functions.print_conversationally("Look in the bathroom. They're usually somewhere around there.")
          world.hostess_level = 2
        elif how_can_she_help == "Finding the candles":
          functions.print_conversationally("She stares at you for second then laughs. It's beautiful. 'Dude, they're on the table!'")
          world.hostess_level = 2

      else:
        functions.print_conversationally("What next?")

    elif please_fuck_off == "Where can I find the matches?":
      functions.print_conversationally("'Did you think to look in the bathroom?' She turns away, muttering to herself. 'Idiot...'")

      world.joanne_mood = 1
      world.hostess_level = 2

    else:
      functions.print_conversationally(f"'You are a terrible liar, {world.main_character.name}... But your helplessness is a little endearing, I guess. Fine. What can help you with?'")

      world.joanne_mood = 1

      how_can_she_help = functions.menu("\n\nWhat can she help you with?", ["Finding the matches", "Finding the candle"])

      if how_can_she_help == "Finding the matches":
        functions.print_conversationally("Look in the bathroom. They're usually somewhere around there.")
        world.hostess_level = 2
      elif how_can_she_help == "Finding the candle":
        functions.print_conversatioanlly("She stares at you for second then laughs. It's beautiful. 'Dude, they're on the table!'")
        world.hostess_level = 2
