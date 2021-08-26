from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date

class MyModelManager(models.Manager):
    def get_queryset(self):
        return super(MyModelManager, self).get_queryset().filter(active=True)

class Question(models.Model):
    created = models.DateField('Creada', auto_now_add=True)
    author = models.ForeignKey(get_user_model(), related_name="questions", verbose_name='Pregunta',
                               on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descripción')
    # TODO: Quisieramos tener un ranking de la pregunta, con likes y dislikes dados por los usuarios.
    # added:
    # Cuando en las respuestas ocurre un INSERT o UPDATE, se genera el CAlculo del Rating.
    ranking = models.PositiveIntegerField("Puntos", default=0)
    active = models.BooleanField(default=True)    

    def get_absolute_url(self):
        return reverse('survey:question-edit', args=[self.pk])

    '''
    def calculate_score(self):
        # Not used, Logic in DataBase
        today = date.today()
        score = 0
        if (self.created - today).days == 0: # remaining_days
            score = score + 10
        question = Question.objects.get(self.pk)
        answers = question.answers.all()
        print(len(answers))
        print("answers:",answers)
        for answer in answers:
            score = score + (10 + 5*answer.like - 3*answer.dislike)
        return score
    '''    

    objects = MyModelManager()

    class Meta:
    	ordering = ['-ranking']


class Answer(models.Model):
    ANSWERS_VALUES = ((0,'Sin Responder'),
                      (1,'Muy Bajo'),
                      (2,'Bajo'),
                      (3,'Regular'),
                      (4,'Alto'),
                      (5,'Muy Alto'),)

    question = models.ForeignKey(Question, related_name="answers", verbose_name='Pregunta', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name="answers", verbose_name='Autor', on_delete=models.CASCADE)
    value = models.PositiveIntegerField("Respuesta", default=0)
    comment = models.TextField("Comentario", default="", blank=True)
    # added:
    like = models.PositiveIntegerField("Like", default=0)
    dislike = models.PositiveIntegerField("Disike", default=0)


class Point(models.Model):
    question_id = models.PositiveIntegerField("question_id", default=0)
    score = models.PositiveIntegerField("score", default=0)