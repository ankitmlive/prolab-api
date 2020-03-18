from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from prolab.utilities import get_unique_slug, get_read_time
from .utils import get_read_time


class ArticleManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ArticleManager, self).filter(draft=False).filter(created_at__lte=timezone.now())

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    #textfield should be used for storing markdown
    content = models.TextField(editable=False)
    draft = models.BooleanField(default=False)
    read_time =  models.IntegerField(default=0)
    is_active = models.BooleanField(default=False, blank=False)
    #catags = models.ManyToManyField('catags.Catag', related_name='articles')
    #author = models.ForeignKey('auth.User', related_name='articles')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    published_at    = models.DateTimeField(auto_now=False, auto_now_add=False)

    objects = ArticleManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def get_api_url(self):
        return reverse("posts-api:detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["-timestamp", "-updated_at"]
    
    def get_markdown(self):
        content = self.content
        return mark_safe(content)

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var
 
pre_save.connect(pre_save_post_receiver, sender=Article)
