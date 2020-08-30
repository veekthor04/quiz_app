from django.db import models
from django.template.defaultfilters import truncatechars
from solo.models import SingletonModel

# Create your models here.
class SiteConfiguration(SingletonModel):

    time_minute = models.IntegerField(default=3)
    time_second = models.IntegerField(default=0)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"

class Passage(models.Model):

    passage_text = models.TextField()

    def __str__(self):
        return truncatechars(self.passage_text, 100)

class Question(models.Model):

    passage = models.ForeignKey(Passage, on_delete=models.CASCADE)
    question = models.CharField( max_length=300)
    option1 = models.CharField(max_length=200, help_text="option")
    option2 = models.CharField(max_length=200, help_text="option")
    option3 = models.CharField(max_length=200, help_text="option")
    option4 = models.CharField(max_length=200, help_text="option")

    correct_option = models.CharField(max_length=200, help_text="Note: It should be a duplicate of an option listed above")

    def __str__(self):
        return self.question