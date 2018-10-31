from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    myfield = MarkdownxField()
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return  self.title
    pass