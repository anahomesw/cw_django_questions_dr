from django.test import TestCase

from models import Question
from models import Answer

# Create your tests here.
class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(title='Q10', description='D10',author =1)
        Answer.objects.create(question=1, comment='C10', author =1, like=2, dislike=1)

    def test_question(self):
        question=Question.objects.get(id=1)
        field_label = question._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

        answer=Answer.objects.get(id=1)
        field_label = answer._meta.get_field('comment').verbose_name
        self.assertEquals(field_label,'comment')

    # must be Enabled database access in tests, to test database with Triggers.