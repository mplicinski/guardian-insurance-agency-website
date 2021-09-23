from django.conf import settings
from django.db import models
from django.db.models import Q, lookups
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


from .utils import slugify_instance_title

#User = settings.AUTH_USER_MODEL

# Create your models here.
class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none() # return Article.objects.none() # [] empty list
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups) # self.get_queryset() makes this reuseable with other models


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)
        

class Article(models.Model):
    '''
    Article
    '''
    user = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=ArticleManager()

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse("articles:update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("articles:delete", kwargs={"slug": self.slug})

    def get_content_preview(self):
        content_preview = f"{self.content[:375]}..."
        return content_preview
    
    # def save(self, request, *args, **kwargs):
    #     self.user = request.user
    #     super().save(*args, **kwargs)
    #     # we could do additional actions

def article_pre_save(sender, instance, *args, **kwargs): # instance is the particular instance of the model (Article) that is currently being sent
    # print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    # print('post_save')
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)