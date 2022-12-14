import random


f = open('words.txt').read().split()
a = 1
d = {
  '1': 'st',
  '2': 'nd',
  '3': 'rd',
  '4': 'th'
}

easy = []
normal = []
hard = []

for i in f:
  if len(i) in (3, 4):
    easy.append(i)
  elif len(i) in (5, 6):
    normal.append(i)
  elif len(i) > 6:
    hard.append(i)

z = 1
print("Welcome to Jumble Words Game!\n If you want to quit anytime, type '0'.\nThe game is divided into 3 difficulties.\nEasy, Normal, Hard.\nYou will have 3 tries to guess a word!")
print()
diff = input("Choose Your Difficulty (Easy, Normal, Hard): ").lower()
if diff == 'easy':
    wl = easy
elif diff == 'normal':
    wl = normal
elif diff == 'hard':
    wl = hard
else:
    print("Invalid Choice. Aborting!")
    z = 0
score = 0
while z == 1:
  tries = 3
  picked = random.choice(f)
  jum = random.sample(picked, len(picked))
  jumble = ''.join(jum)
  picked = random.choice(wl)
  jum = random.sample(picked, len(picked))
  jumble = ''.join(jum)
  if jumble == picked:
    continue
  print('So here is your', a, d[str(a)] if str(a) in d else 'th', 'Word\n', jumble)
  guess = input("Your Guess: ")
  if guess == jumble:
    print("Correct! You got a point")
    score += 1
    a += 1
  elif guess == "0":
    print("Thank You for playing!\nYour Total Score:", score)
  else:
    tries -= 1
    print("Wrong Guess, You lost a try, Available tries:", tries)
    if tries == 0:
       print("You lost!\nYour Total Score:", score)
       print("The word was:", picked)
       break
    else:
      x = input("Guess: ")
      if x == jumble:
        print("This Time you got the right one! gg")
        score = score + 1
      elif x == "0":
        print("Your total score:", score)
        break

      else:
        print("Wrong Guess, You lost a try, available tries:", tries-1)
        tries = tries - 1
        if tries == 0:
          print("You lost!\nYour Total Score:", score)
          print("The word was:", picked)
          break

        else:
          j = input("Guess: ")
          if j == jumble:
            print("This time you got the right one! gg")
            score = score + 1
          elif j == "0":
            print("Your total score:", score)
            break
          else:
            print("Wrong Guess, 0 tries available")
            print("You lost!\nYour Total Score:", score)
            print("The word was:", picked)
            break
