import tkinter as tk
from tkinter import messagebox
import operationBD as bd
import tkinter.font as tkFont
import ajouterDepense
import ajouterBudget
import modifierDepense
import statistiques
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
        self.master.title("projetPython | Gestion des depenses | Accueil")

        frameTitrat = tk.Frame(self.master, height=100, width=100)
        frameTitrat.pack()
        frameBouton = tk.Frame(self.master, height=30, width=600)
        frameBouton.pack()

        frameIsolant= tk.Frame(self.master, height=50, width=600)
        frameIsolant.pack()
        tk.Label(frameIsolant, text="Liste des depenses").grid(row=0)

        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.titreKbir=tk.Label(frameTitrat, text="Bienvenue {}".format(user),font=fontStyle)
        self.titreS9ir=tk.Label(frameTitrat, text="Selectionner une operation")

        self.titreKbir.grid(row=0)
        self.titreS9ir.grid(row=1,column=0)

        self.ajouterBouton = tk.Button(frameBouton, text='ajouter depense', width=20, bg="#cccccc", command=self.ajouterDepenseF)
        self.modifierDepenseBouton = tk.Button(frameBouton, text='modifier depense', width=20, bg="#cccccc", command=self.modifierDepenseF,state=tk.DISABLED)
        self.suprimerBouton = tk.Button(frameBouton, text='suprimer depense', width=20, bg="red",fg="white", command=self.suprimerDepense, state=tk.DISABLED)
        self.modifierBudgetBouton = tk.Button(frameBouton, text='modifier le budget', width=20, bg="#cccccc", command=self.modifierBudget)
        self.statistiquesBouton = tk.Button(frameBouton, text='statistiques', width=20, bg="#cccccc", command=self.statistiquesChoix)
        self.actualiserBouton = tk.Button(frameBouton, text='actualiser', width=20, bg="#cccccc", command=self.actualiser)


        budgetActuel=bd.selectEtatActuelBudget()
        print(budgetActuel)
        self.BudgetLabel = tk.Label(frameBouton, text="{} Dh.".format(budgetActuel['valeur']), width=10,height=2, bg="yellow",font='Helvetica 18 bold')

        self.ajouterBouton.grid(row=1, column=2, padx=2)
        self.modifierDepenseBouton.grid(row=1, column=1, padx=2)
        self.suprimerBouton.grid(row=1, column=3, padx=2)
        self.modifierBudgetBouton.grid(row=1, column=4, padx=2)
        self.statistiquesBouton.grid(row=1, column=5, padx=2)
        self.actualiserBouton.grid(row=2, column=3, padx=2)
        self.BudgetLabel.grid(row=3, column=3, padx=2)

        self.charger()

        tk.mainloop()

    def vider(self):
        for frame in self.frameTableDepense:
            self.frameTableDepense[frame].pack_forget()
    
    def charger(self):
        budgetActuel = bd.selectEtatActuelBudget()
        self.BudgetLabel["text"]="{} Dh".format(budgetActuel['valeur'])
        depense = bd.selectTable("depense")
        print(depense)
        self.var = {}
        self.selectBouton = {}
        self.montant = {}
        self.type = {}
        self.categorie = {}
        self.date = {}
        self.description = {}
        self.frameTableDepense = {}
        self.frameTableDepense[0] = tk.Frame(self.master, height=300, width=600, bg="black")
        self.frameTableDepense[0].pack()
        counter = {}
        for i in range(0, len(depense)):
            counter[i] = i
            color = "gray"
            if i % 2 == 0:
                color = "orange"
            self.frameTableDepense[i + 1] = tk.Frame(self.master, height=300, width=600, bg=color)
            self.frameTableDepense[i + 1].pack()
            self.var[i] = tk.StringVar()
            self.selectBouton[i] = tk.Checkbutton(self.frameTableDepense[i + 1], text="", variable=self.var[i],
                                                  onvalue="{}".format(depense[i]['id_depense']),
                                                  command=lambda: self.afficher(), offvalue="")
            self.montant[i] = tk.Label(self.frameTableDepense[i + 1], text="{}".format(depense[i]['montant']), width=10)
            typeAffiche = "entrant"
            colorTypeLabel="green"
            if depense[i]['type'] == "in":
                typeAffiche = "entrant"
            else:
                typeAffiche = "sortant"
                colorTypeLabel = "red"
            self.type[i] = tk.Label(self.frameTableDepense[i + 1], text="{}".format(typeAffiche),bg=colorTypeLabel, width=10)
            self.categorie[i] = tk.Label(self.frameTableDepense[i + 1], text="{}".format(depense[i]['categorie']), width=10)
            self.date[i] = tk.Label(self.frameTableDepense[i + 1], text="{}".format(depense[i]['date_ajout']).split(" ")[0],
                                    width=20)
            self.description[i] = tk.Label(self.frameTableDepense[i + 1], text="{}".format(depense[i]['description']),
                                           width=40)

        tk.Label(self.frameTableDepense[0], text="selection", bg="black", fg="white", width=10).grid(row=0, column=1)
        tk.Label(self.frameTableDepense[0], text="montant", bg="black", fg="white", width=10).grid(row=0, column=2)
        tk.Label(self.frameTableDepense[0], text="type", bg="black", fg="white", width=10).grid(row=0, column=3)
        tk.Label(self.frameTableDepense[0], text="categorie", fg="white", bg="black", width=10).grid(row=0, column=4)
        tk.Label(self.frameTableDepense[0], text="date", bg="black", fg="white", width=20).grid(row=0, column=5)
        tk.Label(self.frameTableDepense[0], text="description", bg="black", fg="white", width=40).grid(row=0, column=6)

        # affichage des composants [checkbox, et label du nom]
        for i in range(0, len(depense)):
            self.selectBouton[i].grid(row=i + 1, column=1, padx=4, pady=2)
            self.montant[i].grid(row=i + 1, column=2, padx=4, pady=2)
            self.type[i].grid(row=i + 1, column=3, padx=4, pady=2)
            self.categorie[i].grid(row=i + 1, column=4, padx=4, pady=2)
            self.date[i].grid(row=i + 1, column=5, padx=4, pady=2)
            self.description[i].grid(row=i + 1, column=6, padx=4, pady=2)

    #chouuuuuuuuv m3a 4e

    def afficher(self):
        counter=0
        resultat=False
        for v in self.var:
            if self.var[v].get():
                #print("v:",v)
                counter+=1
                resultat=self.var[v].get()
            else:
                self.selectBouton[v]['state'] = tk.DISABLED
                #print("not")
        if counter==0:
            for v in self.var:
                self.selectBouton[v]['state'] = tk.NORMAL
                self.suprimerBouton['state'] = tk.DISABLED
                self.modifierDepenseBouton['state'] = tk.DISABLED
        else :
            self.suprimerBouton['state']=tk.NORMAL
            self.modifierDepenseBouton['state'] = tk.NORMAL
        return resultat


    def actualiser(self):
        self.vider()
        self.charger()



    def modifierDepenseF(self):
        id=self.afficher()
        modifierDepense.fenetreModifierDepense(id)
        self.actualiser()
        self.afficher()

    def ajouterDepenseF(self):
        ajouter=ajouterDepense.fenetreAjouterDepense()
        self.actualiser()

    def suprimerDepense(self):
        if self.afficher():
            if messagebox.askokcancel("Confirmation", "Voulez vous vraiment supprimer l'enregistrement?"):
                bd.deleteDepense(self.afficher())
                messagebox.showinfo("Resultat", "l'enregistement est suprimé")
            else:
                messagebox.showinfo("Resultat", "l'operation est annulée")
        self.actualiser()
        self.afficher()

    def modifierBudget(self):
        ajouterBudget.fenetreAjouterBudget()
        self.actualiser()

    def statistiquesChoix(self):
        statistiques.fenetreStatisques()
