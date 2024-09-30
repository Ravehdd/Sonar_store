from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=255)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="photos/", null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Description(models.Model):
    device = models.ForeignKey("Device", on_delete=models.PROTECT)
    description_paragraph = models.TextField()


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class SelectedCard(models.Model):
    card_id = models.IntegerField(max_length=255)





