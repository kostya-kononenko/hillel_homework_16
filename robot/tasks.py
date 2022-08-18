from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send(email, text_robot):
    send_mail(
        'This my new robot program',
        text_robot,
        'kkononenko3@gmail.com',
        [email, ],
        fail_silently=False,
    )
