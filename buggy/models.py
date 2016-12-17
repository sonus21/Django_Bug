from django.contrib.auth.models import User
from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
    header = models.TextField(db_index=True)
    score  = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        max_width = 100
        if len(self.header) >  max_width:
            return "%s...[Score: %s ]" % (self.header[:max_width-3], self.score)
        return "%s [Score: %s ]" % (self.header, self.score)


@python_2_unicode_compatible
class Explanation(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField()
    past_explanation = models.ForeignKey('self', on_delete=models.CASCADE,
                                         db_constraint=False, blank=True,
                                         default=-1, null=True)
    def __str__(self):
        return str(self.description[:40])
