from django.db import models
import os
from uuid import uuid4


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class PackageGroup(BaseModel):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    description_ar = models.CharField(max_length=255)
    img = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.name


class Package(BaseModel):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    duration_ar = models.CharField(max_length=255)
    price = models.IntegerField()
    price_ar = models.IntegerField()
    price_usd = models.IntegerField()
    price_usd_ar = models.IntegerField()
    description = models.CharField(max_length=255)
    description_ar = models.CharField(max_length=255)
    package = models.ForeignKey('PackageGroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PackageDetails(BaseModel):
    description = models.CharField(max_length=255)
    description_ar = models.CharField(max_length=255)
    package_details = models.ForeignKey('Package', on_delete=models.CASCADE, related_name='package_details')


class GreatTransformation(BaseModel):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    img = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.name


class GreatTransformationDetails(BaseModel):
    description = models.CharField(max_length=255)
    description_ar = models.CharField(max_length=255)
    trans_details = models.ForeignKey('GreatTransformation', on_delete=models.CASCADE, related_name='trans_details')


class Setting(BaseModel):
    # address = models.CharField(max_length=255)
    # main_mobile_number = models.CharField(max_length=255)
    # secondary_mobile_number = models.CharField(max_length=255)
    # email = models.EmailField()
    about_us = models.TextField(max_length=8000)
    about_us_ar = models.TextField(max_length=8000)

    # about_us_img = CloudinaryField('image')

    def __str__(self):
        return self.about_us


class Slider(BaseModel):
    img = models.ImageField(upload_to=path_and_rename)
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    description_ar = models.CharField(max_length=255)
    setting = models.ForeignKey('Setting', on_delete=models.CASCADE, related_name='slider')


class Transformation(BaseModel):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    title_ar = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    description_ar = models.TextField(max_length=500)
    order = models.IntegerField(unique=True)
    img = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.title


class FoodPackages(BaseModel):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FoodRaw(BaseModel):
    FoodPackages = models.ForeignKey('FoodPackages', on_delete=models.CASCADE, related_name='Food_packages')


class Food(BaseModel):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    food_raw = models.ForeignKey('FoodRaw', on_delete=models.CASCADE, related_name='food_raw')

    def __str__(self):
        return self.name


class CustomEmails(BaseModel):
    trainer_name = models.CharField(max_length=200)
    email = models.TextField(max_length=500)

    def __str__(self):
        return self.trainer_name
