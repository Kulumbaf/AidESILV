# Generated by Django 2.2.12 on 2020-05-14 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='pseudonyme')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name="date d'inscription")),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='dernière connexion')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('prenom', models.CharField(default='', max_length=30)),
                ('nom', models.CharField(default='', max_length=50)),
                ('code_postal', models.IntegerField(default=0)),
                ('ville', models.CharField(default='', max_length=80)),
                ('num_rue', models.IntegerField(default=0, verbose_name='numéro')),
                ('nom_rue', models.CharField(default='', max_length=100)),
                ('tel', models.CharField(default='', max_length=10, verbose_name='numéro de téléphone')),
                ('foyer', models.IntegerField(default=0, verbose_name='nombre de personne dans le foyer')),
                ('bebes', models.IntegerField(default=0, verbose_name="nombre d'enfants de moin de 4 ans")),
                ('stripe_id', models.CharField(blank=True, max_length=200, null=True)),
                ('ebooks', models.ManyToManyField(blank=True, to='products.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
