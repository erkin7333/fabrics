from django.shortcuts import render




def register(request):
    return render(request, 'account/sing-up.html')



def user_login(request):

    return render(request, 'account/login.html')
