from django.db import models
# from django.db.backends.sqlite3. import
from user_account.models import User

# Navabr uchun Menyu Kategoriya modeli
class MenuCategory(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='menucategory')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menyu Kategoriya"


# Categoriya  uchun Model
class Caregory(models.Model):
    menucategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=80)
    # path = models.

    def __str__(self):
        return self.menucategory.name + " -- " + self.name

    class Meta:
        verbose_name = 'Kategoriya'


class SubCategory(models.Model):
    category = models.ForeignKey(Caregory, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.category.menucategory.name + ' -- ' + self.category.name + ' -- ' + self.name


# To'plam uchun model
class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "To'plam"

# Brendlar uchun model
class Brand(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brendlar"


# Maxsulotlar uchun model
class Product(models.Model):
    menucategoriy = models.ForeignKey(MenuCategory, on_delete=models.RESTRICT, blank=True, null=True)
    categories = models.ForeignKey(Caregory, on_delete=models.RESTRICT, blank=True, null=True)
    subcategories = models.ForeignKey(SubCategory, on_delete=models.RESTRICT, blank=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.RESTRICT, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name="Maxsulot nomi")
    title = models.CharField(max_length=255, verbose_name="Sarlovha")
    subject = models.CharField(max_length=500, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, verbose_name="Ishlab chiqaruvchi")
    vendor_code = models.CharField(max_length=10, verbose_name="Sotuvchi kodi")
    available = models.BooleanField(default=False, verbose_name='Sotuvda bormi')
    price = models.FloatField()
    top = models.BooleanField(default=False, verbose_name="Top productga qo'shish")
    description = models.TextField()
    image = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100

    class Meta:
        verbose_name = 'Maxsulot'

class Delivery(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Delivery"


class Payment(models.Model):
    name = models.CharField(max_length=50)
    icon = models.FileField(upload_to='payment')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Payment"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    payment_type = models.ForeignKey(Payment, on_delete=models.RESTRICT)
    delivery_type = models.ForeignKey(Delivery, on_delete=models.RESTRICT)
    full_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    paid_amount = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Order"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    total_price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order)

    def get_total_price(self):
        return self.total_price / 100

    class Meta:
        verbose_name = "OrderItem"



class Setting(models.Model):
    key = models.CharField(max_length=52, primary_key=True)
    value = models.CharField(max_length=2000)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Setting"






























# def make_tree(categories, parent_id, child=None):
#     for category in categories:
#         if category.parent_id == parent_id:
#             item = {"name": category.name, "child": []}
#             child.append(item)
#             make_tree(categories, category.id, item["child"])
#
# root = {"name": "root", "child": []}
# make_tree(Category.objects.all(), None, root["child"])