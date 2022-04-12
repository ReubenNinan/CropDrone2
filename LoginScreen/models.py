# from django.db import models
# from django.contrib.auth.models import User, auth

# class GPSData(models.Model):
#     user_name = models.CharField(max_length=100)
#     plant_name = models.CharField(max_length=100)
#     plant_id = models.IntegerField()
#     date = models.CharField(max_length=100)
#     time = models.CharField(max_length=100)
#     X_Coords = models.DecimalField(max_digits=9, decimal_places=6)
#     Y_Coords = models.DecimalField(max_digits=9, decimal_places=6)
#     img = models.ImageField(upload_to = 'DB Pictures')
#     # desc = models.TextField(null = True),

from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User


class ImageData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True, blank=True, max_length=200)
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='DB Pictures')
    fileupload = models.FileField(null=True, upload_to='CSV Files')

    @property
    def file_download_path(self):
        return str((self.fileupload.path)+".csv")


    # category = models.ForeignKey(ImageData, null=True, blank=True, on_delete=models.CASCADE)

    # insert way to have user specific .csv link

#! class Category(models.Model):
#!     title = models.CharField(null=True, blank=True, max_length=200)

    # #Utility Variable
    # uniqueId = models.CharField(null=True,   blank=True, max_length=100)
    # slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return '{} {}'.format(self.title, self.uniqueId)

    # def get_absolute_url(self):
    #     return reverse('category-detail', kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):
    #     if self.date_created is None:
    #         self.date_created = timezone.localtime(timezone.now())
    #     if self.uniqueId is None:
    #         self.uniqueId = str(uuid4()).split('-')[4]
    #         self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

    #     self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
    #     self.last_updated = timezone.localtime(timezone.now())
    #     super(Category, self).save(*args, **kwargs)


#!class Image(models.Model):
    #!description = models.TextField(null=True, blank=True)
    #!altText = models.TextField(null=True, blank=True)

    # hashtags = models.CharField(null=True, blank=True, max_length=300)

    # ImageFields
    #!squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='DB Pictures')
    # landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    # tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='tall')

    # Related Fields
    #!category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    # Utility Variable
    # uniqueId = models.CharField(null=True, blank=True, max_length=100)
    # slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    # date_created = models.DateTimeField(blank=True, null=True)
    # last_updated = models.DateTimeField(blank=True, null=True)

    # def __str__(self):
    #     return '{} {}'.format(self.category.title, self.uniqueId)

    # def get_absolute_url(self):
    #     return reverse('image-detail', kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):
    #     if self.date_created is None:
    #         self.date_created = timezone.localtime(timezone.now())
    #     if self.uniqueId is None:
    #         self.uniqueId = str(uuid4()).split('-')[4]
    #         self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))

    #     self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))
    #     self.last_updated = timezone.localtime(timezone.now())
    #     super(Image, self).save(*args, **kwargs)
