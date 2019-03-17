import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_weight = tk.Entry(self)
        self.input_weight.pack()

        self.input_height = tk.Entry(self)
        self.input_height.pack()

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Berechnen"
        self.hi_there["command"] = self.calculate
        self.hi_there.pack(side="top")

        self.output = tk.Label(self)
        self.output["text"] = "Bitte Gewicht und Körpergrüße eingeben und auf Berechnen klicken"
        self.output.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def calculate(self):
        weight=float(self.input_weight.get())
        height=float(self.input_height.get())
        
        if height > 3: 
            height=height /100

        bmi=weight/(height*height)
        bmi=round(number=bmi, ndigits=0)
        self.output["text"] = int(bmi)
        if bmi <=24:
            self.output.configure(background='green')
        else:
            self.output.configure(background='red')

root = tk.Tk()
app = Application(master=root)
app.mainloop()