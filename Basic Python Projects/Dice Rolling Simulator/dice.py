from pynput import keyboard   #pip install pynput
import sys
import random

def roll(dice):
    if dice == 1:
        return random.randint(1,6)
    else:
        return (random.randint(1,6), random.randint(1,6))

print('(=Dice Rolling Simulator=)')
print('How many dices you want for each roll? (1 or 2)')
while True:
    try:
        dice = int(input('> '))
        if dice in [1, 2]:
            break
        else:
            print('please enter 1 or 2!!')
            continue
    except ValueError:
        print('enter a number')
        continue
        
print("Press 'Space' to roll a dice or 'Escape' to exit")

def on_release(key):
    if key == keyboard.Key.space:
        print(roll(dice))
    elif key == keyboard.Key.esc:
        sys.exit()


with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
