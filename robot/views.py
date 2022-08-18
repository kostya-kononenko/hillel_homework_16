from datetime import timedelta

from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import RobotForm
from .tasks import send


def home(request):
    return render(request, "robot/home.html")


def error(request):
    return render(request, "robot/error.html")


def robot(request):
    if request.method == "POST":
        robot_form = RobotForm(request.POST)
        if robot_form.is_valid():
            email = robot_form.cleaned_data["email"]
            text_for_robot = robot_form.cleaned_data["text_for_robot"]
            data_robot = robot_form.cleaned_data["data_robot"]
            data_receive = timezone.now()
            data_between = data_receive + timedelta(days=2)
            if (data_robot > data_receive) and (data_robot <= data_between):
                send.s(email, text_for_robot).apply_async(eta=data_robot)
                return redirect('robot:home')
            else:
                return redirect('robot:error')
    else:
        robot_form = RobotForm()
    return render(
        request,
        "robot/robot.html",
        {"robot_form": robot_form, }
    )
