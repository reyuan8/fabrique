from django.utils.translation import gettext as _
from model_utils import Choices


QUESTION_TYPES = Choices(
    (1, "text", _("Текс")),
    (2, "multiple", _("Несколько ответов")),
    (3, "single", _("Один ответ")),
)


PASS_SURVEY_DESCRPTION = """
    request data must be in next format :
    {
        "user_id": "id",  # user id
        "survey": "id",  # survey id
        "answers": [  # list of question with answers
            {
                "question": "id",  # question id
                "answers": [ id/list of ids ],  #  id/list_of_ids( simple answer/multiple answers )
                "custom_answer": "text"  # custom answer if custom answer question type
            }
        ]
    }
"""