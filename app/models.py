from django.db import models

class Imagem(models.Model):
    id = models.BigAutoField(primary_key=True)  # Definindo a chave primária explicitamente
    nome = models.CharField(max_length=100)
    # imagem = models.ImageField(upload_to='imagens/')
    
    def __str__(self):
        return self.nome

class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)  # Definindo a chave primária explicitamente
    name = models.CharField(max_length=200) 
    price = models.IntegerField(null=False) 
    image = models.ImageField(upload_to='media/cardapio_images/', null=True, blank=True)
    menu_item_description = models.TextField(max_length=1000, default='') 

    def __str__(self):
        return self.name
  
class Booking(models.Model):
    id = models.BigAutoField(primary_key=True)  # Definindo a chave primária explicitamente
    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name