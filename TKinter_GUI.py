import tkinter as tk

class Button:
    def __init__(self, root):
        self.root = root
        self.klicks = 0
        
        def klick():
            
            self.klicks +=1
            self.label.config(text=f"Button {self.klicks} geklickt")
            if self.klicks == 1000:
                print("BOOM!")

        self.label = tk.Label(root, text = "Servus!")
        self.label.pack()
        
        self.button = tk.Button(root, text="Klick mich!", command=klick)
        self.button.pack(pady=10)

        
    
root = tk.Tk()
root.title("Button")
gui = Button(root)
root.mainloop()