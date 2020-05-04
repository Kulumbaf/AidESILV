# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:20:59 2020

@author: pierr
"""
import pandas
import pickle
    
    
def inscription():
    
    idCompte=str(Compte.compteur)
    compteur = Compte.compteur
    nom=input("Saisissez votre nom: ")
    mail=input("Saisissez votre adresse mail: ")
    password=input("Veuillez créer un mot de passe: ")
    adresse=input("Saisissez votre adresse: ")
    telephone = input("Saisissez votre numéro de téléphone: ")
    ville=input("Saisissez le nom de votre ville: ")
    numSS =input("Veuillez entrer votre numéro de sécurité sociale: ")
    return Compte(idCompte,nom,mail,password,telephone,adresse,ville,numSS,compteur)

def creationframe():
    serialisable = inscription()
    data = [[serialisable[i] for i in range(8)]]
    colonne = ["idCompte","nom","mail","password","telephone","adresse","ville","numSS"]
    data = creationframe()
    dataFrame = pandas.DataFrame(data,columns = colonne)
    return dataFrame

def serialisation(dataFrame,colonne):
    dataFrame = addCompteFrame(dataFrame,colonne)
    with open("demandeurs.dat",'wb') as f:
        pickle.dump(dataFrame,f)

def addCompteFrame(dataFrame,colonne):
    reponse =input("tapez oui si vous souhaitez ajouter un compte")
    while reponse == "oui":
        donnee = creationframe()
        df2=pandas.DataFrame(donnee,columns = colonne)
        dataFrame = dataFrame.append(df2)
        reponse = input("tapez oui pour ajouter un autre compte")
    return dataFrame
    
    
   
def deserialisation():
    with open("demandeurs.dat",'rb') as f:
        pickle.load(f)
        
class Compte:    
    compteur=0
    def __init__(self,idCompte,nom,mail,password,telephone,adresse,ville,numSS,compteur):
        self.idCompte=idCompte
        self.nom=nom
        self.mail=mail
        self.password=password
        self.telephone=telephone
        self.adresse=adresse
        self.ville=ville
        self.numSS = numSS
        compteur+=1
        
    def __getitem__(self,indice):
        reponse=None
        assert indice in range(8)
        if indice == 0:
            reponse = self.idCompte
        elif indice == 1:
            reponse = self.nom
        elif indice == 2:
            reponse = self.mail
        elif indice == 3:            
            reponse = self.password
        elif indice == 4:            
            reponse = self.telephone
        elif indice == 5:            
            reponse = self.adresse
        elif indice == 6:
            reponse = self.ville
        elif indice == 7:
            reponse = self.numSS
        return reponse
        
        
    def __setitem__(self,indice,valeur):
        assert indice in range(8)
        if indice == 0:
            self.idCompte=valeur
        elif indice == 1:
            self.nom=valeur
        elif indice == 2:
            self.mail=valeur
        elif indice == 3:            
            self.password=valeur
        elif indice == 4:            
            self.telephone=valeur
        elif indice == 5:            
            self.adresse=valeur
        elif indice == 6:
            self.ville=valeur
        elif indice == 7:
            self.numSS = valeur
            
            
if __name__ == '__main__':
    serialisation()
    deserialisation()
    

    