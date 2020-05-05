from django.shortcuts import render

def index(requete):
    return render(requete, 'accueil/index.html')
