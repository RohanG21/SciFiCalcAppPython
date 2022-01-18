
from tkinter import *
from tkinter import ttk, StringVar
import math
#problems to solve:
    #have deci point button


class Expression:

    def __init__(self, root):
        self.a = None
        self.sign = None
        self.b = None
        self.aNegation = 0
        self.bNegation = 0
        self.bDigitCount = 0
        self.result = StringVar()
        self.radOrDeg = 0
        root.title("Scientific Calculator")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky="N W E S")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        frame = ttk.Frame(mainframe)
        # set result box frame size
        frame.grid(column=1, row=1, sticky="N W E S")
        resultbox = ttk.Label(frame)
        resultbox.configure(background='grey50', width=50)
        resultbox.grid(column=1, row=1, sticky="N W E S")
        resultbox['textvariable'] = self.result

        # buttons
        ttk.Button(mainframe, text="0", command=self.insert0).grid(column=1, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="1", command=self.insert1).grid(column=2, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="2", command=self.insert2).grid(column=3, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="3", command=self.insert3).grid(column=4, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="4", command=self.insert4).grid(column=5, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="5", command=self.insert5).grid(column=6, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="6", command=self.insert6).grid(column=7, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="7", command=self.insert7).grid(column=8, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="8", command=self.insert8).grid(column=9, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="9", command=self.insert9).grid(column=10, row=2, sticky="N W E S")
        ttk.Button(mainframe, text="+", command=self.addition).grid(column=1, row=3, sticky="N W E S")
        ttk.Button(mainframe, text="-", command=self.subtraction).grid(column=2, row=3, sticky="N W E S")
        ttk.Button(mainframe, text="/", command=self.divide).grid(column=3, row=3, sticky="N W E S")
        ttk.Button(mainframe, text="*", command=self.multiplication).grid(column=4, row=3, sticky="N W E S")
        ttk.Button(mainframe, text="calculate", command=self.calculate).grid(column=6, row=3, sticky="N W E S")
        ttk.Button(mainframe, text="clear", command=self.clear).grid(column=7, row=3, sticky="N W E S")
        ttk.Button(mainframe, text="x^", command=self.exponentiate).grid(column=5, row=3, sticky ="N W E S")
        ttk.button(mainframe, text="sin", command=self.sinx).grid(column=1, row=4, sticky="N W E S")
        ttk.button(mainframe, text="cos", command=self.cosx).grid(column=2, row=4, sticky="N W E S")
        ttk.button(mainframe, text="tan", command=self.tanx).grid(column=3, row=4, sticky="N W E S")
        ttk.button(mainframe, text="rad", command=self.convertToRad).grid(column=1, row=5, sticky= "N W E S")
        ttk.button(mainframe, text="deg", command=self.convertToDeg).grid(column=2, row=5, sticky= "N W E S")

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        root.bind("<Return>", self.calculate)

    def insert0(self, *args):
        if self.a is None:
            self.a = 0
        else:
            if self.sign is None:
                self.a = self.a*10

            else:
                if self.bDigitCount > 0:
                    self.b = self.b*10
                    self.bDigitCount = self.bDigitCount+1
                else:
                    self.b = 0

    def insert1(self, *args):
        if self.a is None:
            self.a = 1
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 1
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 1
                else:
                    self.b = 1
                    self.bDigitCount = self.bDigitCount + 1

    def insert2(self, *args):
        if self.a is None:
            self.a = 2
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 2
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 2
                else:
                    self.b = 2
                    self.bDigitCount = self.bDigitCount+1

    def insert3(self, *args):
        if self.a is None:
            self.a = 3
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 3
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 3
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 3
                    self.bDigitCount = self.bDigitCount + 1

    def insert4(self, *args):
        if self.a is None:
            self.a = 4
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 4
            else:
                if self.bDigitCount > 0:
                    self.b = self.b*10
                    self.b = self.b+4
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 4
                    self.bDigitCount = self.bDigitCount + 1

    def insert5(self, *args):
        if self.a is None:
            self.a = 5
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 5
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 5
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 5
                    self.bDigitCount = self.bDigitCount + 1
    def insert6(self, *args):
        if self.a is None:
            self.a = 6
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 6
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 6
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 6
                    self.bDigitCount = self.bDigitCount + 1

    def insert7(self, *args):
        if self.a is None:
            self.a = 7
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 7
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 8
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 7
                    self.bDigitCount = self.bDigitCount + 1

    def insert8(self, *args):
        if self.a is None:
            self.a = 8
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 8
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 8
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 8
                    self.bDigitCount = self.bDigitCount + 1

    def insert9(self, *args):
        if self.a is None:
            self.a = 9
        else:
            if self.sign is None:
                self.a = self.a * 10
                self.a = self.a + 9
            else:
                if self.bDigitCount > 0:
                    self.b = self.b * 10
                    self.b = self.b + 9
                    self.bDigitCount = self.bDigitCount + 1
                else:
                    self.b = 9
                    self.bDigitCount = self.bDigitCount + 1

    def addition(self, *args):
       if self.a is not None:
        self.sign = '+'

    def subtraction(self, *args):
        if self.a is None:
            self.aNegation = 1
        elif self.sign is None:
            self.sign = '-'
        else:
            self.bNegation = 1

    def multiplication(self, *args):
        if self.a is not None:
         self.sign = '*'

    def divide(self, *args):
       if self.a is not None:
        self.sign = '/'

    def calculate(self, *args):
        if self.a is not None and self.b is not None:
            if self.aNegation == 1:
                self.a = self.a * -1
            if self.bNegation == 1:
                self.b = self.b * -1
            if self.sign == '+':
                self.result.set(str(self.a + self.b))
                self.a = self.a + self.b
                self.b = None
                self.sign = None
                self.bDigitCount = 0
                self.aNegation = 0
                self.bNegation = 0
            elif self.sign == '-':
                self.result.set(str(self.a - self.b))
                self.a = self.a - self.b
                self.b = None
                self.sign = None
                self.bDigitCount = 0
                self.aNegation = 0
                self.bNegation = 0
            elif self.sign == '*':
                self.result.set(str(self.a * self.b))
                self.a = self.a * self.b
                self.b = None
                self.sign = None
                self.bDigitCount = 0
                self.aNegation = 0
                self.bNegation = 0
            elif self.sign == '/':
                if self.b == 0:
                    self.a = None
                    self.b = None
                    self.bDigitCount = 0
                    self.sign = None
                    self.aNegation = 0
                    self.bNegation = 0
                    self.result.set("Err")
                else:
                    self.result.set(str(self.a / self.b))
                    self.a = self.a / self.b
                    self.b = None
                    self.sign = None
                    self.bDigitCount = 0
                    self.aNegation = 0
                    self.bNegation = 0
            elif self.sign == '^':
                if self.b == 0:
                    self.a = None
                    self.b = None
                    self.sign = None
                    self.result.set(str(1))
                    self.bNegation = 0
                    self.aNegation = 0
                else:
                    exvalue = 1
                    i = 0
                    while i < abs(self.b):
                        exvalue = (exvalue * self.a)
                        i = i+1
                    if self.b < 0:
                        self.result.set(str(1/exvalue))
                        self.a = 1/exvalue
                    else:
                        self.result.set(str(exvalue))
                        self.a = exvalue
                    self.b = None
                    self.bDigitCount = 0
                    self.sign = None
                    self.aNegation = 0
                    self.bNegation = 0

    def exponentiate(self):
        if self.sign is None:
            self.sign = '^'
    def sinx(self):
        if self.radOrDeg == 0:
            ans = math.sin(math.radians(self.a))
            self.result.set(str(ans))
        else:
            ans = math.sin(self.a)
            self.result.set(str(ans))
    def cosx(self):
        if self.radOrDeg == 0:
            ans = math.cos(math.radians(self.a))
            self.result.set(str(ans))
        else:
            ans = math.cos(self.a)
            self.result.set(str(ans))


    def tanx(self):
        if self.radOrDeg == 0:
            ans = math.tan(math.radians(self.a))
            self.result.set(str(ans))
        else:
            ans = math.tan(self.a)
            self.result.set(str(ans))
    def convertToRad(self):
        self.a *= (math.pi/180)
        self.radOrDeg = 1
    def convertToDeg(self):
        if self.radOrDeg !=0 :
            self.a *= 180/math.pi

    def clear(self):
        self.a = None
        self.b = None
        self.aNegation=0
        self.bNegation=0
        self.radOrDeg = 0
        self.bDigitCount = 0
        self.sign = None
        self.result.set("cleared")

# features to include: allowing multiple digits in one number,
# appending operations and digit, multiple digits meaning result is a,x^,log,clear,(,),


test = Tk()
Expression(test)
test.mainloop()