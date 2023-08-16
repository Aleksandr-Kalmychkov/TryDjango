from django import forms
from django.forms import ModelForm
from .models import Application
from django.utils.translation import gettext_lazy as _
# class UserForm(ModelForm):
#     class Meta:
#         model = Application
#         nameOfEvent = forms.CharField(label="Наименование мероприятия:")
#         socialMediaLinks = forms.URLField(label="Ссылки на соц. сети:")
#         name = forms.CharField(label="Ваше имя:")
#         phoneNumber = forms.CharField(label="Номер телефона:")
#         email = forms.EmailField(label="Электронная почка:")
#         dateOfEvent = forms.DateField(label="Дата проведения мероприятия:", widget=forms.SelectDateWidget)
#         city = forms.CharField(label="Город:")
#         countOfClasses = forms.IntegerField(label="Количество классов автомобилей:")
#         countOfWinners = forms.IntegerField(label="Количество призовых мест:")
#         fileOfRules = forms.FileField(label="Прикрепите файл регламента:", widget=forms.FileInput)
#         deliveryAddress = forms.CharField(label="Адрес ближайшего пункта выдачи транспортной компании:")
#         comment = forms.CharField(label="Комментарий:", widget=forms.Textarea)

class UserForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        labels = {
            "nameOfEvent": _("Наименование мероприятия"),
            "socialMediaLinks": _("Ссылка на соц. сети"),
            "name": _("Ваше имя"),
            "phoneNumber": _("Номер телефона"),
            "email": _("Электронная почта"),
            "dateOfEvent": _("Дата проведения мероприятия"),
            "city": _("Город"),
            "countOfClasses": _("Количество классов автомобилей"),
            "countOfWinners": _("Количетсво победителей"),
            "fileOfRules": _("Файл регламента соревнований"),
            "deliveryAddress": _("Адрес ближайшего пункта выдачи транспортной компании"),
            "comment": _("Комментарий"),
        }
        
        