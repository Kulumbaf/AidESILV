# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:20:59 2020

@author: pierr
"""
import csv
#methode serialiser,deserialiser
def writecsv(fichier):
    
    
def readcsv(fichier):
    
class Compte:
    def __init__(self,idCompte,nom,mail,password,telephone,adresse,ville):
        self.idCompte=idCompte
        self.nom=nom
        self.mail=mail
        self.password=password
        self.telephone=telephone
        self.adresse=adresse
        self.ville=ville
        
    def __getitem__(self,indice):
        reponse=None
        assert indice in range(7)
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
        
        
    def __setitem__(self,indice,valeur):
        assert indice in range(7)
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
            
            
if __name__ == '__main__':
    

    