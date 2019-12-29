import tkinter as tk
from tkinter import messagebox
import operationBD as bd
import tkinter.font as tkFont
import ajouterDepense
import ajouterBudget
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

        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.titreKbir=tk.Label(frameTitrat, text="Bienvenue {}".format(user),font=fontStyle)
        self.titreS9ir=tk.Label(frameTitrat, text="Selectionner une operation")

        self.titreKbir.grid(row=0)
        self.titreS9ir.grid(row=1,column=0)

        self.ajouterBouton = tk.Button(frameBouton, text='ajouter depense', width=20,  command=self.ajouterDepenseF)
        self.modifierBouton = tk.Button(frameBouton, text='modifier depense', width=20, command=self.modifierDepense)
        self.suprimerBouton = tk.Button(frameBouton, text='suprimer depense', width=20, command=self.suprimerDepense, state=tk.DISABLED)
        self.modifierBudgetBouton = tk.Button(frameBouton, text='modifier le budget', width=20, command=self.modifierBudget)
        self.statistiquesBouton = tk.Button(frameBouton, text='statistiques', width=20, command=self.statistiquesChoix)

        self.ajouterBouton.grid(row=1, column=2, padx=2)
        self.modifierBouton.grid(row=1, column=1, padx=2)
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
        frameTableDepense = {}
        frameTableDepense[0] = tk.Frame(self.master, height=300, width=600, bg="black")
        frameTableDepense[0].pack()
        counter={}
        for i in range(0,len(depense)):
            counter[i]=i
            color="gray"
            if i%2==0:
                color="orange"
            frameTableDepense[i+1] = tk.Frame(self.master, height=300, width=600, bg=color)
            frameTableDepense[i+1].pack()
            self.var[i]=tk.StringVar()
            self.selectBouton[i]=tk.Checkbutton(frameTableDepense[i+1], text="", variable=self.var[i],onvalue="{}".format(depense[i]['id_depense']), command=lambda:self.afficher(),offvalue="")
            self.montant[i] = tk.Label(frameTableDepense[i+1], text="{}".format(depense[i]['montant']),width=10)
            typeAffiche = "entrant"
            if depense[i]['categorie']=="in":
                typeAffiche="entrant"
            else:
                typeAffiche = "sortant"
            self.type[i] = tk.Label(frameTableDepense[i+1], text="{}".format(typeAffiche),width=10)
            self.categorie[i] = tk.Label(frameTableDepense[i+1], text="{}".format(depense[i]['categorie']),width=10)
            self.date[i] = tk.Label(frameTableDepense[i+1], text="{}".format(depense[i]['date_ajout']).split(" ")[0],width=20)
            self.description[i] = tk.Label(frameTableDepense[i+1], text="{}".format(depense[i]['description']),width=40)

        tk.Label(frameTableDepense[0], text="selection",bg="black",fg="white",width=10).grid(row=0,column=1)
        tk.Label(frameTableDepense[0], text="montant",bg="black",fg="white", width=10).grid(row=0,column=2)
        tk.Label(frameTableDepense[0], text="type",bg="black",fg="white", width=10).grid(row=0,column=3)
        tk.Label(frameTableDepense[0], text="categorie",fg="white",bg="black", width=10).grid(row=0,column=4)
        tk.Label(frameTableDepense[0], text="date",bg="black",fg="white", width=20).grid(row=0,column=5)
        tk.Label(frameTableDepense[0], text="description",bg="black",fg="white", width=40).grid(row=0,column=6)

        #affichage des composants [checkbox, et label du nom]
        for i in range(0,len(depense)):
            self.selectBouton[i].grid(row=i+1,column=1,padx=4,pady=2)
            self.montant[i].grid(row=i+1,column=2,padx=4,pady=2)
            self.type[i].grid(row=i+1, column=3, padx=4,pady=2)
            self.categorie[i].grid(row=i+1, column=4, padx=4,pady=2)
            self.date[i].grid(row=i+1, column=5, padx=4,pady=2)
            self.description[i].grid(row=i+1, column=6, padx=4,pady=2)


        tk.mainloop()

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
        else :
            self.suprimerBouton['state']=tk.NORMAL

        return resultat


    def modifierDepense(self):
        print("fonction a preparer")

    def ajouterDepenseF(self):
        ajouter=ajouterDepense.fenetreAjouterDepense()

    def suprimerDepense(self):
        if self.afficher():
            if messagebox.askokcancel("Confirmation", "Voulez vous vraiment supprimer l'enregistrement?"):
                bd.deleteDepense(self.afficher())
                messagebox.showinfo("Resultat", "l'enregistement est suprimé")
            else:
                messagebox.showinfo("Resultat", "l'operation est annulée")



    def modifierBudget(self):
        ajouterBudget.fenetreAjouterBudget()

    def statistiquesChoix(self):
        print("a preparer")
