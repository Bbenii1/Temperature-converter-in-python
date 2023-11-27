from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('300x150')
root.title('Converter')


def homePage():
    frame = Frame(root, width=300, height=150)
    frame.place(x=0,y=0)
    
    proceed = ttk.Button(frame, text='Temperature converter', command=temp_converter)
    proceed.place(x=85, y=20)

global temp_unit, temp_to, output, temp_unit_input
   
def temp_converter():
    frame2 = Frame(root, width=300, height=150)
    frame2.place(x=0, y=0)
            
    text = ttk.Label(frame2, text='Temperature converter', font=("Fira Code Medium", 15), justify='center')
    text.grid(row=0, column=0, columnspan=10, pady=(10, 20), padx=(45, 0))

    global temp_unit_input, temp_unit, temp_to, output
    #Convert by choosing the unit
    temp_unit_input = ttk.Entry(frame2, width=10, justify='center')
    temp_unit_input.grid(row=1, column=7, padx=(20, 0))

    temp_unit = ttk.Combobox(frame2, values=['C°', '°F', 'K'], width=3, state='readonly', postcommand=empty)
    temp_unit.grid(row=1, column=8)
    
    temp_to = ttk.Combobox(frame2, width=3, state='readonly', values='', postcommand=modify)
    temp_to.grid(row=2, column=8)

    convert_button = ttk.Button(frame2, text='Convert', command=convert)
    convert_button.grid(row=1, column=9)
    
    output = ttk.Label(frame2, width=10, borderwidth=1, relief='solid', anchor='center')
    output.grid(row=2, column=7, padx=(20,0))

    #go Home
    home = ttk.Button(frame2, text='X', command=homePage, width=2,)
    home.place(x=0,y=0)

def convert():
    converted = int(temp_unit_input.get())
           
    if temp_unit.get() == 'C°' and temp_to.get() == '°F':
        output.config(text= f'{round((converted * 1.8 + 32),3)}')
    elif temp_unit.get() == 'C°' and temp_to.get() == 'K':
        if converted >= 0:
            output.config(text= f'{round((converted + 273.15),2)}' )
        elif converted < 0:
            output.config(test= f'{round((-273.15 + converted),2)}')

    if temp_unit.get() == '°F' and temp_to.get() == 'C°':
        output.config(text= f'{round(((converted - 32) / 1.8),3)}')
    elif temp_unit.get() == '°F' and temp_to.get() == 'K':
        output.config(text= f'{round(((converted + 459.67) / 1.8),3)}' )

    if temp_unit.get() == 'K' and temp_to.get() == 'C°':
        output.config(text= f'{round(converted - 273.15,3)}')
    elif temp_unit.get() == 'K' and temp_to.get() == '°F':
        output.config(text= f'{round(converted * 1.8 -459.67,3)}')

def modify():
    if temp_unit.get() == 'C°':
        temp_to.config(value=['','°F', 'K'])
        temp_to.current(0)

    elif temp_unit.get() == '°F':
        temp_to.config(value=['', 'C°', 'K'])
        temp_to.current(0)

    elif temp_unit.get() == 'K':
        temp_to.config(value=['' ,'C°', '°F'])
        temp_to.current(0)

def empty():
    temp_to.set('')

homePage()
root.mainloop()