inventory = []

import os
import time
import random
import sys
import shutil

CritChanceBonus = 0
CounterDamage = 0
DodgeBuff = 0
base_attack = 0
attack_damage = base_attack
MageShieldChanceTrinket = 0
MageShieldHealthTrinket = 0
BonusTank = 0
ThornsDamage = 0
StrafeItem = 0


#os.system('mode con:cols=170 lines=40')
os.system('cls')
os.system('color 0f')



#Prints out string letter by letter. Also makes sure words are not cut off
def print_slow(text):
  # Get terminal size
  columns, rows = shutil.get_terminal_size()

  # Split the text into words
  words = text.split(" ")
  current_line = ""

  for word in words:
    # If adding the next word exceeds the terminal width, print the current line and start a new one
    if len(current_line) + len(word) + 1 > columns:
      # Print current line and move to the next line
      for letter in current_line:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.050)
      sys.stdout.write("\n")
      current_line = word  # Start a new line with the current word
    else:
      # Add the word to the current line
      if current_line:
        current_line += " " + word
      else:
        current_line = word

  # Print the last line
  if current_line:
    for letter in current_line:
      sys.stdout.write(letter)
      sys.stdout.flush()
      time.sleep(0.050)
    sys.stdout.write("\n")

#Puts text in true center
def center_text(text):
  # Get terminal size
  columns, rows = shutil.get_terminal_size()

  # Calculate center position
  text_lines = text.split("\n")
  max_line_length = max(len(line) for line in text_lines)
    
  start_row = (rows - len(text_lines)) // 2
  start_col = (columns - max_line_length) // 2

  # Print empty lines to center vertically
  print("\n" * start_row, end="")

  # Print text centered horizontally
  for line in text_lines:
        print(" " * start_col + line)

def printSlowCentered(text):
  columns, _ = shutil.get_terminal_size()
  start_col = (columns - len(text)) // 2
  print(" " * start_col, end="")  # Add spaces before the slow print
  print_slow(text)

def printSlowTrueCentered(text):
  # Get terminal size
  columns, rows = shutil.get_terminal_size()

  # Split text into multiple lines (handles multi-line text correctly)
  text_lines = text.split("\n")
    
  # Calculate vertical centering
  start_row = (rows - len(text_lines)) // 2

  # Print empty lines to push text downward for vertical centering
  print("\n" * start_row, end="")

  # Print each line centered horizontally
  for line in text_lines:
    start_col = (columns - len(line)) // 2
    print(" " * start_col, end="")  # Add spaces before slow print
    print_slow(line)  # Slow print the line
    print()  # Move to the next line

def scroll():
  count=20
  for i in range(0,20,1):
   print('\n')
   time.sleep(.10)



def credits():
  os.system('color 0a')
  time.sleep(.20)
  os.system('color 8a')
  time.sleep(.20)
  os.system('color 7a')
  time.sleep(.20)
  os.system('color fa')
  time.sleep(.5)
  riskyLogo = '''

     ▄████████  ▄█     ▄████████    ▄█   ▄█▄ ▄██   ▄           ▄████████     ███     ███    █▄  ████████▄   ▄█   ▄██████▄     ▄████████ 
    ███    ███ ███    ███    ███   ███ ▄███▀ ███   ██▄        ███    ███ ▀█████████▄ ███    ███ ███   ▀███ ███  ███    ███   ███    ███ 
    ███    ███ ███▌   ███    █▀    ███▐██▀   ███▄▄▄███        ███    █▀     ▀███▀▀██ ███    ███ ███    ███ ███▌ ███    ███   ███    █▀  
   ▄███▄▄▄▄██▀ ███▌   ███         ▄█████▀    ▀▀▀▀▀▀███        ███            ███   ▀ ███    ███ ███    ███ ███▌ ███    ███   ███        
   ▀▀███▀▀▀▀▀   ███▌ ▀███████████ ▀▀█████▄    ▄██   ███      ▀███████████     ███     ███    ███ ███    ███ ███▌ ███    ███ ▀███████████ 
   ▀███████████ ███           ███   ███▐██▄   ███   ███               ███     ███     ███    ███ ███    ███ ███  ███    ███          ███ 
     ███    ███ ███     ▄█    ███   ███ ▀███▄ ███   ███         ▄█    ███     ███     ███    ███ ███   ▄███ ███  ███    ███    ▄█    ███ 
     ███    ███ █▀    ▄████████▀    ███   ▀█▀  ▀█████▀        ▄████████▀     ▄████▀   ████████▀  ████████▀  █▀    ▀██████▀   ▄████████▀  
     ███    ███                     ▀                                                                                                    
      '''
  center_text(riskyLogo)

  time.sleep(.65)
  scroll()

  os.system('cls')
  time.sleep(.2)
  os.system('color 7e')
  time.sleep(.2)
  os.system('color 8e')
  time.sleep(.2)
  os.system('color 0e')
  time.sleep(.35)

  riseLogo = '''
██████╗ ██╗███████╗███████╗    ████████╗ ██████╗     ██╗   ██╗ █████╗ ██╗     ██╗  ██╗ █████╗ ██╗     ██╗      █████╗ 
██╔══██╗██║██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗    ██║   ██║██╔══██╗██║     ██║  ██║██╔══██╗██║     ██║     ██╔══██╗
██████╔╝██║███████╗█████╗         ██║   ██║   ██║    ██║   ██║███████║██║     ███████║███████║██║     ██║     ███████║
██╔══██╗██║╚════██║██╔══╝         ██║   ██║   ██║    ╚██╗ ██╔╝██╔══██║██║     ██╔══██║██╔══██║██║     ██║     ██╔══██║
██║  ██║██║███████║███████╗       ██║   ╚██████╔╝     ╚████╔╝ ██║  ██║███████╗██║  ██║██║  ██║███████╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝       ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
'''
  center_text(riseLogo)
  print("\n" * 10, end="")


  printSlowCentered('Press Enter To Begin')
  input('')
  
  scroll()

  os.system('cls')
  time.sleep(.01)
  printSlowTrueCentered('Play At Your Own Risk!')
  time.sleep(1.75)
  os.system('cls')
  time.sleep(1)


def intro_talk():
  global player_name
  printSlowTrueCentered('*All Answers Are Character Sensitive And An Empty Response Is NOT An Acceptable Response!*\n\n\nFeel Free To Let Us Know About Any Bugs Or Ideas For How To Improve Our Game!')
  time.sleep(2)
  os.system('color f')
  os.system('cls')
  time.sleep(.75)


def askSave_name():
    global player_name
    print_slow('\nDo you want to save?')
    ask = input(f'\n{player_name}: ').upper()
    if ask == "Y" or ask == "YES":
        name_save = (player_name) 
        thefile = open("Rise_variable_file.txt", "w")
        thefile.write(name_save)
        thefile.close()
    elif ask == "N" or ask == "NO":
        print('You might regret that but you are the player!')
        return
    else:
        time.sleep(1)
        os.system('color 4')
        print('That was not an option')
        time.sleep(1)
        os.system('color f')
        askSave_name()


def askSave_class():
    global class_thing
    global player_name
    print_slow('\n\nDo you want to save?')
    ask = input(f'\n{player_name}: ').upper()
    if ask == "Y" or ask == "YES":
        class_save = (class_thing) 
        thefile = open("Rise_variable_file.txt", "a")
        thefile.write(f'\n{class_save}: ')
        thefile.close()
    elif ask == "N" or ask == "NO":
        print('You might regret that but you are the player!')
        return
    else:
        time.sleep(1)
        os.system('color 4')
        print('That was not an option')
        time.sleep(1)
        os.system('color f')
        askSave_class()



def story_line():
  print_slow('\nOnce in time, The Nine Realms lived and worked harmoniously together, but that changed when the bottom realms revolted sending all 9 realms into chaos. Only one realm could save them, Asgard. The heavenly realm and home to some of the strongest warriors including Odin. Odin and the Valkyrie were able to stop the fighting but they were still no where close to peace. Due to Odins involvement in the war, he was less then liked by the lower realms, but at least there were no plans for war, thats what they thought....   ')
  time.sleep(5)
  print_slow('....\nThe beast is getting closer to you, the moment you look back to take a peek at the beast you run into a tree, you find just enough strength to turn over and see the beast pounce directly towards you. Your instinct kicks in to cover your face and... You snap to reality. It was just a dream. The first thing you see is a beer in hand. Theres a local asgardian band playing in the background and you start to remember that you were partying late the night before. While deep in thought a raven comes and lands on the bar in front of you. It caws, and it sounded like it almost said follow me. Your mind wanted to ignore it, but your instincts pulled you towards listening to what you thought you heard. It leads you all the way to Odins Castle to meet with the man himself. ')
  time.sleep(5)       
  
      


def players_name():
  global player_name
  print_slow('\nOdin: What Is Your Name Being?')
  player_name = input('\n> ').upper()
  while player_name == '':  
    print_slow(f'\nOdin: That is UNACCEPTABLE!  I Require A Name!')
    player_name = input('\n>').upper()
  time.sleep(1)
  print_slow(f'\nOdin: Is {player_name} the name by which you would liked to be called? Y/N')
  player_name_choice = input('\n>').upper()
  while player_name_choice != '':
    if player_name_choice == 'Y':
      time.sleep(1)
      print_slow(f'\nOdin: AHHH yes that is what it was! Welcome to the Valkaryie {player_name}!')
      time.sleep(2)
      break
    if player_name_choice == 'N':
      time.sleep(1)
      print_slow("\nOdin: Then why in Helheim did you tell me that name?! Lets Try Again!")
      time.sleep(1)
      players_name()
      break
    else:
      time.sleep(1)
      os.system('color 4')
      print_slow("\nOdin: That wasn't even an option that I gave you! Try Again!")
      time.sleep(1)
      os.system('color f')
      players_name()  
      break





def class_select():
  global class_health
  global class_thing
  global player_name
  os.system('color f')
  print_slow('\nOdin: What Class Were You Again? Archer, Mage, Warrior, or Thief:')
  class_thing = input(f'\n{player_name}: ').upper()
  while class_thing != ' ':
    if class_thing == 'ARCHER':
      time.sleep(1)
      class_health = 20
      attack_damage = 10
      print_slow('\nArcher, The Marksman, Has The Ability To Precision Hit, Known To Kill Anyone They Lay Their Eyes On')
      break
    elif class_thing ==  'MAGE':
      time.sleep(1)
      class_health = 40
      print_slow('\nMage, The Scholar, Has The Ability To Heal Themselves Temporarily, Their Knowledge Is Their Power')
      break
    elif class_thing == 'WARRIOR':
      time.sleep(1)
      class_health = 60
      print_slow('\nWarrior, The Fighter, Has The Ability To Block, Never In History Have They Backed Down')
      break
    elif class_thing == 'THIEF':
      time.sleep(1)
      class_health = 0
      print_slow('\nThief, The Bandit, Has A Higher Chance To Dodge And Counter-Attacks On Dodge, Watch Yourself They Like Shiny Things')
      break
    else:
      time.sleep(1)
      os.system('color 4')
      print_slow('\nThat Class Does Not Exist Here, Please Try Again')
      time.sleep(1)
      os.system('color f')
      class_thing = input('\nOdin: What Class Were You Again? Archer, Mage, Warrior, or Thief:\n>').upper()
      continue
     
  
      


def big_choice():
  global player_name
  global class_thing
  time.sleep(1)
  print_slow(f'\nOdin: Are You Sure {class_thing} Is What You Were?, Y/N?')
  choice = input(f'\n{player_name}: ').upper()
  while choice != ' ':
    if choice == 'Y':
      time.sleep(1)
      print_slow(f'\nOdin: Okay Then {player_name} I need your help!')
      time.sleep(2)
      break
    elif choice == 'N':
      print_slow('\nWell Darn I Guess Lets Go Through This Again')
      time.sleep(1)
      class_select()
      time.sleep(1)
      health()
      player_attack(0)
      big_choice()
      break
    else:
      time.sleep(1)
      os.system('color 4')
      print_slow(f'\nOdin: What in the H E double hockey sticks does that even mean {player_name}... Please Try Again!')
      time.sleep(1)
      os.system('color f')
      big_choice()
      break
          




def health():
  global player_health

  player_health = 90 + class_health
  time.sleep(1)
  print_slow(f'\nYour Starting health Is {player_health}')
          




def heal():
  global player_name
  global player_health
  global class_health
  print_slow('\nYou arrive at a heal totem would you like to use it? Y/N')
  healing = input(f'\n{player_name}: ').upper()
  while healing != '':
    if healing == 'Y':
      player_health = 90 + class_health
      print_slow(f'\nHealing Successful, You are now back up to {player_health} HP')
      break
    if healing == 'N':
      print_slow('\nHealing Denied, Continue on')
      break
    else:
      time.sleep(1)
      os.system('color 4')
      print_slow('\nThat is not an option try again')
      time.sleep(1)
      os.system('color f')
      heal()
      break






def player_attack(x):
  global attack_damage
  global weapon_damage
  if class_thing == 'ARCHER':
    attack_damage = (50 + x)
  else:
    if class_thing == 'MAGE':
      attack_damage = (45 + x)
    else:
      if class_thing == 'THIEF':
        attack_damage = (65 + x)
      else:
        if class_thing == 'WARRIOR':
          attack_damage = (45 + x)
                  
  
  
      

def giants_dialogue():
  global player_name
  print_slow('\nOdin: Loki has been running rampant around the realms and I have finally snapped. I need you to to travel to Jotunheim to take him out. The adventure may be rough, but I think you are the person for this job. If you agree I can provide more information.')
  time.sleep(3)
  print_slow('\nOdin: So would you like to take on this task? Y/N?')
  giants_dialogue_choice = input(f'\n{player_name}: ').upper()
  while giants_dialogue_choice != ' ':
    if giants_dialogue_choice == 'Y':
      time.sleep(1)
      print_slow('\nOdin: Fantastic! Heres the plan')
      time.sleep(1)
      break
    elif giants_dialogue_choice == 'N':
      time.sleep(1)
      print_slow('\nOdin: YOU SON OF A *****! You better rethink that decision or you are a coward and I will lose my ****!')
      time.sleep(1)
      giants_dialogue()
      break
    else:
      time.sleep(1)
      os.system('color 4')
      print_slow('\nOdin: Mind telling me what the meaning is of what you just said?? Just retry that!')
      time.sleep(1)
      os.system('color f')
      giants_dialogue()
      break





def the_plan():
    global player_name
    print_slow('\nOdin: I must request that you take out Cayde the Frost Giant, Freyja, Fenrir and then Loki.')
    time.sleep(2)
    print_slow('\nOdin: Are you still sure you are ready for this? Y/N')
    biggest_choice = input(f'\n{player_name}: ').upper()
    time.sleep(1)
    while biggest_choice != '':
        if biggest_choice == 'Y':
            print_slow('\nOdin: FIGHT FOREVER GUARDIAN!!!')
            break
        elif biggest_choice == 'N':
            print_slow('\nOdin: YOU ARE A COMPLETE AND UTTER COWARD! Try that again or be banished from this realm!')  
            the_plan()
            break
        else:
            time.sleep(1)
            os.system('color 4')
            print_slow('Odin: What in Squirenation does that mean?! Try again!')
            time.sleep(1)
            os.system('color f')
            the_plan()
            break





def  giants_dialogue2():
  print_slow('\nAfter listening to Odin you leave the castle to set out on your quest.As you are walking you notice up ahead there is a cliff face that will not be scaleable making it a dead end, but just to the right of it theres a cave entrance.')
  time.sleep(2.75)
  print_slow('\nYou Can Either Can Continue Into The Cave Quit and Give Up The Journey')
  time.sleep(.5)
  print_slow('\nC/Q?')
  cave_decision = input(f'\n{player_name}: ').upper()
  while cave_decision != ' ':
    if cave_decision == 'Q':
      time.sleep(1)
      print_slow('*Odin Echos Lowdly* Odin: YOU COWARD HOW DARE YOU, YOU BETTER RETHINK' )
      giants_dialogue2()
      break
    elif cave_decision == 'C':
      time.sleep(1)
      print_slow('\nYou continue into the cave entrance')
      time.sleep(1)
      print_slow('\nYou hear a strange noise then a loud Growl')      
      break
    else:
      os.system('color 4')
      print_slow('\nThat was not an option! Please Try Again')
      time.sleep(1)
      os.system('color f')
      giants_dialogue2()
      break
      

      
    
    
def cayde_dialogue():
  global player_name
  global class_thing
  print_slow('\nYou look around to find the source of the sound. You look towards the cave entrance thinking that it could be a escape route if necessary. Thats when a loud crash echoes throughout the cave, so loud your ear rings from it. You whip around to see Cayde staring straight at you with a demonic look in his eyes')
  print_slow(f'\nCayde: You dumb {class_thing}! You want to come to my home territory and try to take me out?! You and Odin are more moronic than I imagined! Let us imagine for one second that you defeat me, Freyja will obliterate you back to another eon! Buuuttt.. we will not even get to that point because I will eliminate you right here right now! RAGHHHHHHHHHH')





def mini_boss_giant():
    global boss_attack
    global player_attack
    global player_name
    global player_health
    global fight_health
    global boss_health
    boss_health = 200
    turn = 'Player'
    boss_attack = 35
    print_slow('\nCAYDE CHARGES AT YOU!')
    time.sleep(1)
    print_slow('\nFight or Flee?')
    move1 = input(f'\n{player_name}: ').upper()
    time.sleep(1)
    if move1 == 'FIGHT':
      while boss_health > 0 or player_health > 0:
        if turn == 'Player':
          if class_thing == 'ARCHER':
            ArcherCrit()
            turn = 'Boss'

          else:

            boss_health = boss_health - attack_damage
            print_slow('\n\nYou Attacked!')
            time.sleep(1)
            print_slow(f"\nThe Giant's health is {boss_health}")
            time.sleep(1)
            turn = 'Boss'
        else:
          if turn == 'Boss':
            if class_thing == 'THIEF':
              ThiefDodge()
              turn = 'Player'
            if class_thing == 'MAGE':
              MageShield()
              turn = 'Player'
              
            if class_thing == "ARCHER":
              ArcherStrafe()
              turn = "Player"
            if class_thing == 'WARRIOR':
              WarriorArmor()
              turn = 'Player'
              

        if boss_health <= 0:
          print_slow(f'\n\nYou Won')
          if class_thing == 'WARRIOR':
            RandomItem = random.randint(0,100)
            if RandomItem > 50:
              print_slow('\nWould you like to pickup this basic tank item? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                BonusTankBasicItem()
              else:
                print_slow('\nYou leave the item on the ground')
            else:
              print_slow('\n\nWould you like a basic thorns item? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == "Y":
                ThornsBasicItem()
              else:
                print_slow('\nYou leave the item on the ground')
          elif class_thing == "THIEF":
            RandomItem = random.randint(0,100)
            if RandomItem > 50:
              print_slow('\n\nWould you like to pick up this basic dodge item? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                BasicDodgeItems()
              else:
                print_slow('\nYou leave this item on the ground')
            else:
              print_slow("\n\nDo you want this basic counter item? Y/N")
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                BasicCounterBuff()
              else:
                print_slow('\nYou leave this item on the ground')
          elif class_thing == 'MAGE':
            RandomItem = random.randint(0,100)
            if RandomItem > 50:
              print_slow('\n\nDo you want a basic shield health item? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                MageBasicHealthItem()
              else:
                print_slow('\nYou dropped this item on the ground')
            else:
              print_slow('\n\nDo you want a basic shield chance item? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                MageBasicChanceItem()
              else:
                print_slow('\nYou dropped this item on the ground')
          else:
            RandomITem = random.randint(0,100)
            if RandomITem > 50:
              print_slow('\n\nYou find a basic crit item would you like to pick it up? y/n')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                BasicArcherCrit()
              else:
                print_slow('\nYou dropped the item')
            else:
              print_slow('\n\nYou find a basic strafe item on the ground would you like to pick it up? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'Y':
                BasicStrafeItem()
              else:
                print_slow('\nYou dropped the item on the ground ')

            
              
          break
        if player_health < 0:
          print_slow(f'\nYou Lost, The Giant Survived With {boss_health} Health Left') 
          break





def post_cayde_dialogue():
  global player_health
  global player_name
  global class_thing
  print_slow('\nThe cave turned out to be very short, having an exit not even half a mile passed the lifeless body of Cayde.You exit the cave as lightning strikes in front of you.The dust settles and Odin is kneeling in a godly stance. Odin stands up and looks at you in a very proud manner')
  print_slow('\nOdin: Looks like I picked the right person for the job. Cayde was a nuisance and I am glad he is one less person I have to worry about')
  if player_health > 45: 
    print_slow(f'\n{player_name}: It was an easy fight! Training was harder than Cayde!')
  if player_health < 45:
    print_slow(f'\n{player_name}: It was a close fight, but I knew I was going to win the whole time!')  
  print_slow(f'\nOdin: Unfortunately {class_thing} this is just the start. I need you to go to the World Tree and fight Freyja. Loki corrupted her mind and tricked her into thinking that he is the good guy. The thing is though if you just attack her stinky pp until she is on the verge of death she will snap out of it.')
  print_slow(f'\nOdin: Now get out there {class_thing} and continue the fight to better the 9 realms!')





def freyja_dialogue():
  global player_name
  global class_thing
  time.sleep(1)
  print_slow('\nIt takes several hours, but you finally reach the world tree. Its beauty is unmeasurable. It has more colors than on a rainbow, with leaves and branches sprouting everywhere. There are so many different species that its almost impossible to count.\nYou start to look around the tree to see where to start climbing. That is when you see Freyja standing on a branch only around 250 feet up. It looks like she is about to execute a Dwarf. ')
  print_slow(f'\n{player_name}: Stop! Do not lay a hand on that dwarf you foul woman')
  print_slow('\nYou grab onto a foot a flying beast and jump off onto the same branch as Freyja.')
  print_slow(f'\nFreyja: Ah yes, you are this new upcoming {class_thing} I have heard so little about...Ha! Have you come here to *does hand air quotes* fix me? Not going to happen pesky {class_thing}')
  print_slow(f'\n{player_name}: That is where you are wrong you wretch of god! I am not ordinary {class_thing}! I am {player_name} and I did not come to lose')
  print_slow('\nYou charge at Freyja with your weapon ready')


def Freyja():
    global boss_attack
    global player_name
    global player_health
    global player_attack
    global fight_health
    global boss_health
    global StrafeItem
    boss_health = 250
    turn = 'Player'
    boss_attack = 50
    print_slow('\nThe Goddess Freyja appears!')
    time.sleep(1)
    print_slow('\nFight or Flee?')
    move1 = input(f'\n{player_name}: ').upper()
    time.sleep(1)
    if move1 == 'FIGHT':
      while boss_health > 0 or player_health > 0:
        if turn == 'Player':
          if class_thing == 'ARCHER':
            ArcherCrit()
            turn = 'Boss'

          else:

            boss_health = boss_health - attack_damage
            print_slow('\n\nYou Attacked!')
            time.sleep(1)
            print_slow(f"\nThe Goddess's health is {boss_health}")
            time.sleep(1)
            turn = 'Boss'
        else:
          if turn == 'Boss':
            if class_thing == 'THIEF':
              ThiefDodge()
              turn = 'Player'
            if class_thing == 'MAGE':
              MageShield()
              turn = 'Player'
              
            if class_thing == "ARCHER":
              ArcherStrafe()
              turn = "Player"
            if class_thing == 'WARRIOR':
              WarriorArmor()
              turn = 'Player'
              

        if boss_health <= 0:
          print_slow(f'\n\nYou Won')
          if class_thing == 'WARRIOR':
            RandomItem = random.randint(0,100)
            if RandomItem > 50:
              print_slow('\nWould you like to pickup this basic tank item? Y/N')
              Pickup = input(f'\n{player_name}: ')
              if Pickup == 'y':
                BonusTankBasicItem()
              else:
                print_slow('\nYou leave the item on the ground')
            else:
              print_slow('\n\nWould you like a basic thorns item? Y/N')
              Pickup = input(f'\n{player_name}: ')
              if Pickup == "y":
                ThornsBasicItem()
              else:
                print_slow('\nYou leave the item on the ground')
          elif class_thing == "THIEF":
            RandomItem = random.randint(0,100)
            if RandomItem > 50:
              print_slow('\n\nWould you like to pick up this basic dodge item? Y/N')
              Pickup = input(f'\n{player_name}: ')
              if Pickup == 'y':
                BasicDodgeItems()
              else:
                print_slow('\nYou leave this item on the ground')
            else:
              print_slow("\n\nDo you want this basic counter item? Y/N")
              Pickup = input(f'\n{player_name}: ')
              if Pickup == 'y':
                BasicCounterBuff()
              else:
                print_slow('\nYou leave this item on the ground')
          elif class_thing == 'MAGE':
            RandomItem = random.randint(0,100)
            if RandomItem > 50:
              print_slow('\n\nDo you want a basic shield health item? Y/N')
              Pickup = input(f'\n{player_name}: ')
              if Pickup == 'y':
                MageBasicHealthItem()
              else:
                print_slow('\nYou dropped this item on the ground')
            else:
              print_slow('\n\nDo you want a basic shield chance item? Y/N')
              Pickup = input(f'\n{player_name}: ')
              if Pickup == 'y':
                MageBasicChanceItem()
              else:
                print_slow('\nYou dropped this item on the ground')
          else:
            RandomITem = random.randint(0,100)
            if RandomITem > 50:
              print_slow('\n\nYou find a basic crit item would you like to pick it up? y/n')
              Pickup = input(f'\n{player_name}: ')
              if Pickup == 'y':
                BasicArcherCrit()
              else:
                print_slow('\nYou dropped the item')
            else:
              print_slow('\n\nYou find a basic strafe item on the ground would you like to pick it up? Y/N')
              Pickup = input(f'\n{player_name}: ').upper()
              if Pickup == 'y':
                BasicStrafeItem()
              else:
                print_slow('\nYou dropped the item on the ground ')

            
              
          break
        if player_health < 0:
          print_slow(f'\nYou Lost, Freyja Survived With {boss_health} Health Left') 
          break
            
    elif move1 == 'Flee':
        FleeChance = random.randint(0,100)
        if FleeChance > 50:
          print_slow('\nYou Escaped')
    else:
      os.system('color 4')
      print_slow('\nThats Not An Option Try Again')
      time.sleep(1)
      os.system('color f')
      

    
    

def post_freyja_dialogue():
  input('')




def BasicItem():
  if class_thing == 'ARCHER':
    time.sleep(1)
    print_slow('You Have Found A Basic Longbow Lying Right Behind The Giant!')
    player_attack(10)
    print_slow(attack_damage)
  elif class_thing == "WARRIOR":
    time.sleep(1)
    print_slow('You Have Found A Rusted Blade From A Skeleton Right Beside The Giant')
    player_attack(10)
  elif class_thing == 'MAGE':
    time.sleep(1)
    print_slow('You Found A Oak Staff From A Skeleton Right Beside The Giant')
    player_attack(10)
  else:
    time.sleep(1)
    print_slow('You Have Found A Iron Dagger From The Giants Pocket')
    player_attack(10)





def MageShield():
  global boss_attack
  global player_health
  global MageShieldHealthTrinket
  global MageShieldChanceTrinket
  global fight_health
  
  
  ShieldHealth = (random.randint(30,75) + MageShieldHealthTrinket)
  ShieldChance = random.randint(0,100)
  if ShieldChance > (70 - MageShieldChanceTrinket):
    if ShieldHealth > boss_attack:
      print_slow('\nYou throw up a shield!')
                  
      fight_health = player_health + (ShieldHealth - boss_attack)
      player_health = fight_health
      print_slow(f"Your new health is {fight_health}")
      turn = 'Player'
      time.sleep(1)
    else:
      fight_health = player_health - (ShieldHealth - boss_attack)
      player_health = fight_health
      print_slow(fight_health)
      time.sleep(1)
      turn = 'Player'
  else:
    fight_health = player_health - boss_attack
    player_health = fight_health
    print_slow("\nYou have been hit!")
    time.sleep(1)
    print_slow(f"Your health is {player_health}!")
    turn = 'Player'





def WarriorArmor():
  global BonusTank
  global player_health
  global boss_health
  global fight_health
  fight_health = player_health - (boss_attack*(.5 - BonusTank))
  boss_health = (boss_attack*(.45 - BonusTank)*ThornsDamage)
  print_slow('\nYou tanked a hit!')
  time.sleep(1)
  print_slow(f'Your new health is {fight_health}')
  player_health = fight_health
  time.sleep(1)
  turn = 'Player'
  '''
  # to make more tanky set BonusTank to a decimal currently only taking half damage base the number will increase your tank
  # to buff thorns damage any number between 0-1 will do partial damage back any number <1 will reflect more damage 
  '''
  




def ThiefDodge():
  global player_health
  global fight_health
  global boss_attack
  global CounterDamage
  global boss_health
  DodgeChance = random.randint(0,100) 
  if DodgeChance > (60 - DodgeBuff):
    counterAttack = (10 + CounterDamage)
    boss_health = boss_health - counterAttack
    print_slow('\n\nThe Monster Attacked But You Counter Attacked!!')
    time.sleep(1)
    print_slow(f"\nThe Monster health is {boss_health}")
    turn = 'Player'
    time.sleep(1)
  else:
    fight_health = player_health - boss_attack
    print_slow('\n\nThe Monster Attacked')
    time.sleep(1)
    print_slow(f"\nYour Health is {fight_health}")
    player_health = fight_health

    turn = 'Player'
    time.sleep(1)





def ArcherCrit():
  global boss_health
  global CritChanceBonus
  CritChance = random.randint(0,100)
  CritBonus = random.randint(0,30)
  if CritChance > (75 - CritChanceBonus):
    boss_health = boss_health - (attack_damage*2.5 + CritBonus)
    print_slow('\n\nYou hit a vital!!')
    time.sleep(1)
    print_slow(f"\nThe monsters health is {boss_health}")
    time.sleep(1)
    turn = 'Boss'
  else:
    boss_health = boss_health - attack_damage
    print_slow('\n\nYou Attacked!')
    time.sleep(1)
    print_slow(f"\nThe Monster health is {boss_health}")
    turn = 'Boss'
              
def ArcherStrafe():
    global player_health
    global StrafeItem
    StrafeChance = random.randint(0,100)
    if StrafeChance > (99 - StrafeItem):
      print_slow('\nYOU STRAFED!!!!!')
      time.sleep(1)
      turn = 'Player'
    else:
      fight_health = player_health - boss_attack
      player_health = fight_health
      print_slow("\n\nYou have been hit!")
      time.sleep(1)
      print_slow(f"\nYour health is {player_health}")
      time.sleep(1)

def BasicStrafeItem():
  global StrafeItem
  print_slow('\nyou find a cloak that allows you to blend into the background')
  StrafeItem = 100

def BasicArcherCrit():
  global CritChanceItem
  print_slow('\nYou find a scope for your bow that improves your accuracy')
  CritChanceBonus = 10





def BasicCounterBuff():
  global CounterDamage
  print_slow('\nYou find a book listing weaknesses of people and your counter damage is buffed')
  CounterDamage = 10

def BasicDodgeItems():
  print_slow('\nYou found a lucky rabbits foot')
  DodgeBuff = 10





def BonusTankBasicItem():
  print_slow('\nYou found a sturdy chest piece')
  BonusTank = .1

def ThornsBasicItem():
  print_slow('\nYou found a mail shirt glowing with power that decreases your armor but deals thorns damage')
  ThornsDamage = .5
  BonusTank = -.1





def MageBasicHealthItem():
  print_slow('\nYou found a old amulet that empowers your shield')
  MageShieldHealthTrinket = 30
  MageShieldChanceTrinket = -5

def MageBasicChanceItem():
  print_slow('\nYou found a amulet humming with power to emprove you shield chance')
  MageShieldChanceTrinket = 10
  MageShieldHealthTrinket = -20

  print_slow('\nYou found a amulet humming with power to emprove you shield chance')
  MageShieldChanceTrinket = 10
  MageShieldHealthTrinket = -20


def HellfireBow():
  print_slow('\nYou find a bow made of bones radiating with demonic power')
  CritBonus = 10
  CritChanceBonus = 75
  player_attack(100)

def LostBane():
  print_slow('\n You find the legendary Lost Bane with the power of full counter')
  BonusTank = .30
  ThornsDamage = 4
  
def AmuletOfAbsoluteProtection():
  print_slow('\nYou find a legendary amulet lost to time that generates impenatrable shields')
  MageShieldHealthTrinket = 1000
  MageShieldChanceTrinket = 50



credits()
intro_talk()
story_line() 
players_name()
 
class_select()

health() 
player_attack(0)
big_choice() 
giants_dialogue()
giants_dialogue2()
cayde_dialogue()
mini_boss_giant()
heal()
post_cayde_dialogue() 
freyja_dialogue()
Freyja()
