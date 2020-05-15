from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from products.models import Product

from django.conf import settings

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, prenom, nom, code_postal, ville, nom_rue, foyer, bebes, password):
        if not email:
            raise ValueError("Une adresse mail est requise")
        if not username:
            raise ValueError("Un pseudonyme est requis")
        if not prenom:
            raise ValueError("Un prénom est requis")
        if not nom:
            raise ValueError("Un nom de famille est requis")
        if not code_postal:
            raise ValueError("Le code postal du lieu d'habitation est requis")
        if not ville:
            raise ValueError("La ville d'habitation est requise")
        if not nom_rue:
            raise ValueError("Le lieu exacte d'habitation est requis")
        if not foyer:
            raise ValueError("Le nombre de membre du foyer est requis")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password,
            prenom = prenom,
            nom = nom,
            code_postal = code_postal,
            ville = ville,
            nom_rue = nom_rue,
            foyer = foyer,
            bebes = bebes,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, prenom, nom, code_postal, ville, nom_rue, foyer, bebes, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            prenom = prenom,
            nom = nom,
            code_postal = code_postal,
            ville = ville,
            nom_rue = nom_rue,
            foyer = foyer,
            bebes = bebes,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser):
    REQUIRED_FIELDS = ('user','email')
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(verbose_name="pseudonyme", max_length=15, unique=True)
    date_joined = models.DateTimeField(verbose_name="date d'inscription", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="dernière connexion", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    prenom = models.CharField(max_length=30, default='')
    nom = models.CharField(max_length=50, default='')
    code_postal = models.IntegerField(default=0)
    ville = models.CharField(max_length=80, default='')
    num_rue = models.IntegerField(verbose_name="numéro", default=0)
    nom_rue = models.CharField(max_length=100, default='')
    tel = models.CharField(verbose_name="numéro de téléphone", max_length=10, default='')
    foyer = models.IntegerField(verbose_name="nombre de personne dans le foyer", default=0)
    bebes = models.IntegerField(verbose_name="nombre d'enfants de moin de 4 ans", default=0)
    ebooks = models.ManyToManyField(Product, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'prenom', 'nom', 'code_postal', 'ville', 'nom_rue', 'foyer', 'bebes',)

    objects = MyAccountManager()

    def __str__(self):
        return self.username + " | " + self.email + " | " + " ".join([self.prenom, self.nom])

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True