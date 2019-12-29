import tkinter as tk
from tkinter import messagebox
import operationBD as bd
import tkinter.font as tkFont

class fenetreStatisques:
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

    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("800x400")
        self.master.title("projetPython | Gestion des depenses |Statisques")

        frameEnTete= tk.Frame(self.master)
        frameContainer = tk.Frame(self.master)

        frameEnTete.pack()
        frameContainer.pack()

        tk.Label(frameEnTete, text="STATISTIQUES" , font="calibri 18 bold").grid(row=0)


        #frameContainer.grid(row=0,column=0)
        f1 = tk.Frame(frameContainer,width=200,height=200, bg="yellow", highlightthickness=2,highlightbackground="black")#etat actuel de budget
        f2 = tk.Frame(frameContainer,width=200,height=200, bg="red", highlightthickness=2,highlightbackground="black") #sortant
        f3 = tk.Frame(frameContainer,width=200,height=200, bg="green", highlightthickness=2,highlightbackground="black")#entrant
        f4 = tk.Frame(frameContainer,width=200,height=200, bg="orange", highlightthickness=2,highlightbackground="black")#list out
        f5 = tk.Frame(frameContainer,width=200,height=200, bg="orange", highlightthickness=2,highlightbackground="black")#list in



        f1.grid(row=0, column=0,padx=10,pady=10)
        f2.grid(row=0, column=1,padx=10,pady=10)
        f3.grid(row=0, column=2,padx=10,pady=10)
        f4.grid(row=1, column=0,padx=10,pady=10)
        f5.grid(row=1, column=1,padx=10,pady=10)

        f1.grid_propagate(0)
        f2.grid_propagate(0)
        f3.grid_propagate(0)
        f4.grid_propagate(0)
        f5.grid_propagate(0)

        fontStyleTitreObject="calibri 20"
        fontStyleMonyObject="casandra 30 bold"
        valeurEtatBudget = tk.Label(f1, text="{} Dh".format(bd.valeurEtatActuelBudget()), bg="yellow", font=fontStyleMonyObject)
        titreEtatBudget =tk.Label(f1,text="porte monnaie", bg="yellow", font=fontStyleTitreObject)

        valeurSommeSortant = tk.Label(f2, text="{} Dh".format(bd.sommeDepense("out")), bg="red", font=fontStyleMonyObject)
        titreSommeSortant = tk.Label(f2, text="sortant", bg="red",font=fontStyleTitreObject)

        valeurSommeEntrant = tk.Label(f3, text="{} Dh".format(bd.sommeDepense("in")),bg="green", font=fontStyleMonyObject)
        titrerSommeEntrant = tk.Label(f3, text="entrant", font=fontStyleTitreObject,bg="green")

        titreEtatBudget.grid(row=1, column=1,sticky=tk.W)
        valeurEtatBudget.grid(row=0,column=1,sticky=tk.W)
        titreSommeSortant.grid(row=1,column=1,sticky=tk.W)
        valeurSommeSortant.grid(row=0,column=1,sticky=tk.W)
        titrerSommeEntrant.grid(row=1,column=1,sticky=tk.W)
        valeurSommeEntrant.grid(row=0,column=1,sticky=tk.W)

        listeInTitreFrame=tk.Frame(f4)
        listeInTitreFrame.grid(row=0,column=0)
        listeInTitreLabel=tk.Label(listeInTitreFrame, text="REVENUES PAR CATEGORIE",width=21, bg="white", font="calibri 13 bold")
        listeInTitreLabel.grid(row=0,column=0,sticky=tk.W)

        listeOutTitreFrame = tk.Frame(f5)
        listeOutTitreFrame.grid(row=0, column=0)
        listeOutTitreLabel = tk.Label(listeOutTitreFrame, text="DEPENSES PAR CATEGORIE", width=21, bg="white", font="calibri 13 bold")
        listeOutTitreLabel.grid(row=0, column=0, sticky=tk.W)

        lesTypeParCategorieIn= bd.lesTypeParCategorie("in")
        listeLigneIn={}
        listeInLigneLabel={}
        listeInLigneLabelValue={}
        for i in range(0, len(lesTypeParCategorieIn)):
            color="gold"
            if i%2==0:
                color="gold"
            else:
                color="orange red"
            listeLigneIn[i]=tk.Frame(f4)
            listeLigneIn[i].grid(row=i+1, column=0)
            listeInLigneLabel[0] = tk.Label(listeLigneIn[i], text="{}".format(lesTypeParCategorieIn[i]['categorie']),width=13, bg=color,font="calibri 9")
            listeInLigneLabelValue[0] = tk.Label(listeLigneIn[i], text="{}".format(lesTypeParCategorieIn[i]['montant']),width=17, bg=color,font="calibri 9 bold")
            listeInLigneLabel[0].grid(row=i, column=0, sticky=tk.W)
            listeInLigneLabelValue[0].grid(row=i, column=1, sticky=tk.W)

        lesTypeParCategorieOut = bd.lesTypeParCategorie("out")
        listeLigneOut = {}
        listeOutLigneLabel = {}
        listeOutLigneLabelValue = {}
        for i in range(0, len(lesTypeParCategorieOut)):
            color = "gold"
            if i % 2 == 0:
                color = "gold"
            else:
                color = "orange red"
            listeLigneOut[i] = tk.Frame(f5)
            listeLigneOut[i].grid(row=i + 1, column=0)
            listeOutLigneLabel[0] = tk.Label(listeLigneOut[i], text="{}".format(lesTypeParCategorieOut[i]['categorie']),
                                            width=13, bg=color, font="calibri 9")
            listeOutLigneLabelValue[0] = tk.Label(listeLigneOut[i], text="{}".format(lesTypeParCategorieOut[i]['montant']),
                                                 width=17, bg=color, font="calibri 9 bold")
            listeOutLigneLabel[0].grid(row=i, column=0, sticky=tk.W)
            listeOutLigneLabelValue[0].grid(row=i, column=1, sticky=tk.W)

        tk.mainloop()
