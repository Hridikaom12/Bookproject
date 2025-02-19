# models.py
from django.db import models
from bookapp.models import Book
from bookapp.models import Author
from authapp.models import UserProfile
from django.contrib.auth.models import User



class Cart(models.Model):
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)



class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
