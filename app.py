import tkinter as tk
from tkinter import font

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        rows=5
        cols=4

        for i in range(rows):
            self.master.rowconfigure(i, weight=1)
        for i in range(cols):
            self.master.columnconfigure(i, weight=1)

        # create a font
        self.base_font = font.Font(self.master, family="Comic Sans MS", size=12, weight="bold")
        
        # create a display widget
        self.display = tk.Label(self.master, text="0", width=25, height=2, anchor="e", font=self.base_font)
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        # create number buttons
        button_list = []
        for i in range(0, 10):
            if(i == 0):
                button_list.append(tk.Button(self.master, text=f"{i}", width=15, height=2, font=self.base_font,
                                             command=lambda i=i:self.add_digit(f"{i}")))
                button_list[i].grid(row=4, column=0, columnspan=2, sticky="NSEW")
            else:
                button_list.append(tk.Button(self.master, text=f"{i}", width=5, height=2, font=self.base_font,
                                             command=lambda i=i:self.add_digit(f"{i}")))
                button_list[i].grid(row=3-(i-1)//3, column=(i-1)%3, sticky="NSEW")
        
        # create ops buttons
        self.button_plus = tk.Button(self.master, text="+", width=5, height=2, font=self.base_font, command=self.add)
        self.button_plus.grid(row=3, column=3, sticky="NSEW")

        self.button_plus = tk.Button(self.master, text="-", width=5, height=2, font=self.base_font, command=self.subtract)
        self.button_plus.grid(row=2, column=3, sticky="NSEW")

        self.button_plus = tk.Button(self.master, text="*", width=5, height=2, font=self.base_font, command=self.multiply)
        self.button_plus.grid(row=1, column=3, sticky="NSEW")

        self.button_plus = tk.Button(self.master, text="/", width=5, height=2, font=self.base_font, command=self.divide)
        self.button_plus.grid(row=0, column=3, sticky="NSEW")
        
        self.button_equals = tk.Button(self.master, text="=", width=5, height=2, font=self.base_font, command=self.equals)
        self.button_equals.grid(row=4, column=3, sticky="NSEW")

        self.button_equals = tk.Button(self.master, text=".", width=5, height=2, font=self.base_font,
                                       command=self.decimal)
        self.button_equals.grid(row=4, column=2, sticky="NSEW")
        
        # initialize variables
        self.operand1 = None
        self.operand2 = None
        self.total = 0
        self.current_value = 0
        self.operator = ""
        self.new_number = True
        self.new_equation = True

    
    def add_digit(self, digit):
        if self.new_equation:
            self.operand1 = None
            self.operand2 = None
            self.total = 0
            self.new_equation = False
        if self.new_number:
            self.current_value = int(digit)
            self.new_number = False
        else:
            self.current_value = self.current_value * 10 + int(digit)
        self.display.config(text=str(self.current_value))
        
    def add(self):
        if(self.operand1 == None):
            self.operand1 = self.current_value
        elif(self.new_equation):
            self.new_equation = False
        else:
            self.operand2 = self.current_value
            self.operand1 = self.calc_op()
            self.display.config(text=str(self.operand1))
        self.operator = "+"
        self.new_number = True

    def subtract(self):
        if(self.operand1 == None):
            self.operand1 = self.current_value
        elif(self.new_equation):
            self.new_equation = False
        else:
            self.operand2 = self.current_value
            self.operand1 = self.calc_op()
            self.display.config(text=str(self.operand1))
        self.operator = "-"
        self.new_number = True

    def multiply(self):
        if(self.operand1 == None):
            self.operand1 = self.current_value
        elif(self.new_equation):
            self.new_equation = False
        else:
            self.operand2 = self.current_value
            self.operand1 = self.calc_op()
            self.display.config(text=str(self.operand1))
        self.operator = "*"
        self.new_number = True

    def divide(self):
        if(self.operand1 == None):
            self.operand1 = self.current_value
        elif(self.new_equation):
            self.new_equation = False
        else:
            self.operand2 = self.current_value
            self.operand1 = self.calc_op()
            self.display.config(text=str(self.operand1))
        self.operator = "/"
        self.new_number = True

    def decimal(self):
        if not self.new_number:
            pass

    def calc_op(self):
        if self.operator == "+":
             return self.operand1 + self.operand2
        if self.operator == "-":
             return self.operand1 - self.operand2
        if self.operator == "/":
             return self.operand1 / self.operand2
        if self.operator == "*":
             return self.operand1 * self.operand2
    
    def equals(self):
        if self.operand1 == None:
            self.operand1 = self.current_value
            self.total = self.operand1
            self.display.config(text=str(self.total))
            self.new_number = True
            self.new_equation = True
            return
        self.operand2 = self.current_value
        self.total = self.calc_op()
        self.operand1 = self.total

        self.operand2 = None
        self.display.config(text=str(self.total))
        self.new_number = True
        self.new_equation = True

root = tk.Tk()
calculator = CalculatorGUI(root)
root.mainloop()
