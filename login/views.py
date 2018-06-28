from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as mylogin

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            mylogin(request, user)
            return redirect(students.views.home)
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    logout(request)
    return render(request, 'login.html')
