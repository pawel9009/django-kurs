from django.shortcuts import render
from ap.models import User
from ap.forms import NewUserForm


def index(request):
    return render(request, 'ap/index.html')
# Create your views here.

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('error')
    return render(request, 'ap/users.html', {'form': form})
