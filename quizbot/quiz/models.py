from django.db import models
# from django.utils.translation import ugettext 

# Create your models here.

class Question(models.Model):

    LEVEL = (
        (0, ('Any')),
        (1, ('Beginner')),
        (2, ('Intermediate')),
        (3, ('Advanced')),
        (4, ('Expert'))
    )
    title = models.CharField(("title"), max_length = 300)
    points = models.SmallIntegerField(("points"))
    difficulty = models.IntegerField(("Difficulty"), choices=LEVEL, default=0)
    is_active = models.BooleanField(("Is Active"), default = True)
    created_at = models.DateTimeField(("Created"), auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(("Updated"), auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name=("Question"), on_delete=models.CASCADE)
    answer = models.TextField(("Answer"), max_length = 500)
    is_correct = models.BooleanField(("Correct Answer"), default = False)
    is_active = models.BooleanField(("Is Active"), default = True)
    created_at = models.DateTimeField(("Created"), auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(("Updated"), auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.answer

