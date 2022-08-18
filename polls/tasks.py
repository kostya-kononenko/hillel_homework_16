from time import sleep

from celery import shared_task

from polls.models import Question


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def question_update(pk, text):
    sleep(5)
    question = Question.objects.get(id=pk)
    question.question_text = text
    question.save()
