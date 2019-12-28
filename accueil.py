import tkinter as tk
from tkinter import messagebox
import operationBD as bd
import tkinter.font as tkFont
class fenetreAccueil:

    closed=False

    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __init__(self,user):
        self.master = tk.Tk()
        self.master.geometry("800x400")
        self.master.resizable(False, False)
        self.master.title("projetPython | Gestion des depenses | Accueil")

        frameTitrat = tk.Frame(self.master, height=100, width=100)
        frameTitrat.pack()
        frameBouton = tk.Frame(self.master, height=30, width=600)
        frameBouton.pack()

        frameIsolant= tk.Frame(self.master, height=50, width=600)
        frameIsolant.pack()
        tk.Label(frameIsolant, text="Liste des depenses").grid(row=0)

        frameTableDepense = tk.Frame(self.master, height=300, width=600, bg="white")
        frameTableDepense.pack()

        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.titreKbir=tk.Label(frameTitrat, text="Bienvenue {}".format(user),font=fontStyle)
        self.titreS9ir=tk.Label(frameTitrat, text="Selectionner une operation")

        self.titreKbir.grid(row=0)
        self.titreS9ir.grid(row=1,column=0)

        self.modifierBouton = tk.Button(frameBouton, text='ajouter depense', width=20, command=self.modifierDepense)
        self.ajouterBouton = tk.Button(frameBouton, text='modifier depense', width=20,  command=self.ajouterDepense)
        self.suprimerBouton = tk.Button(frameBouton, text='suprimer depense', width=20, command=self.suprimerDepense)
        self.modifierBudgetBouton = tk.Button(frameBouton, text='modifier le budget', width=20, command=self.modifierBudget)
        self.statistiquesBouton = tk.Button(frameBouton, text='statistiques', width=20, command=self.statistiquesChoix)

        self.modifierBouton.grid(row=1, column=1, padx=2)
        self.ajouterBouton.grid(row=1, column=2, padx=2)
        self.suprimerBouton.grid(row=1, column=3, padx=2)
        self.modifierBudgetBouton.grid(row=1, column=4, padx=2)
        self.statistiquesBouton.grid(row=1, column=5, padx=2)

        depense=bd.selectTable("depense")
        print(depense)
        self.var = {}
        self.selectBouton={}
        self.montant = {}
        self.type = {}
        self.categorie = {}
        self.date = {}
        self.description = {}
        for i in range(0,len(depense)):
            self.var[i]=tk.StringVar()
            self.selectBouton[i]=tk.Checkbutton(frameTableDepense, text="", variable=self.var[i],onvalue="{}".format(depense[i]['id_depense']), offvalue="")
            self.montant[i] = tk.Label(frameTableDepense, text="{}".format(depense[i]['montant']),width=10)
            typeAffiche = "entrant"
            if depense[i]['categorie']=="in":
                typeAffiche="entrant"
            else:
                typeAffiche = "sortant"
            self.type[i] = tk.Label(frameTableDepense, text="{}".format(typeAffiche),width=10)
            self.categorie[i] = tk.Label(frameTableDepense, text="{}".format(depense[i]['categorie']),width=10)
            self.date[i] = tk.Label(frameTableDepense, text="{}".format(depense[i]['date_ajout']),width=20)
            self.description[i] = tk.Label(frameTableDepense, text="{}".format(depense[i]['description']),width=40)

        #affichage des composants [checkbox, et label du nom]
        for i in range(0,len(depense)):
            self.selectBouton[i].grid(row=i,column=1,padx=4,pady=4)
            self.montant[i].grid(row=i,column=2,padx=4,pady=4)
            self.type[i].grid(row=i, column=3, padx=4,pady=4)
            self.categorie[i].grid(row=i, column=4, padx=4,pady=4)
            self.date[i].grid(row=i, column=5, padx=4,pady=4)
            self.description[i].grid(row=i, column=6, padx=4,pady=4)


        tk.mainloop()

    def afficher(self):
        for var in self.var:
            if self.var[var].get():
                print(self.var[var].get())

    def modifierDepense(self):
        print("fonction a preparer")

    def ajouterDepense(self):
        print("fonction a preparer")

    def suprimerDepense(self):
        print("fonction a preparer")

    def modifierBudget(self):
        print("fonction a preparer")

    def statistiquesChoix(self):
        print("fonction a preparer")
