# Survey app

## Installation
Install ``docker`` and run ``docker-compose up --build`` to build and start project

## Usage

### Admin routes
authorization = ``basic`` \
credentials = ``admin:admin123`` \

1. Create/Update/Delete survey \
route = ``/survey/`` \
methods = ``[post, put, delete]``

2. Create/Update/Delete questions \
route = ``/survey/questions/`` \
methods = ``[post, put, delete]``

3. Create/Update/Delete answers \
route = ``/survey/answers/`` \
methods = ``[post, put, delete]``

### Client routes

1. List/Retrieve all active surveys \
route = ``/survey/active/`` \
methods = ``[get]``

2. Pass survey \
route = ``/survey/pass/``
method = ``post`` \
params = request data must be in next format :
```
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
```

3. List survey results \
route = ``/survey/results/`` \
methods = ``[get]`` \
put ``user_id`` in query params to checks results

