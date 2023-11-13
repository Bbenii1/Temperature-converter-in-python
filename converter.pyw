import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('620x150')
        self.root.title('Temperature converter')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand='true')
        
        self.text = ttk.Label(self.mainframe, text='Üdv Koma!', font=("Fira Code Medium", 20), justify='center')
        self.text.grid(row=0, column=0, columnspan=10, pady=(0, 10))

        #Celsius to Fahrenheit converter
        self.input_field_c = ttk.Entry(self.mainframe, justify='center', width=10)
        self.input_field_c.grid(row=1, column=0, padx=(30,0))
        
        self.celsius = ttk.Label(self.mainframe, text='C°')
        self.celsius.grid(row=1, column=1)

        convert_c_button = ttk.Button(self.mainframe, text='Convert', command=self.c_to_f_convert)
        convert_c_button.grid(row=1, column=2)

        self.output_field_f = ttk.Label(self.mainframe, borderwidth=1, relief='solid', anchor='center', width=10)
        self.output_field_f.grid(row=2, column=0, padx=(30,0), pady=(10,0))

        self.celsius = ttk.Label(self.mainframe, text='°F')
        self.celsius.grid(row=2, column=1)

        #Fahrenheit to Celsius converter
        self.input_field_f = ttk.Entry(self.mainframe, justify='center', width=10)
        self.input_field_f.grid(row=1, column=3, padx=(30, 0))

        self.farenheit = ttk.Label(self.mainframe, text='°F')
        self.farenheit.grid(row=1, column=4)

        convert_f_button = ttk.Button(self.mainframe, text='Convert', command=self.f_to_c_convert)
        convert_f_button.grid(row=1, column=5)

        self.output_field_c = ttk.Label(self.mainframe, borderwidth=1, relief='solid', width=10, anchor='center')
        self.output_field_c.grid(row=2, column=3, padx=(30,0), pady=(10, 0))

        self.celsius = ttk.Label(self.mainframe, text='C°')
        self.celsius.grid(row=2, column=4)

        #Convert by choosing the unit
        temp = ['C°', '°F']

        self.temp_unit_input = ttk.Entry(self.mainframe, width=10)
        self.temp_unit_input.grid(row=1, column=7, padx=(30, 0))

        self.temp_unit = ttk.Combobox(self.mainframe, values=['C°', '°F'], width=3)
        self.temp_unit.current(0)
        self.temp_unit.grid(row=1, column=8)

        convert_button = ttk.Button(self.mainframe, text='Convert', command=self.convert)
        convert_button.grid(row=1, column=9)

        self.output = ttk.Label(self.mainframe, width=10, borderwidth=1, relief='solid', anchor='center')
        self.output.grid(row=2, column=7, padx=(30, 0))

        self.root.mainloop()
        return
    
    def c_to_f_convert(self):
        celsius = float(self.input_field_c.get())
        self.output_field_f.config(text= '{:.1f}' .format(celsius * 1.8 + 32))

    def f_to_c_convert(self):
        fahrenheit = float(self.input_field_f.get())
        self.output_field_c.config(text= '{:.3f}' .format((fahrenheit - 32) / 1.8) )

    def convert(self):
        converted = float(self.temp_unit_input.get())
        if self.temp_unit.get() == 'C°':
            self.output.config(text= '{:.1f} °F' .format(converted * 1.8 + 32))
        elif self.temp_unit.get() == '°F':
            self.output.config(text= '{:.3f} C°' .format((converted - 32) / 1.8) )

        
if __name__ == '__main__':
    App()