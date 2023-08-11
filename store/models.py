from django.db import models

# Create your models here.
class Product(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='store/img', default='store/img/default_image.jpg', null=True)

    def __str__(self):
        return self.titulo