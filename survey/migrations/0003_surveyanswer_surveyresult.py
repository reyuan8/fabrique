# Generated by Django 2.2.10 on 2021-05-06 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_survey_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='results', to='survey.Survey')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_answer', models.TextField(blank=True, null=True)),
                ('answers', models.ManyToManyField(related_name='user_answers', to='survey.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='survey.Question')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='survey.SurveyResult')),
            ],
        ),
    ]
