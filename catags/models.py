from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class CaTag(models.Model):
    catag_name = models.CharField(max_length=100)
    catag_slug = models.SlugField(max_length=100, verbose_name=_('catag slug'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.catag_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.catag_slug = slugify(self.catag_name)
        super(CaTag, self).save(*args, **kwargs)
