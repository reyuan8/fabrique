from django.db import models
from model_utils.models import TimeStampedModel

from survey.constants import QUESTION_TYPES


class Survey(TimeStampedModel):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


class Question(TimeStampedModel):
    survey = models.ForeignKey(Survey, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()
    type = models.PositiveSmallIntegerField(choices=QUESTION_TYPES, default=QUESTION_TYPES.text)


class Answer(TimeStampedModel):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    text = models.TextField()


class SurveyResult(models.Model):
    survey = models.ForeignKey(Survey, related_name="results", on_delete=models.SET_NULL, null=True)
    user_id = models.PositiveIntegerField()


class SurveyAnswer(models.Model):
    result = models.ForeignKey(SurveyResult, related_name="answers", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="questions", on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer, related_name="user_answers")
    custom_answer = models.TextField(blank=True, null=True)
