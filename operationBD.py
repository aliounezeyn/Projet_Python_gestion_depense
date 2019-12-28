import pymysql.cursors


def dataBaseConnection():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='gestiondepense',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except :
        print("errreur de connexion a la base")
        exit()


#fonction pour executer les operation: INSET, UPDATE et DELETE
def executerRequete(requete):
    connection=dataBaseConnection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(requete)
        connection.commit()
        print("SUC Req Exec: ",requete)
        return True
    except:
        print("ERR Req Exec, ",requete)
        return False
    finally:
        connection.close()


#fonction pour selectioner une seule ligne d'une table, chemps[param]=valeur
def selectOneRow(table,param,valeur):
    connection=dataBaseConnection()
    sql = "SELECT * FROM {} WHERE {} = %s ".format(table,param)
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (valeur))
            result = cursor.fetchone()
            return result
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

#fonction pour selectioner une seule ligne d'une table, chemps[param]=valeur
def selectAllRows(table,param,valeur):
    connection=dataBaseConnection()
    sql = "SELECT * FROM {} WHERE {} = %s ".format(table,param)
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (valeur))
            result = cursor.fetchall()
            return result
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

#fonction pour selectioner une seule ligne d'une table, chemps[param]=valeur
def selectTable(table):
    connection=dataBaseConnection()
    sql = "SELECT * FROM {} ".format(table)
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

#Operations sur la table BUDGET
#insertion [mise a jour de l'etat du budget]
def insertBudget(montant, date_ajout):
    connection = dataBaseConnection()
    sql = "INSERT INTO budget (montant, date_ajout) VALUES (%s,%s)"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (montant,date_ajout))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()
#update [mise a jour d'un enregistrement budget]
def updateBudget(id_budget, montant, date_ajout):
    connection = dataBaseConnection()
    sql = "UPDATE budget SET montant=%s, date_ajout=%s WHERE id_budget = %s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (montant,date_ajout,id_budget))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

def deleteBudget(id_budget):
    connection = dataBaseConnection()
    sql = "DELETE FROM budget WHERE id_budget = %s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_budget))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

#Operations sur la table DEPENSE
def insertDepense(montant,type,categorie, date_ajout,description):
    connection = dataBaseConnection()
    sql = "INSERT INTO depense (montant,type,categorie, date_ajout,description) VALUES (%s,%s,%s,%s,%s)"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (montant,type,categorie, date_ajout,description))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

def updateDepense(id_depense,montant,type,categorie, date_ajout,description):
    connection = dataBaseConnection()
    sql = "UPDATE depense SET montant=%s, type=%s, categorie=%s, date_ajout=%s, description=%s WHERE id_depense = %s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (montant,type,categorie, date_ajout,description,id_depense))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

def deleteDepense(id_depense):
    connection = dataBaseConnection()
    sql = "DELETE FROM depense WHERE id_depense = %s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_depense))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()




#Operations sur la table user
def insertUser(nom,mot_de_passe):
    connection = dataBaseConnection()
    sql = "INSERT INTO user (nom,mot_de_passe) VALUES (%s,%s)"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (nom,mot_de_passe))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

def updateUser(id_user,nom,mot_de_passe):
    connection = dataBaseConnection()
    sql = "UPDATE user SET nom=%s, mot_de_passe=%s WHERE id_user = %s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (nom,mot_de_passe,id_user))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

def deleteUser(id_user):
    connection = dataBaseConnection()
    sql = "DELETE FROM user WHERE id_user = %s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (id_user))
        connection.commit()
        print("SUC Req Exec: ", sql)
        return True
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()

def verifierUser(nom,mot_de_passe):
    connection = dataBaseConnection()
    sql = "SELECT * FROM user WHERE nom = %s AND mot_de_passe=%s"
    print(sql)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (nom,mot_de_passe))
            result = cursor.fetchone()
            if result == None :
                return False
            else:
                return nom
    except:
        print("erreur selection: ", sql)
        return False
    finally:
        connection.close()