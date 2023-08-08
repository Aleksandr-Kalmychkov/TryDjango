from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
 
 
def index(request):
    if request.method == "POST":
        return HttpResponse(f"<h2>Заявка отправлена!</h2>")
    else:
        userform = UserForm()
        return render(request, "app1/main_template.html", {"form": userform})