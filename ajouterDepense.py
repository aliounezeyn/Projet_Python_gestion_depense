import tkinter as tk
from tkinter import messagebox
import operationBD as bd
import tkinter.font as tkFont

class fenetreAjouterDepense:
    def ajouter(self):
        #if bd.verifierUser(self.montantInput.get(), self.dateInput.get()):

        if self.is_number(self.montantInput.get()) :
            if bd.insertDepense(self.montantInput.get(),
                             self.typeInput.get(),
                             self.categorieInput.get(),
                             self.dateInput.get(),
                             self.descriptionInput.get()) :
                messagebox.showinfo("Message | succes de l'operation", "succes de l'operation")
                self.master.quit()
                print("fentreAjouterBudget.message: SUC")
            else:
                print("fenetreAjuterDepense.message: ERR_exec_req")
        else:
            print("fenetreAjuterDepense.message: ERR_valeur_incor")
            messagebox.showerror("Message | Erreur", "valeur incorrecte")


    closed=False

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("800x400")
        self.master.resizable(False, False)
        self.master.title("projetPython | Gestion des depenses | Ajouter Depense")

        f2 = tk.Frame(self.master, height=200, width=100)
        f2.pack()
        f1 = tk.Frame(self.master, height=600, width=600)
        f1.pack()
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.titreLable=tk.Label(f2, text="Ajouter une depense",font=fontStyle).grid(row=0)
        self.titreLable2=tk.Label(f2, text="Saisir les informations").grid(row=1)

        self.montantLabel = tk.Label(f1, text="montant", width=15).grid(row=1, column=1)
        self.typeLabel = tk.Label(f1, text="type", width=15).grid(row=2, column=1)
        self.categorieLabel = tk.Label(f1, text="categorie", width=15).grid(row=3, column=1)
        self.descriptioLabeln = tk.Label(f1, text="description", width=15).grid(row=4, column=1)
        self.dateLabel = tk.Label(f1, text="date", width=15).grid(row=5, column=1)

        self.montantInput = tk.Entry(f1,width=30)
        self.typeInput = tk.Entry(f1, width=30)
        self.categorieInput = tk.Entry(f1, width=30)
        self.descriptionInput = tk.Entry(f1, width=30)
        self.dateInput = tk.Entry(f1, width=30)


        self.montantInput.grid(row=1,column=2)
        self.typeInput.grid(row=2,column=2)
        self.categorieInput.grid(row=3, column=2)
        self.descriptionInput.grid(row=4, column=2)
        self.dateInput.grid(row=5, column=2)

        f3 = tk.Frame(self.master, height=600, width=600)
        f3.pack()
        self.enregistrerBouton = tk.Button(f3, text='Enregistrer', width=10, bg="green", command=self.ajouter).grid(row=2, column=1,
                                                                                                    sticky=tk.W, pady=4)

        #self.retournerBouton = tk.Button(f3, text='Retourner', width=10, command=self.master.quit).grid(row=3, column=1, sticky=tk.W,
        #                                                                               pady=4)
        footer = tk.Frame(self.master, height=300, width=300)
        footer.pack_propagate(0)  # don't shrink
        footer.pack()

        self.labelText = tk.StringVar()
        self.message = tk.Label(footer, textvariable=self.labelText, fg="red", ).grid(row=10)

        tk.mainloop()
