import tkinter as tk
from tkinter import ttk
import decimal
from decimal import *

class TempConvert():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('320x150')
        self.root.minsize(320, 150)
        self.root.maxsize(320,150)
        self.root.title('Temperature converter')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand='true')
        
        self.text = ttk.Label(self.mainframe, text='Convert temperature', font=("Fira Code Medium", 15), justify='center')
        self.text.grid(row=0, column=0, columnspan=1000, pady=(10, 20), padx=(45, 0))

        #Convert by choosing the unit

        self.temp_unit_input = ttk.Entry(self.mainframe, width=10, justify='center')
        self.temp_unit_input.grid(row=1, column=7, padx=(70, 0))

        self.temp_unit = ttk.Combobox(self.mainframe, values=['C°', '°F', 'K'], width=3, state='readonly', postcommand=self.empty)
        self.temp_unit.grid(row=1, column=8)

        self.temp_to = ttk.Combobox(self.mainframe, width=3, state='readonly', values='', postcommand=self.modify)
        self.temp_to.grid(row=2, column=8)

        convert_button = ttk.Button(self.mainframe, text='Convert', command=self.convert)
        convert_button.grid(row=1, column=9)

        self.output = ttk.Label(self.mainframe, width=10, borderwidth=1, relief='solid', anchor='center')
        self.output.grid(row=2, column=7, padx=(70, 0))

        self.root.mainloop()
        return
    
    def c_to_f_convert(self):
        celsius = float(self.input_field_c.get())
        self.output_field_f.config(text= '{}' .format(round((celsius * 1.8 + 32),2)))

    def f_to_c_convert(self):
        fahrenheit = float(self.input_field_f.get())
        self.output_field_c.config(text= '{}' .format(round(((fahrenheit - 32) / 1.8),2)))

    def convert(self):
        converted = int(self.temp_unit_input.get())
            
        if self.temp_unit.get() == 'C°' and self.temp_to.get() == '°F':
            self.output.config(text= f'{round((converted * 1.8 + 32),3)}')
        elif self.temp_unit.get() == 'C°' and self.temp_to.get() == 'K':
            if converted >= 0:
                self.output.config(text= f'{round((converted + 273.15),2)}' )
            elif converted < 0:
                self.output.config(test= f'{round((-273.15 + converted),2)}')

        if self.temp_unit.get() == '°F' and self.temp_to.get() == 'C°':
            self.output.config(text= f'{round(((converted - 32) / 1.8),3)}')
        elif self.temp_unit.get() == '°F' and self.temp_to.get() == 'K':
            self.output.config(text= f'{round(((converted + 459.67) / 1.8),3)}' )

        if self.temp_unit.get() == 'K' and self.temp_to.get() == 'C°':
            self.output.config(text= converted - 273.15)
        elif self.temp_unit.get() == 'K' and self.temp_to.get() == '°F':
            self.output.config(text= converted * 1.8 -459.67)

    def modify(self):
        if self.temp_unit.get() == 'C°':
            self.temp_to.config(value=['','°F', 'K'])
            self.temp_to.current(0)

        elif self.temp_unit.get() == '°F':
            self.temp_to.config(value=['', 'C°', 'K'])
            self.temp_to.current(0)

        elif self.temp_unit.get() == 'K':
            self.temp_to.config(value=['' ,'C°', '°F'])
            self.temp_to.current(0)

    def empty(self):
        self.temp_to.set('')
     
if __name__ == '__main__':
    TempConvert()