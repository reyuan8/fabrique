from rest_framework import serializers

from survey.models import Survey, Question, Answer, SurveyResult, SurveyAnswer


class ChoiceValueDisplayField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data

    def get_attribute(self, instance):
        try:
            attr = self.source
            display_method = getattr(instance, 'get_%s_display' % attr)

            value = getattr(instance, attr)
            display_value = display_method()

            return {
                'value': value,
                'display': display_value
            }
        except Exception as e:
            print(e)
            return super(ChoiceValueDisplayField, self).get_attribute(instance)


class SurveyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ["id", "name", "end_date", "description", "is_active"]


class SurveySerializer(SurveyBaseSerializer):
    class Meta(SurveyBaseSerializer.Meta):
        fields = SurveyBaseSerializer.Meta.fields + ["start_date"]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "survey", "text", "type", "answers"]
        extra_kwargs = {"answers": {"read_only": True}}


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "question", "text"]


class SurveyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ["id", "name", "start_date", "end_date", "description"]


class AnswerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "text"]


class QuestionBaseReadSerializer(serializers.ModelSerializer):
    type = ChoiceValueDisplayField()

    class Meta:
        model = Question
        fields = ["id", "text", "type"]


class QuestionReadSerializer(QuestionBaseReadSerializer):
    answers = AnswerReadSerializer(many=True, read_only=True)

    class Meta(QuestionBaseReadSerializer.Meta):
        fields = QuestionBaseReadSerializer.Meta.fields + ["answers"]


class SurveyDetailSerializer(SurveyListSerializer):
    questions = QuestionReadSerializer(many=True, read_only=True)

    class Meta(SurveyListSerializer.Meta):
        fields = SurveyListSerializer.Meta.fields + ["questions"]


class SurveyAnswerSerializer(serializers.ModelSerializer):
    question = QuestionBaseReadSerializer(read_only=True)
    answers = AnswerReadSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyAnswer
        fields = ["id", "question", "answers", "custom_answer"]


class SurveyResultSerializer(serializers.ModelSerializer):
    answers = SurveyAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = SurveyResult
        fields = ["id", "survey", "user_id", "answers"]


