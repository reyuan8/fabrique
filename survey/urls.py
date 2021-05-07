from django.urls import path, include
from rest_framework.routers import DefaultRouter

from survey.views import health_check, SurveyViewSet, QuestionViewSet, AnswerViewSet, SurveyReadViewSet, PassSurveyView, \
    SurveyResultViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'active', SurveyReadViewSet)
router.register(r'results', SurveyResultViewSet)
router.register(r'', SurveyViewSet)

urlpatterns = [
    path('pass/', PassSurveyView.as_view(), name='pass_survey'),
    path('healthcheck/', health_check, name='health_check'),
    path("", include(router.urls)),
]