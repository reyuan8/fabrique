from django.db import transaction
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from survey.authentication import MyAuthentication
from survey.constants import PASS_SURVEY_DESCRPTION
from survey.models import Survey, Question, Answer, SurveyResult, SurveyAnswer
from survey.serializers import SurveyBaseSerializer, SurveySerializer, QuestionSerializer, AnswerSerializer, \
    SurveyListSerializer, SurveyDetailSerializer, SurveyResultSerializer
from survey.utils import validate_pass_survey_params


@api_view(["GET"])
def health_check(request):
    return Response("OK")


class SurveyViewSet(generics.CreateAPIView,
                    generics.UpdateAPIView,
                    generics.DestroyAPIView,
                    generics.ListAPIView,
                    viewsets.GenericViewSet):
    queryset = Survey.objects.all()
    permission_classes = []
    authentication_classes = [MyAuthentication]

    def get_queryset(self):
        return self.queryset.order_by("id")

    def get_serializer_class(self):
        return {
            "create": SurveySerializer,
            "update": SurveyBaseSerializer,
            "partial_update": SurveyBaseSerializer,
            "list": SurveySerializer,
        }.get(self.action)


class QuestionViewSet(generics.CreateAPIView,
                      generics.UpdateAPIView,
                      generics.DestroyAPIView,
                      generics.ListAPIView,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    permission_classes = []
    authentication_classes = [MyAuthentication]
    serializer_class = QuestionSerializer


class AnswerViewSet(generics.CreateAPIView,
                    generics.UpdateAPIView,
                    generics.DestroyAPIView,
                    generics.ListAPIView,
                    viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    permission_classes = []
    authentication_classes = [MyAuthentication]
    serializer_class = AnswerSerializer


class SurveyReadViewSet(generics.ListAPIView,
                        generics.RetrieveAPIView,
                        viewsets.GenericViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Survey.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_active=True).order_by("id")

    def get_serializer_class(self):
        return {
            "list": SurveyListSerializer,
            "retrieve": SurveyDetailSerializer,
        }.get(self.action)


class PassSurveyView(APIView):

    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(operation_description=PASS_SURVEY_DESCRPTION)
    def post(self, request):
        data = request.data
        validate_pass_survey_params(data)

        with transaction.atomic():

            survey_result = SurveyResult()
            survey_result.survey_id = data["survey"]
            survey_result.user_id = data["user_id"]
            survey_result.save()

            for answer in data["answers"]:
                survey_answer = SurveyAnswer()
                survey_answer.result = survey_result
                survey_answer.question_id = answer["question"]
                survey_answer.custom_answer = answer["custom_answer"]
                survey_answer.save()

                if len(answer["answers"]):
                    survey_answer.answers.set(answer["answers"])
                survey_answer.save()

        return Response(data)


class SurveyResultViewSet(generics.RetrieveAPIView,
                          generics.ListAPIView,
                          viewsets.GenericViewSet):
    serializer_class = SurveyResultSerializer
    permission_classes = []
    authentication_classes = []
    queryset = SurveyResult.objects.all()

    def get_queryset(self):
        if self.request.query_params.get("user_id"):
            return self.queryset.filter(user_id=self.request.query_params["user_id"])
        return []
