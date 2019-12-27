import tkinter as tk
import operationBD as bd

class fenetreConnexion:
    def connecter(self):
        print("First Name: %s\nLast Name: %s" % (self.e1.get(), self.e2.get()))
        if bd.verifierUser(self.e1.get(), self.e2.get()) :
            print("fenetreConnexion.message.Con: SUC")
        else:
            print("fenetreConnexion.message.Con: ERR")
            self.labelText.set("ERR: nom ou mot de passe incorrect")


    def __init__(self):
        master = tk.Tk()
        master.resizable(False, False)
        master.title("projetPython | Gestion des depenses | Connexion")
        master.geometry("500x300")

        canvas = tk.Canvas(master, width=100, height=100)
        canvas.pack()
        my_image = tk.PhotoImage(file="media/userLogo.png")
        canvas.create_image(9, 0, anchor=tk.NW, image=my_image)

        f = tk.Frame(master, height=300, width=300)
        f.pack_propagate(0)  # don't shrink
        f.pack()

        tk.Label(f, text="Nom", width=15).grid(row=0, column=0)
        tk.Label(f, text="Mot de passe", width=15).grid(row=1, column=0)

        self.e1 = tk.Entry(f)
        self.e2 = tk.Entry(f)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        self.b1=tk.Button(f, text='connecter', width=10, bg="green",command=self.connecter).grid(row=2, column=1, sticky=tk.W, pady=4)

        self.b2=tk.Button(f, text='sortir', width=10, command=f.quit).grid(row=3, column=1, sticky=tk.W, pady=4)

        footer = tk.Frame(master, height=300, width=300)
        footer.pack_propagate(0)  # don't shrink
        footer.pack()

        self.labelText = tk.StringVar()
        self.message = tk.Label(footer, textvariable=self.labelText, fg="red", ).grid(row=5)

        tk.mainloop()
