import functions
import world
import person_class
import objects

def manager():
    world.manager.leave_room(world.kitchen)
    world.manager.name = "Dickswab aka Russell"
    world.manager.side_character_enter_room(world.kitchen)
    world.bonepart_intro = 2

    functions.print_conversationally("The large, bald man looks up from his clipboard and stares at you, his eyes black pits of ignorance. 'Waddaya want?' Now you remember. This is your manager: Russell. You also remember that the man is a complete and total dickswab.")

    waddaya_want = functions.menu("\n\nWaddaya want?", ["Nothing, just passing through.", "To tell you how great you look today!", "When do I get paid?", "World peace, brother. Just for everyone to get along."])


    if waddaya_want == "Nothing, just passing through.":
      functions.print_conversationally(f"{world.manager.name} grunts and turns back to his clipboard.")
      world.manager_level = 2

    elif waddaya_want == "To tell you how great you look today!":
      functions.print_conversationally("His eyes narrow as though trying to detect any sarcasm which, of course, there was. But his tiny little mind can't comprehend that an underling would dare to disrespect him. He smiles. 'Thanks, kid. You too. That's okay to say right?'")
      world.main_character.gain_charisma(10)
      world.manager_level = 2

    elif waddaya_want == "When do I get paid?":
      functions.print_conversationally("When you actually do your job twerp. C'mon, we're opening soon. Get back to work.")
      world.manager_level = 2

    else:
      functions.print_conversationally(f"'Truth, man! It's a fucked up world out there. We could all stand to gain a little compassion.' This surprises you, as typically {world.manager.name} is a bit of a giant throbbing cock. But hey, I guess people can surprise you.\n\nYou turn to leave but he stops you by putting a hand on your shoulder. 'Don't forget your notepad, kid.'")
      objects.notepad()
      world.manager_level = 2
      
      
