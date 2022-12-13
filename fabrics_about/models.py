from django.db import models


# Kompaniya haqida malumotlar modeli
class About(models.Model):
    description = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Kompaniya malumoti"


# Yetkaziberish uchun model
class Delivery(models.Model):
    description = models.TextField()
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Yetkaziberish xizmati'


# Manzil va Kontakt uchun model
class Contact(models.Model):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f"{str(self.phone)} {self.address} {self.email}"

    class Meta:
        verbose_name = 'Kontakt'


#  Sharhlar yozish uchun model
class Comment(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='media/comment/image')
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sayt uchun koment"


# OMMAVIY TAKLIFLAR uchun model
class PublicOffer(models.Model):
    description = models.TextField()

    class Meta:
        verbose_name = "OMMAVIY TAKLIF"


# Zakaz qilish uchun shablon model
class Order(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='shablon_order')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Buyurtam qilish uchun shablon"



# Filiallar uchun model
class Branches(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='braches')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Filiallar"


#  Filiallar uchun Detail model
class BranchDetail(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=500)

    def __str__(self):
        return f"{str(self.phone)} {str(self.address)}"

    class Meta:
        verbose_name = "Filial Tavsifi"


# Blog uchun model
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog')
    content = models.TextField()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Blog"


# BlogDetail uchun model
class BlogDetail(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return str(self.blog)

    class Meta:
        verbose_name = "Blog Tavsifi"
