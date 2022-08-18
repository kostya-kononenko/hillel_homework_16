from datetime import datetime

from django import forms


class RobotForm(forms.Form):

    email = forms.EmailField(max_length=50, required=True)
    text_for_robot = forms.CharField(max_length=300, required=True)
    data_robot = forms.DateTimeField(label='Data', initial=datetime.now(), required=True, help_text='Enter format '
                                                                                                    'YYYY-MM-DD '
                                                                                                    'HH:MM:SS')
