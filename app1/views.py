from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from .models import Application
 
 
def index(request):
    if request.method == "POST":
        day = "{:{fill}{align}{width}}"
        day = day.format(request.POST.get("dateOfEvent_day"), fill='0', align='>', width=2)
        #day = "{:02d}".format(request.POST.get("dateOfEvent_day"))
        month = "{:{fill}{align}{width}}"
        month = month.format(request.POST.get("dateOfEvent_month"), fill='0', align='>', width=2)
        #month = "{:02d}".format(request.POST.get("dateOfEvent_month"))
        year = "{:{fill}{align}{width}}"
        year = year.format(request.POST.get("dateOfEvent_year"), fill='0', align='>', width=4)
        #year = "{:04d}".format(request.POST.get("dateOfEvent_year"))
        application = Application.objects.create(
            nameOfEvent = request.POST.get("nameOfEvent"),
            socialMediaLinks = request.POST.get("socialMediaLinks"),
            name = request.POST.get("name"),
            phoneNumber = request.POST.get("phoneNumber"),
            email = request.POST.get("email"),
            dateOfEvent = year + "-" + month + "-" + day,
            city = request.POST.get("city"),
            countOfClasses = request.POST.get("countOfClasses"),
            countOfWinners = request.POST.get("countOfWinners"),
            fileOfRules = request.POST.get("fileOfRules"),
            deliveryAddress = request.POST.get("deliveryAddress"),
            comment = request.POST.get("comment")
        )
        id = application.id
        return HttpResponse(f"<h2>Заявка отправлена! Идентификатор: {id}</h2>")
    else:
        userform = UserForm()
        return render(request, "app1/form.html", {"form": userform})