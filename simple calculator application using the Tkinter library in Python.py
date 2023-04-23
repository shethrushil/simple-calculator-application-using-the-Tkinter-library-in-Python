# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:25:56 2023

@author: rushilsheth
"""

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display entry widget
        self.display = tk.Entry(master, width=30, justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create the number buttons
        for i in range(10):
            tk.Button(master, text=str(i), width=5, height=2, command=lambda x=i: self.append_number(x)).grid(row=(i+3)//3, column=(i-1)%3)

        # Create the operation buttons
        tk.Button(master, text='+', width=5, height=2, command=self.add).grid(row=3, column=3)
        tk.Button(master, text='-', width=5, height=2, command=self.subtract).grid(row=4, column=3)
        tk.Button(master, text='*', width=5, height=2, command=self.multiply).grid(row=5, column=3)
        tk.Button(master, text='/', width=5, height=2, command=self.divide).grid(row=6, column=3)
        tk.Button(master, text='=', width=5, height=2, command=self.equals).grid(row=6, column=2)
        tk.Button(master, text='C', width=5, height=2, command=self.clear).grid(row=6, column=1)

        # Initialize calculator variables
        self.first_number = None
        self.operation = None

    def append_number(self, number):
        if self.operation == None:
            if self.first_number == None:
                self.first_number = number
            else:
                self.first_number = str(self.first_number) + str(number)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.first_number)
        else:
            if self.second_number == None:
                self.second_number = number
            else:
                self.second_number = str(self.second_number) + str(number)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.second_number)

    def add(self):
        self.operation = '+'
        self.second_number = None

    def subtract(self):
        self.operation = '-'
        self.second_number = None

    def multiply(self):
        self.operation = '*'
        self.second_number = None

    def divide(self):
        self.operation = '/'
        self.second_number = None

    def equals(self):
        if self.first_number != None and self.operation != None and self.second_number != None:
            if self.operation == '+':
                result = int(self.first_number) + int(self.second_number)
            elif self.operation == '-':
                result = int(self.first_number) - int(self.second_number)
            elif self.operation == '*':
                result = int(self.first_number) * int(self.second_number)
            elif self.operation == '/':
                result = int(self.first_number) / int(self.second_number)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.first_number = result
            self.operation = None
            self.second_number = None

    def clear(self):
        self.display.delete(0, tk.END)
        self.first_number = None
        self.operation = None
        self.second_number = None

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
