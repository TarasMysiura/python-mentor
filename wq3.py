from tkinter import *
from decimal import *
 
win = Tk()
win.title('Калькулятор')
 
buttons = (('7', '8', '9', '/'),
          ('4', '5', '6', '*'),
          ('1', '2', '3', '-'),
          ('0', '.', '=', '+')
          )
 
activeStr = ' '
Stack = []
 
def Calculate():
   global stack
   global label
   result = 0
   num2 = Decimal(Stack.pop())
   operation = Stack.pop()
   num1 = Decimal(Stack.pop())
 
   if operation == '+':
       result = num1 + num2
   if operation == '-':
       result = num1 - num2
   if operation == '/':
     try:
       result = num1 / num2
     except DivisionByZero:
          result = "На 0 делить нельзя!"
   if operation == '*':
       result = num1 * num2
   label.configure(text = str(result))
 
 
def Click(text):
     global activeStr
     global Stack
 
     if text == 'CE':
          Stack.clear()
          activeStr = ' '
          label.configure(text = '0')
 
     elif '0' <= text <= '9':
          activeStr += text
          label.configure(text = activeStr)
 
     elif text == '.':
          if activeStr.find('.') == -1:
               activeStr += text
               label.configure(text = activeStr)
 
     else:
          if len(Stack) >= 2:
               Stack.append(label['text'])
               Calculate()
               Stack.clear()
               Stack.append(label['text'])
               activeStr = ' '
               if text != '=':
                    Stack.append(text)
          else:
               if text != '=':
                    Stack.append(label['text'])
                    Stack.append(text)
                    activeStr = ' '
                    label.configure(text = '0')
 
 
 
label = Label(win, text = '0', width = 35, font = 'Times 15')
label.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")
 
button = Button(win, text = 'CE', font = 'Times 15', command = lambda text = 'CE': Click(text))
button.grid(row = 1, column = 3, sticky = "nsew", ipadx = 20, ipady = 5)
for row in range(4):
   for col in range(4):
       button = Button(win, text = buttons[row][col], font = 'Times 15', command = lambda row = row, col = col: Click(buttons[row][col]))
       button.grid(row = row + 2, column = col, sticky = "nsew", ipadx = 30, ipady = 15)
 
win.grid_rowconfigure(6, weight = 1)
win.grid_columnconfigure(4, weight = 1)
 
win.mainloop()