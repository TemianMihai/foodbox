from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import uuid


class Packs(models.Model):
    name = models.CharField(null=True, max_length=20)
    slug = models.SlugField(default=uuid.uuid1, unique=True)
    description = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to='images',
                              null=True, blank=True)
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', args=[self.slug])
