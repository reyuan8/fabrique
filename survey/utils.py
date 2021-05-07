from rest_framework.exceptions import ValidationError


def error_message(message, error_type="validation error"):
    return {
        "error": error_type,
        "message": message
    }


def validate_pass_survey_params(data: dict):
    if not data.get("user_id"):
        raise ValidationError(detail=error_message("user_id must be given"))
    if not data.get("survey"):
        raise ValidationError(detail=error_message("survey must be given"))

    answers = data.get("answers")
    if not answers:
        raise ValidationError(detail=error_message("answers must be given"))
    if type(answers) != list:
        raise ValidationError(detail=error_message("answers must be list"))

    for a in answers:
        if not a.get("question"):
            raise ValidationError(detail=error_message("question must be in answers list"))
        if not a.get("answers"):
            if not type(a.get("answers")) == list:
                raise ValidationError(detail=error_message("answers must be in answers list"))
        if not a.get("custom_answer"):
            a["custom_answer"] = ""
