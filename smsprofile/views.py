from django.shortcuts import render

def register_student(request):
    if(request.method=="POST"):
        print(request.POST)
    return render(request,template_name='smsprofile/student_reg_form.html')
