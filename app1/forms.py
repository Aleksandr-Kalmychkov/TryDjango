from django import forms
 
class UserForm(forms.Form):
    nameOfEvent = forms.CharField(label="Наименование мероприятия:")
    socialMediaLinks = forms.URLField(label="Ссылки на соц. сети:")
    name = forms.CharField(label="Ваше имя:")
    phoneNumber = forms.CharField(label="Номер телефона:")
    email = forms.EmailField(label="Электронная почка:")
    dateOfEvent = forms.DateField(label="Дата проведения мероприятия:", widget=forms.SelectDateWidget)
    city = forms.CharField(label="Город:")
    countOfClasses = forms.IntegerField(label="Количество классов автомобилей:")
    countOfWinners = forms.IntegerField(label="Количество призовых мест:")
    fileOfRules = forms.FileField(label="Прикрепите файл регламента:", widget=forms.FileInput)
    deliveryAddress = forms.CharField(label="Адрес ближайшего пункта выдачи транспортной компании:")
    comment = forms.CharField(label="Комментарий:", widget=forms.Textarea)