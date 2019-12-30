
import connexion

import accueil

#fAccueil=ajouterBudget.fenetreAjouterBudget()

fConnexion=connexion.fenetreConnexion()
if fConnexion.closed :
    fAccueil=accueil.fenetreAccueil(fConnexion.user)

