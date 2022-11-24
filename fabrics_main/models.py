from django.db import models
# from django.db.backends.sqlite3. import



# Navabr uchun Menyu Kategoriya modeli
class MenuCategoriy(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='menucategory')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Menyu Kategoriya"


# Categoriya va Parent uchun Model
class Caregoriy(models.Model):
    menucategoriy = models.ForeignKey(MenuCategoriy, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('Caregoriy', on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=80)
    # path = models.

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Kategoriya'



# def make_tree(categories, parent_id, child=None):
#     for category in categories:
#         if category.parent_id == parent_id:
#             item = {"name": category.name, "child": []}
#             child.append(item)
#             make_tree(categories, category.id, item["child"])
#
# root = {"name": "root", "child": []}
# make_tree(Category.objects.all(), None, root["child"])