from django.shortcuts import render
from enroll.models import Student


# Create your views here.
def StudentInfo(request):
    stud=Student.objects.all()
    print('myoutput',stud)
    return render(request,'enroll/studetails.html',{'stu':stud})

