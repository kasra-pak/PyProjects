import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.minsize(width=300, height=350)
        self.geometry('300x350')
        self.configure(bg='lightgrey')

        # Display of calculator
        self.frm_disp = tk.Frame(self, bg='red', relief=tk.RIDGE, border=3)
        self.frm_disp.columnconfigure([*range(11)], weight=1)
        self.frm_disp.rowconfigure([1, 2], weight=1)
        self.frm_disp.pack(fill=tk.BOTH)

        ## memory usage indicator
        self.lbl_memory = tk.Label(self.frm_disp, text='M', bg='green', font=('system 10 points', 15))
        self.lbl_memory.grid(row=0, column=0, sticky='news')

        ## error indicator; indicates digit overflows
        self.lbl_error = tk.Label(self.frm_disp, text='E', bg='grey', font=('system 10 points', 15))
        self.lbl_error.grid(row=1, column=0, sticky='news')

        ## digits
        self.disp_number = tk.StringVar()
        self.disp_number.set('0.12345678')
        self.lbl_operands = tk.Label(self.frm_disp, textvariable=self.disp_number, bg='lightgrey', anchor='e', font=('system 10 points', 30))
        self.lbl_operands.grid(row=0, column=1, sticky='news', rowspan=2, columnspan=10)

        ## operator
        self.disp_operator = tk.StringVar()
        self.disp_operator.set('+')
        self.lbl_operators = tk.Label(self.frm_disp, textvariable=self.disp_operator, bg='grey', anchor='e', font=80)
        self.lbl_operators.grid(row=0, column=11, sticky='news', rowspan=2)


        # Keypad of calculator
        keys = [['OFF', 'MR', 'M-', 'M+', '÷'],
                ['%', '7', '8', '9', '×'],
                ['√', '4', '5', '6', '-'],
                ['C', '1', '2', '3', '+'],
                ['AC', '0', '●', '=']]

        self.frm_keypad = tk.Frame(self, bg='grey')
        self.frm_keypad.rowconfigure([0, 1, 2 ,3, 4], minsize=1, weight=1)
        self.frm_keypad.columnconfigure([0, 1, 2 ,3, 4], minsize=1, weight=1)
        self.frm_keypad.pack(fill=tk.BOTH, expand=1)

        # majority of approaches declare buttons without loops; this makes modifying your code harder
        # so i tried to declare buttons as maintainable as possible using loops
        keypad_buttons = []
        for i in range(len(keys)):
            for j in range(len(keys[i])):
                btn = tk.Button(self.frm_keypad, text=keys[i][j], bg='lightgrey', relief=tk.RIDGE, border=1, font=10, width=6, height=1)
                # following condition gives the "+" button more height
                if keys[i][j] == '+':
                    btn.grid(row=i, column=j, ipady=2, padx=2, pady=2, sticky='news', rowspan=2)
                # following condition changes the background color for "memory" buttons
                elif keys[i][j] == 'MR' or keys[i][j] == 'M+' or keys[i][j] == 'M-':
                    btn.configure(bg='blue')
                    btn.grid(row=i, column=j, ipady=2, padx=2, pady=2, sticky='news')
                # following condition changes the background color for "clear" buttons
                elif keys[i][j] == 'AC' or keys[i][j] == 'C':
                    btn.configure(bg='red')
                    btn.grid(row=i, column=j, ipady=2, padx=2, pady=2, sticky='news')
                # and finally the condition for ordinary buttons
                else:
                    btn.grid(row=i, column=j, ipady=2, padx=2, pady=2, sticky='news')

                keypad_buttons.append(btn)



if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
