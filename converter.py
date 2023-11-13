import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x150')
        self.root.title('Temperature converter')
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand='true')
        
        self.text = ttk.Label(self.mainframe, text='Üdv Koma!', font=("Fira Code Medium", 20), justify='center')
        self.text.grid(row=0, column=0, columnspan=6, pady=(0, 10))

        #Celsius to Farenheit converter
        self.input_field_c = ttk.Entry(self.mainframe, justify='center', width=10)
        self.input_field_c.grid(row=1, column=0, padx=(30,0))
        
        self.celsius = ttk.Label(self.mainframe, text='C°')
        self.celsius.grid(row=1, column=1)

        convert_c_button = ttk.Button(self.mainframe, text='C°to °F', command=self.c_to_f_convert)
        convert_c_button.grid(row=1, column=2)

        self.output_field_f = ttk.Label(self.mainframe, borderwidth=1, relief='solid', anchor='center')
        self.output_field_f.grid(row=2, column=0, sticky='NWES', padx=(30,0), pady=(10,0))

        self.celsius = ttk.Label(self.mainframe, text='°F')
        self.celsius.grid(row=2, column=1)

        #Farenheit to Celsius converter
        self.input_field_f = ttk.Entry(self.mainframe, justify='center', width=10)
        self.input_field_f.grid(row=1, column=3, padx=(30, 0))

        self.farenheit = ttk.Label(self.mainframe, text='°F')
        self.farenheit.grid(row=1, column=4)

        convert_f_button = ttk.Button(self.mainframe, text='°F to C°', command=self.f_to_c_convert)
        convert_f_button.grid(row=1, column=5)

        self.output_field_c = ttk.Label(self.mainframe, borderwidth=1, relief='solid', width=10, anchor='center')
        self.output_field_c.grid(row=2, column=3, padx=(30,0), pady=(10, 0))

        self.celsius = ttk.Label(self.mainframe, text='C°')
        self.celsius.grid(row=2, column=4)


        self.root.mainloop()
        return
    
    def c_to_f_convert(self):
        celsius = float(self.input_field_c.get())
        self.output_field_f.config(text= '{:.1f}' .format(celsius * 1.8 + 32))

    def f_to_c_convert(self):
        farenheit = float(self.input_field_f.get())
        self.output_field_c.config(text= '{:.3f}' .format((farenheit - 32) / 1.8) )


if __name__ == '__main__':
    App()