import random
#The random word list for the hangman game
word_list = ['abruptly','absurd','abyss','affix', 'askew', 'avenue', 
'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 
'beekeeper','bikini', 'blitz','blizzard','boggle','bookworm','boxcar', 
'boxful','buckaroo','buffalo','buffoon','buxom', 'buzzard', 'buzzing', 'buzzwords', 
'caliph','cobweb','cockiness', 'croquet','crypt','curacao','cycle',
'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex','dwarves', 
'embezzle','equip', 'espionage','euouae','exodus', 'faking','fishhook', 
'fixable','fjord','flapjack','flopping','fluffiness','flyby', 
'foxglove', 'frazzled', 'frizzled', 'fuchsia', 
'funny','fgabby','galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm',
'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku','haphazard', 
'hyphen','iatrogenic', 'icebox','injury', 'ivory', 'ivy', 'jackpot', 
'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly','jigsaw', 
'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 
'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 
'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 
'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 
'mnemonic', 'mystify', 'naphtha','nightclub', 'nowadays', 'numbskull', 
'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 
'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 
'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 
'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 
'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 
'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 
'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 
'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 
'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 
'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 
'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 
'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 
'zilch', 'zipper', 'zodiac','zombie']
#All the logo to make the UI more fun and enjoyable
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
n=random.randint(0,213)#picking a random word from the list
chosen=word_list[n]
wordlen=len(chosen)
print('_ '*wordlen)
guess_word=[]
guess=''
cc=0
cw=0
p=0
for i in chosen:
    guess_word.append('_')#initailising the guess word
print(guess_word)
while(cc<wordlen and cw<7):
    print("")
    l=input("enter a letter\n")#taking the guessed letter as input
    for j in range(0,wordlen):
        if(l==chosen[j]):
            guess_word[j]=l
            cc+=1
            p+=1
    if(p==0):#pointer for incorrect guesses
        print("")
        print("Your guessed letter is not present")
        print("you have lost a life")
        print("")
        cw+=1
        print(f"you have {7-cw} lives left")
        print(stages[-cw])
    else:
        print("")
        print("You have found a letter")
        print("")
    p=0        
    for i1 in range(0,wordlen):
         guess=guess+guess_word[i1]+' '
    
    print(guess)
    guess='' 
if(cc>=wordlen):#checking if the player won the game
    print("")
    print("")
    print("CONGRATS YOU HAVE WON THE GAME")
    print("")
    print("")
else:
    print("")
    print("")
    print("THE WORD WAS "+chosen)
    print("""GAME OVER\nTRY AGAIN NEXT TIME\nTHANK YOU FOR PLAYING""")
    print("")
    print("")