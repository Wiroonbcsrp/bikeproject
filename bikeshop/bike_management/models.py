from django.db import models



# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    publish_date = models.DateTimeField('date published')
    category = models.ManyToManyField(Category)
    detail = models.CharField(max_length=255)
    images = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name



    # self เหมือน this ใน java คือ_object ของตัวเอง
    # __str__เหมือนฟังก์ชัน toString()ใน java
