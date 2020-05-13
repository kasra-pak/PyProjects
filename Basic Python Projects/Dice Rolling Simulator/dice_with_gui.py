import tkinter as tk
import random

def roll():
    if dice_count.get() == 1:
        lbl_number['text'] = str(random.randint(1, 6))
    else:
        lbl_number['text'] = str(random.randint(1, 6)) + '\t' + str(random.randint(1, 6))

window = tk.Tk()
window.title('Rolling Dice Simulator')
window.configure(bg='#AED6F1')
window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure(0, minsize=300, weight=1)

# how many dices the user wants to roll
dice_count = tk.IntVar()
# the first button is checked at the begining
dice_count.set(1)

frm_radio_buttons = tk.Frame(master=window, bg='#85C1E9')
frm_radio_buttons.grid(row=0, sticky='swe', ipady=2)

rad_btn_single = tk.Radiobutton(master=frm_radio_buttons, text='Single', variable=dice_count, value=1, bg='#85C1E9')
rad_btn_single.grid(row=0, column=0)
rad_btn_double = tk.Radiobutton(master=frm_radio_buttons, text='Double', variable=dice_count, value=2, bg='#85C1E9')
rad_btn_double.grid(row=0, column=1)


btn_roll = tk.Button(master=window, text='Roll', command=roll, width=14, bg='#3498DB')
btn_roll.grid(row=1, pady=10)
#
lbl_number = tk.Label(bg='#85C1E9')
lbl_number.grid(row=2, sticky='new', ipady=4)

window.mainloop()
