from django.shortcuts import render
def django_learn(request):
    cname='django and python +SQL'
    duration="6 Month"
    seat=1
    django_detail={'cn':cname,'du':duration,'st':seat}
    return render(request,'testapp/home.html',django_detail)

# Create your views here.
