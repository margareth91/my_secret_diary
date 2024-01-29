from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_account = form.save()
            authenticated_account = authenticate(
                username=new_account.username, password=request.POST["password1"]
            )
            login(request, authenticated_account)
            return redirect("index")
    context = {"form": form}
    return render(request, "accounts/register.html", context)
