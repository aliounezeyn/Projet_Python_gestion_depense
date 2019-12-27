import tkinter as tk
from tkinter import filedialog, Text
import operationBD as db


resultat= db.selectOneRow("user","id_user","15")
print(resultat)
print(resultat['id_user'])

resultat_de_la_connexion = db.verifierUser("Mohamed","ghS")
print("resultat de la connexion: ", resultat_de_la_connexion)




fenetre = tk.Tk()
fenetre.title("projetPython")
label = tk.Label(fenetre, text="Hello World" )
label1 = tk.Label(fenetre, text="C\'est notre premeier programme avec tikinter" )
label.pack()
label1.pack()

fenetre.mainloop()