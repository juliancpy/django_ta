from django.db import models

class Post(models.Model):
    guid = models.CharField(blank=True, max_length=100)
    title = models.CharField(blank=True, max_length=100)
    date = models.CharField(blank=True, max_length=100)
    url = models.CharField(blank=True, max_length=255)
    content = models.TextField(blank=False)
    TYPE_CHOICES = ((1, 'Yes'), (0, 'No'), (2, 'None'))
    isAEs_choices = models.SmallIntegerField(
        choices=TYPE_CHOICES, default=2, help_text='Adverse Envent Select',verbose_name='Adverse Event',)
    class Meta:
        verbose_name_plural = 'Posts'
        unique_together = ('id', 'guid')    
        ordering = ('title',)        

    def __unicode__(self):
        return self.title


class MedicalTerm(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    ngram = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    cui = models.CharField(max_length=20)
    similarity = models.FloatField(default=None)
    semtype = models.CharField(max_length=5)
    preferred = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.ngram

    class Meta:
        ordering = ('ngram',)
        verbose_name_plural = 'Medical Terminologies'

    def __unicode__(self):
        return self.ngram