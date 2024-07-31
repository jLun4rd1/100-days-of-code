from assets import *
import time
import sys
#SEGMENTS FUNCTIONS


print(treasure_chest)
type_input("Welcome to Treasure Island.\nYour mission is to find the treasure.\nPress ENTER to continue the dialogue")

# Intro - Either Shadow or Cocounut. Coconut is punished 3 times.
water_shadow = type_input("\n---\nYou find yourself completely alone on a beach. The sun is burning hot. What do you do?\nType 'shadow' to search for a shadow. Type 'coconut' to look for coconuts.\nR: ")
shadow = False
coconut_max_attempts = 0
while shadow == False and coconut_max_attempts < 2:
  if water_shadow == "shadow":
    
    shadow = True
    type_input("\n---\nYou turn around and see a lot of trees that make up a forest. There's plenty of shadow")
  else:    
    if coconut_max_attempts == 0:
      health -= 1
      coconut_max_attempts +=1
      type_input("\n---\nYou waste a lot of your time looking for coconuts. Your throat is dry. You lost 1 health.")
      type_input("The sand below your naked feet is getting hotter. What do you do?\nType 'shadow' to search for a shadow. Type 'coconut' to keep looking for coconuts.\nR: ")
    elif coconut_max_attempts == 1:
      health -= 1
      coconut_max_attempts +=1
      type_input("\n---\nYou waste a lot more time looking for coconuts!! You're rethinking your bad decisions. You lost 1 more health.")
      type_input("The sand below your naked feet is quite uncomfortable. What do you do?\nType 'shadow' to search for a shadow. Type 'coconut' to keep looking for coconuts.\nR: ")
                    
if coconut_max_attempts == 2:
  shadow = True
  type_input("\nYou gave up on looking for coconuts and decided to go for the shadow.")
  type_input("You turn around and see a lot of trees that make up a forest. There's plenty of shadow")

## Part 2 - Either investigate or move_on. Both have their own branches.
# Investigate - can either lead into the cave or die going back to the beach.
# Move on - takes the player to the second ending following the quiet_help branch.
if shadow == True:
  type_input("\n---\nYou see tall trees that cover the sky, a thick grass that makes the ground soft and a mysterious light deep inside the forest.")
  print(forest)
  investigate_move_on = type_input("How do you proceed?\nType 'investigate' to see what is up with the light. Type 'let it go' to move on with your life.\nR: ")

if investigate_move_on == "investigate": # INVESTIGATE
  type_input("\n---\nYou carefully move around the bushes to sneak closer to the light")
  type_input("You can now see a strange hole, what seems to be a cave")
  print(cave)
  cave_beach = type_input("What do you do?\nType 'cave' to go inside the cave. Type 'beach' to go back to the beach.\nR: ")
  
if cave_beach == "beach":
  type_input("\n---\nYou sure don't want to die inside a strange cave. You make your way back to the beach.")
  type_input("As you're getting closer to the sand, you feel a sharp pain on your back.")
  type_input("You look down and, all of the sudden, there's something pointy under your shirt.")
  type_input("You're bleeding. You're getting dizzy. Your vision fades to black.")
  type_input("You died and you'll never know why...")
  print(rip)
  type_input(try_again)
else:
  enemies = False
  resources_choice = False
  type_input("\n---\nYou decidedly went inside the cave. Nobody can stop your confidence!")
  type_input("As you walk, you notice the walls are too close to you and the corridor ahead is narrow.")
  type_input("You have to crouch and move slowly forward. 5 meters away from you there's a hole in the ground.")
  print(hole)
  hole = input("Type 'hole' to go inside the hole, as there's no other option now.\nR: ")
  
## ------------ ## ------------ ## ------------ ## ------------ ## ------------ ## ------------ ##    
                                 
if investigate_move_on == "let it go": # LET IT GO
  type_input("\n---\nYou don't care much for the light. It might as well be a weird looking bug")
  quiet_help = type_input("You stay still for a few minutes and hear steps to your right. What do you do?\nType 'quiet' to stay quiet. Type 'help' to call for help.\nR: ")

if quiet_help == 'help': # -> GAME OVER!
  print("\n---\nYou shout for help, but you hear no answer. The steps stop completely.")
  run_help = type_input("Silence is followed only by the sound of some bushes by the wind. What do you do?\nType 'run' to run. Type 'hello' to check if someone is out there\nR: ")
  if run_help == 'run':
    type_input("\n---\nYou start running as fear fills your heart and makes your body sweat.")
    type_input("Unfortunately, they were faster. You see arrows cutting the air beside you, until one of them cut your leg.")
    type_input("You're on the ground and trying to pull your body towards safety")
    type_input("Suddenly, darkness is all you see.")
    print(rip)
    type_input(try_again)
  else:
    type_input("\n---\nYou say hello, but there's no sign of movement or noise.")
    type_input("...\nR: ", delay=1)
    print(rip)
    type_input(try_again)
      
## Part 3 - The player enters a hole in the cave
# If the player kept quiet, they will meet the enemies inside the cave.
  # This path may lead to choosing one resource!
# If the player went inside the cave, they will continue safely.

# CONTINUE HERE!!
if quiet_help == 'quiet':
  enemies = True
  type_input("\n---\nYou stood quiet and the steps kept going. You notice they're going toward that light from before.")
  type_input("Maybe it wasn't a weird-looking bug afterall.")
  sneak_resources = type_input("What now?\nType 'sneak' to follow the steps quietly. Type 'resources' to look for something that might be useful.\nR: ")
if sneak_resources == 'sneak':
  type_input("\n---\nYou keep your distance and follow the steps.")
  type_input("They lead you to what seems to be a cave.")
  hole = cave_entry()
else:
  resources_choice = True
  type_input("\n---\nYou look around and find 3 items. You're bare-handed and there's no pockets on your clothes, so you'll have to choose one")
  type_input("You find a few stones, some berries and what seems to be... a key?!")
  resources = type_input("What do you choose?\nType 'stones', 'berries' or 'key'.\nR: ")
  if resources == 'stones':
    type_input("\n---\nYou grab 3 stones and take them with you.")
    type_input("You reach the light source and beside a torch on a wall you can see a cave")
    hole = cave_entry()
  elif resources == 'berries':
    type_input("\n---\nYou grab the berries and take them with you.")
    type_input("You reach the light source and beside a torch on a wall you can see a cave")
    hole = cave_entry()
  elif resources == 'key':
    type_input("\n---\nYou grab the key and take it with you.")
    type_input("You reach the light source and beside a torch on a wall you can see a cave")
    hole = cave_entry()      
  else:
    resources_choice = False
    type_input(f"\n---\nIf you were looking for {resources}, this was not one of the options and you didn't find it.")
    type_input("You move on with no resources whatsoever.")
    hole = cave_entry()

## Part 4 - The palyer explores the hole. They are left with two options, left or right.       

# ALREADY COPPIED EVERYTHING. COPY FROM MAIN.PY TO REPLIT            
if hole == 'hole':
  print(ladder)
  type_input("\n---\nGoing down the ladder after a few seconds, you look up.") 
  type_input("The hole is now a little white dot, meters higher than you.")
  if enemies == False:
    type_input("Finally you reach the ground.")
  else:
    type_input("You look down to place your feet carefully on the ground. You don't want to make unnecessary noise.")
  type_input("You turn arround to face the path ahead and it's a forked road.")
  type_input("To your left, you see paintings on the wall, and you notice the ground is beat, as if there have been many walks on it")
  type_input("To your right, ...")
  left_right = input("How do you proceed?\nType 'left' or 'right'.\nR: ")
  

if left_right == 'left' and enemies == False:  
  left_segment()
  type_input("You try to open it, but you have no luck in doing so. It's locked.")
  if resources == 'key':
    type_input(f"You then remember you have the {resources} with you.")
    type_input(f"You use your {resources} to open the door and you're now in a room full of shelves.")
    type_input("On the shelves you have lots of books. Right there, in the middle of the room, there's a cauldron.")
    print(cauldron)
    type_input("Inside the cauldron, though, there's nothing but a metal ladle")
    shelves_go_back = type_input("What do you want to do now?\nType 'shelves' to investigate the shelves or 'go back' come back from where you came.\nR: ")
    if shelves_go_back == 'shelves':
      type_input("You take a good look at those bookshelves. That's what you find.")
      print(bookshelf)
      type_input("The book reads 'TAKE THE LADLE AND GET OUT OF THE HOLE. RIGHT'. It seems like a clue.")
      take_ladle = type_input("Do you want to take the ladle?\nType 'yes' to take it or 'no' to leave it.\nR: ")
      if take_ladle == 'yes':
        type_input("As soon as you put your hand on the object inside the cauldron, everything turns black!")
        type_input("You wake up and you are at your house.")
        type_input("...\nR: ", delay=1)
        type_input("CONGRATULATIONS!!!")
        print(firework)
        type_input("The treasure you found this time was the 'Housing Treasure'. That's 1 out of 3!")
        type_input(win_try_again)
    if shelves_go_back == 'go back' or take_ladle == 'no':
      if take_ladle == 'no':
        type_input("You show no interest for the ladle.")
      type_input("As you leave the room to explore the rest of the cave, you hear steps ahead.")
      type_input("They're getting closer! What do you do?")
      go_back_chill = type_input("Type 'go back' to go back to the room and try to hide or 'chill' to stay where you are since, whoever it is, they may end up being of help.\nR: ")
      if go_back_chill == 'go back':
        type_input("Your heart is beating faster than ever. Your body senses danger!")
        type_input("You try to go back to the room desperately, but there's no stopping them.")
        type_input("You feel their eyes looking at your failed attempt to get inside the room again, at the way you trip on your own feet.")
        type_input("An arrow hits the cauldron and shatters beneath you.")
        type_input("A spear is now stuck in the ground to your left.")
        type_input("You turn around to try and see what's coming, but...")
        type_input("A very sharp pain starts spreading through your whole upperbody from your right shoulder.")
        type_input("You see shadows coming to you. The pain is now coming right from the middle of your chest.")
        type_input("Your vision fades to black")
        print(rip)
        type_input(try_again)
      else:
        type_input("'Finally, human beings!' You think to yourself as you patiently wait for the steps to get closer")
        type_input("You take a good look at the people making the final turn at the end of the visible tunnel. Now they're facing you.")
        type_input("You wave your hand and they stop. Every single one of them with either a spear or a bow in their hand.")
        type_input("They turn to each other and start talking, but you're too far to listen to anything.")
        type_input("They have their weapons ready to attack.")
        type_input("It took no more than 1 arrow to your head to finish this nightmare.")
        print(rip)
        type_input(try_again)      
  else:
    type_input(f"You then remember you could have brought a key with you, but instead you chose {resources}.")
    shelves_go_back = type_input("Type 'go back' to go back as there's no other option.\nR: ")
    type_input("As you turn around to explore the rest of the cave, you hear steps ahead.")
    type_input("They're getting closer! What do you do?")
    break_chill = type_input("Type 'break' to break open the door to the room and try to hide or 'chill' to stay where you are since, whoever it is, they may end up being of help.\nR: ")
    if break_chill == 'break':
      type_input("Your heart is beating faster than ever. Your body senses danger!")
      type_input("You try to go break the damn door desperately, but there's no stopping them.")
      type_input("You feel their eyes looking at your failed attempt to get inside the room, at the way punch and kick the door without really knowing what you're doing.")
      type_input("An arrow hits the door handle and shatters beneath you.")
      type_input("A spear is now stuck in the wall to your left.")
      type_input("You turn around to try and see what's coming, but...")
      type_input("A very sharp pain starts spreading through your whole upperbody from your right shoulder.")
      type_input("You see shadows coming to you. The pain is now coming right from the middle of your chest.")
      type_input("Your vision fades to black")
      print(rip)
      type_input(try_again)
    else:
      type_input("'Finally, human beings!' You think to yourself as you patiently wait for the steps to get closer")
      type_input("You take a good look at the people making the final turn at the end of the visible tunnel. Now they're facing you.")
      type_input("You wave your hand and they stop. Every single one of them with either a spear or a bow in their hand.")
      type_input("They turn to each other and start talking, but you're too far to listen to anything.")
      type_input("They have their weapons ready to attack.")
      type_input("It took no more than 1 arrow to your head to finish this nightmare.")
      print(rip)
      type_input(try_again)
      
elif left_right == 'left' and enemies == True:
  left_segment()
  type_input("You can now listen to noises on the other side of the door.")
  go_back_get_closer = type_input("What do you do?\nType 'go back' to get away from there or type 'get closer' to get a better hear of what's going on.\nR: ")
  
    
  
  
  

  
      