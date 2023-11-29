import functions
import world
import person_class
import waitress_program

def bonepart_and_waitress():
  #SCENE ONE = WAITRESS TELLS ON YOU
  if waitress_program.bonepart_and_waitress_scene == 1:
    functions.print_conversationally(f"As you enter the {world.main_character.current_room}, you see {world.waitress.name} standing at attention besides {world.bonepart.name}. He notices you and speaks:\n\n'Fall in, {world.main_character.name}.'\n\nYou do as he asks.\n\n'Tonight is a special night. Do either of you maggots know why tonight is a special night?'")

    special_night = functions.menu("What's so special about tonight?", ["It's Shabbat", "You're getting laid", "Because we're here together"])

    if special_night == "It's Shabbat":
      functions.print_conversationally("'Well, I can't say you're wrong but you're not right.'")
    elif special_night == "You're getting laid":
      functions.print_conversationally(f"'That's nothing special, {world.main_character.name}. For someone of my standing, that's just another night.'")
    else:
      functions.print_conversationally("'Fuck if I care whether we're here together? Go die in a ditch for all I care.'")
    
    
    \n\n'It's Shabbat, sir.'\n\n'No! I mean, yes, but there's another reason it's special. We have a special guest coming. ")
  else:
    pass
