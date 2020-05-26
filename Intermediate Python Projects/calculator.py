import tkinter as tk
from math import sqrt
from decimal import Decimal
from decimal import InvalidOperation


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
        self.disp_number.set('0')
        self.lbl_operand = tk.Label(self.frm_disp, textvariable=self.disp_number, bg='lightgrey', anchor='e', font=('system 10 points', 30))
        self.lbl_operand.grid(row=0, column=1, sticky='news', rowspan=2, columnspan=10)

        ## operator
        self.lbl_operator = tk.Label(self.frm_disp, text=' ', bg='grey', anchor='e', font=80)
        self.lbl_operator.grid(row=0, column=11, sticky='news', rowspan=2)
        self.operator = None


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

        # just unpacking each button object from the list; don't panic :D
        self.btn_off, \
        self.btn_mem_read, \
        self.btn_mem_sub, \
        self.btn_mem_add, \
        self.btn_divide, \
        self.btn_percent, \
        self.btn_seven, \
        self.btn_eight, \
        self.btn_nine, \
        self.btn_multiply, \
        self.btn_sqrt, \
        self.btn_four, \
        self.btn_five, \
        self.btn_six, \
        self.btn_subtract, \
        self.btn_clear, \
        self.btn_one, \
        self.btn_two, \
        self.btn_three, \
        self.btn_add, \
        self.btn_all_clear, \
        self.btn_zero, \
        self.btn_dot, \
        self.btn_equal = keypad_buttons

        # this flag would turn to True when ever you print calculation results on the screen by pressing '='
        self.sth_on_screen_flag = False
        # temp_operand stores the first_operand in case the user doesn't enter the second_operand
        self.first_operand, self.second_operand , self.temp_operand= 0, None, None

        self.btn_zero.configure(command=lambda :self.enter_number(0))
        self.btn_one.configure(command=lambda :self.enter_number(1))
        self.btn_two.configure(command=lambda :self.enter_number(2))
        self.btn_three.configure(command=lambda :self.enter_number(3))
        self.btn_four.configure(command=lambda :self.enter_number(4))
        self.btn_five.configure(command=lambda :self.enter_number(5))
        self.btn_six.configure(command=lambda :self.enter_number(6))
        self.btn_seven.configure(command=lambda :self.enter_number(7))
        self.btn_eight.configure(command=lambda :self.enter_number(8))
        self.btn_nine.configure(command=lambda :self.enter_number(9))

        self.btn_add.configure(command=self.add)
        self.btn_subtract.configure(command=self.subtract)
        self.btn_multiply.configure(command=self.multiply)
        self.btn_divide.configure(command=self.divide)
        self.btn_sqrt.configure(command=self.square_root)
        # self.btn_percent.configure(command=self.)
        self.btn_equal.configure(command=self.equal)

        self.btn_off.configure(command=self.close_window)
        # self.btn_mem_read.configure(command=self.)
        # self.btn_mem_sub.configure(command=self.)
        # self.btn_mem_add.configure(command=self.)
        self.btn_clear.configure(command=self.clear)
        self.btn_all_clear.configure(command=self.all_clear)
        self.btn_dot.configure(command=self.dot)


    def close_window(self):
        self.destroy()

    def all_clear(self):
        self.disp_number.set('0')
        self.lbl_operator.configure(text=' ')
        self.first_operand, self.second_operand, self.temp_operand = 0, None, None
        self.sth_on_screen_flag = False
        self.operator = None

    def clear(self):
        self.disp_number.set('0')
        self.second_operand = None
        self.sth_on_screen_flag = False

    def fetch_screen(self):
        """reads the current number from the display"""
        try:
            return int(self.disp_number.get())
        except ValueError:
            return self.disp_number.get()

    def add_digit(self, num):
        try:
            # for floating points
            if '.' in str(self.fetch_screen()):
                return str(self.fetch_screen()) + str(num)
            # for integers
            else:
                return int(str(self.fetch_screen()).lstrip('0') + str(num))
        except ValueError:
            return str(self.fetch_screen()).lstrip('0') + str(num)

    def enter_number(self, num):
        if self.lbl_operator['text'] == ' ':
            if self.sth_on_screen_flag:
                self.disp_number.set(num)
                self.first_operand = self.fetch_screen()
                self.sth_on_screen_flag = False
            else:
                self.disp_number.set(self.add_digit(num))
                self.first_operand = self.fetch_screen()
        else:
            if self.sth_on_screen_flag:
                self.first_operand = self.fetch_screen()
                self.disp_number.set(num)
                self.second_operand = self.fetch_screen()
                self.sth_on_screen_flag = False
            else:
                if self.second_operand == None:
                    self.disp_number.set(self.add_digit(num))
                    self.second_operand = num
                    self.disp_number.set(str(num))
                else:
                    # self.second_operand = int(str(self.second_operand).lstrip('0') + str(num))
                    number = str(self.add_digit(num))
                    if '.' in number:
                        self.second_operand = number
                        self.disp_number.set(str(self.second_operand))
                        self.second_operand = float(self.second_operand)
                    else:
                        self.second_operand = number
                        self.disp_number.set(str(self.second_operand))
                        self.second_operand = int(self.second_operand)

    def dot(self):
        if '.' not in str(self.fetch_screen()):
            self.disp_number.set(str(self.fetch_screen()) + '.')
        else:
            pass

    def operate(self, opr):
        if not self.second_operand:
            self.disp_number.set(str(self.fetch_screen()).rstrip('.0') or 0)
            self.operator = opr
            if opr == '*' or opr == '/':
                self.temp_operand = self.first_operand
            else:
                self.temp_operand = 0
        else:
            # this part covers continuous operations like: 3+3*2
            if self.second_operand:
                first_operand_temp = Decimal(str(self.first_operand))
                second_operand_temp = Decimal(str(self.second_operand))
                self.first_operand = eval(f"(first_operand_temp {self.operator} second_operand_temp)")
                self.operator = opr
                self.disp_number.set(str(self.first_operand).rstrip('.0') or 0)
                self.second_operand = None
                self.sth_on_screen_flag = True
            else:
                self.operator = opr


    def add(self):
        self.lbl_operator.configure(text='+')
        self.operate('+')

    def subtract(self):
        self.lbl_operator.configure(text='-')
        self.operate('-')

    def multiply(self):
        self.lbl_operator.configure(text='×')
        self.operate('*')

    def divide(self):
        self.lbl_operator.configure(text='÷')
        self.operate('/')

    def square_root(self):
        if self.first_operand:
            self.first_operand = sqrt(self.first_operand)
            # as long as possible keep the results as integers otherwise show them as floating points
            try:
                self.disp_number.set(int(str(self.first_operand)))
            # covers floating point results
            except ValueError:
                self.disp_number.set(str(self.first_operand))
        else:
            pass

    def equal(self):
        try:
            if self.second_operand:
                first_operand_temp = Decimal(str(self.first_operand))
                second_operand_temp = Decimal(str(self.second_operand))
                self.disp_number.set(str(eval(f"(first_operand_temp {self.operator} second_operand_temp)")).rstrip('.0') or 0)
                self.lbl_operator.configure(text=' ')
                self.first_operand = self.disp_number.get()
                self.second_operand = None
                self.sth_on_screen_flag = True
            else:
                first_operand_temp = Decimal(str(self.first_operand))
                temp_operand_temp = Decimal(str(self.temp_operand))
                self.disp_number.set(str(eval(f"first_operand_temp {self.operator} temp_operand_temp")).rstrip('.0') or 0)
                self.lbl_operator.configure(text=' ')
                self.first_operand = self.disp_number.get()
                self.second_operand = None
                self.sth_on_screen_flag = True


        # when user just press "=" button with no operands
        except InvalidOperation:
            self.disp_number.set(str(self.first_operand).rstrip('.0') or 0)


if __name__ == '__main__':
    calc = Calculator()
    calc.mainloop()
