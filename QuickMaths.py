from tkinter import *

root = Tk()

root.geometry('394x400')
root.configure(bg = '#17161b')
root.title('QuickMaths')
root.resizable(False,False)

equation = ''

def click(num):
  global equation
  equation+=num
  label_result.config(text = equation)
 
def clear():
  global equation
  equation = ''
  label_result.config(text = equation)
 
def calculate():
    global equation
    result = ''
    if equation != '':
        try:
            result = eval(equation)
        except:
            result = 'error'
            equation = ''
    label_result.config(text = result)

def back():
  global equation
  equation = equation[:-1]
  label_result.config(text = equation)

# result label
 
label_result = Label(root,width = 15, height= 1, font = ('arial',30))
label_result.grid(row = 0 , columnspan = 4)
          	 
# button widgets (arithmetic operators)

button_c = Button(root,text = 'C',width= 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#3697f5',command = lambda: clear())  
button_c.grid(row = 1,column = 0,pady = 5)

button_divi = Button(root,text = '/',width = 7,height =3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('/'))
button_divi.grid(row = 1,column =1)

button_percentage = Button(root,text = '%',width = 7,height =3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('%'))
button_percentage.grid(row = 1, column = 2)

button_asterisk = Button(root, text = '*',width = 7,height =3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('*'))
button_asterisk.grid(row = 1,column =3)

button_minus = Button(root,text = '-',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('-'))
button_minus.grid(row = 2,column = 3,pady = 5)

button_plus = Button(root,text = '+',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('+'))
button_plus.grid(row = 3,column = 3,pady = 5)

button_equal = Button(root,text = '=',width = 7,height = 8,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#fe9037',command = lambda: calculate())
button_equal.grid(row = 4 ,column = 3,rowspan = 2)

button_dot = Button(root,text = '.',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('.'))
button_dot.grid(row = 5,column = 2,pady = 5)

button_back = Button(root,text = '<-',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: back())
button_back.grid(row = 5,column = 0)

# button widgets (0-9)

button_7 = Button(root,text = '7',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('7'))
button_7.grid(row = 2,column = 0,pady = 5)

button_8 = Button(root,text= '8',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('8'))
button_8.grid(row = 2,column = 1)

button_9 = Button(root,text = '9',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('9'))
button_9.grid(row = 2,column = 2)

button_4 = Button(root,text = '4',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('4'))
button_4.grid(row = 3,column =0,pady = 5)

button_5 = Button(root,text = '5',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('5'))
button_5.grid(row = 3,column = 1)

button_6 = Button(root,text = '6',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('6'))
button_6.grid(row = 3,column = 2)

button_1 = Button(root,text = '1',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('1'))
button_1.grid(row = 4,column = 0,pady = 5)

button_2 = Button(root,text = '2',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('2'))
button_2.grid(row = 4,column = 1)

button_3 = Button(root,text = '3',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('3'))
button_3.grid(row = 4,column = 2)

button_0 = Button(root,text = '0',width = 7,height = 3,font=('arial',9,'bold'),bd = 1,fg='#fff',bg = '#2a2d36',command = lambda: click('0'))
button_0.grid(row = 5,column = 1,pady = 5)


root.mainloop()
