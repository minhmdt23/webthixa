from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Conference(models.Model):
    name = models.CharField(max_length=512)
    date = models.DateField()
    status = models.BooleanField()
    def date_fomat_d_m_y(self):
        return self.date.strftime("%d/%m/%Y")

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.name

class Nameplate(models.Model):
    name = models.CharField(max_length=512)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

class Element(models.Model):
    nameplate = models.ForeignKey(Nameplate, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.nameplate.name + " - " + self.category.name

