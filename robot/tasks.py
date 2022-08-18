from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail

import requests

from robot.models import Robot_Author, Robot_Quotes


@shared_task
def send(email, text_robot):
    send_mail(
        'This my new robot program',
        text_robot,
        'kkononenko3@gmail.com',
        [email, ],
        fail_silently=False,
    )


def robot_find_request(url):
    get_req = requests.get(url)
    soup = BeautifulSoup(get_req.content, "html.parser")
    return soup


@shared_task
def robot_author_quote():
    main_flag = False
    main_url = "https://quotes.toscrape.com/"
    second_url = main_url
    count_one = 0
    while True:
        all_quote = robot_find_request(second_url).find_all("div", {"class": "quote"})
        for i in all_quote:
            receive_text_quote = i.span.text
            receive_name_author = i.small.text
            receive_link_author = main_url + i.a.get("href")
            req_get = requests.get(receive_link_author)
            get_b = BeautifulSoup(req_get.content, "html.parser")
            description = get_b.find("div", {"class": "author-description"}).text
            if not Robot_Quotes.objects.filter(text=receive_text_quote).exists():
                author_g_o_c = Robot_Author.objects.get_or_create(name=receive_name_author,
                                                                  defaults={'description': description})
                Robot_Quotes.objects.get_or_create(text=receive_text_quote, authors=author_g_o_c[0])
                count_one += 1
            if count_one == 5:
                main_flag = True
                break
        if main_flag:
            break
        if not robot_find_request(second_url).find('li', {'class': 'next'}):
            email = "kkononenko3@gmail.com"
            text_robot = "All quote are over."
            send(email=email, text_robot=text_robot)
            break
        next_page = robot_find_request(second_url).find('li', {'class': 'next'})
        link_next_page = next_page.a.get("href")
        second_url = main_url + link_next_page
