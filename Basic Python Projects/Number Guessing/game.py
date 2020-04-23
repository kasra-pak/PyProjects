import random

def guess(goal, attempts=10):
  print(f"You've got {attempts} attempts")
  print('Make a guess!!')
  
  while attempts:
    guess = int(input('> '))
    attempts -= 1

    if guess < goal:
      print(f'low\t\t {attempts} attempts left')
    elif guess > goal:
      print(f'high\t\t {attempts} attempts left')
    else:
      return f'Excellent!! The answer was {goal}'
    
  return f'Sadly you ran out of attempts!! The answer was {goal}'


print('<-Number Guessing Game->')
while True:
    number_range = {'easy': 10, 'normal': 25, 'hard': 50}
    level = input('Enter game level please (easy, normal or hard)\n> ')
    
    if level in number_range.keys():
      print(f"Allright, the number is between 1 and {number_range[level]}")
      goal = random.randint(1, number_range[level] + 1)
      print(guess(goal))
      ans = input('Wanna try again?(y/n)\n> ')
      if ans == 'n':
        break
      elif ans == 'y':
        continue
      else:
        break
    else:
        print(f'{level} is not a valid entry')
        continue
