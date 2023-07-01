from django.db import models
import uuid
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


def getFilename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class AbstractBaseModel(models.Model):
    name = models.CharField('Name', max_length=100)
    created = models.DateTimeField('Created',auto_now_add=True)
    updated = models.DateTimeField('Updated',auto_now=True)
    activity = models.BooleanField('Activity', default=True)

    class Meta: 
        abstract = True

class ProductModel(AbstractBaseModel):
    price = models.DecimalField('Price', max_digits=9, decimal_places=2)
    description = models.CharField('Description', max_length=300)
    image = ProcessedImageField(
        upload_to=getFilename,
        processors=[ResizeToFit(width=300, height=300)],
        max_length=1048,
        options={'quality': 90},
        blank=True,
    )
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name
    