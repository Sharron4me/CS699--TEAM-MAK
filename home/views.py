from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import student, admintable
import random



def login(request):
    '''
        Loads Page for student login
        Return django.shortcuts.render object with index.html
    '''
    return render(request, 'index.html')
def adminlog(request):
    '''
        Loads Page for admin login
        Return django.shortcuts.render object with adminlog.html
    '''
    return render(request, 'adminlog.html')

def adminhome(request):
    '''
        Loads Page to view Admin's home page
        Return django.shortcuts.render object with admin.html
    '''
    return render(request, 'admin.html')

def log_admin(request):
    '''
        Verifies Admin's Credentials
        Return django.shortcuts.redirect object with /adminhome if success
    '''
    passw = request.POST.get("pwd", "")
    ldap = request.POST.get("ldap", "")
    print(passw,ldap)
    if admintable.objects.filter(ldap=ldap,password=passw).exists():
        print("exists")
        t = admintable.objects.get(ldap=ldap,password=passw)
        return redirect(adminhome)
    return HttpResponse('Login failed!! Try again <a href="http://127.0.0.1:8000/adminlog">here</a>')

def log_ver(request):
    '''
        Verify Students Credentials
        Return django.shortcuts.redirect object with /home if success
    '''
    passw = request.POST.get("pwd", "")
    ldap = request.POST.get("ldap", "")
    print(passw,ldap)
    if student.objects.filter(ldap=ldap,password=passw).exists():
        print("exists")
        t = student.objects.get(ldap=ldap,password=passw)
        print(t.status)
        if t.status == 'Email Verified':
            return HttpResponse('You have not been verified by admin')
        elif t.status == 'unverified':
            return HttpResponse('You have not verified your LDAP, check your mail.')
        else:
            return redirect(home)
    return HttpResponse('Login failed!! Try again <a href="http://127.0.0.1:8000/">here</a>')

def confirm(request):
    '''
        Verify Students Email from link sent to IITB mail
        Return django.shortcuts.HttpResponse object with result
    '''
    ldap = request.GET.get("ldap", "")
    code = request.GET.get("sn", "")
    print(code,ldap)
    if student.objects.filter(ldap=ldap,code=code).exists():
        print("exists")
        t = student.objects.get(ldap=ldap,code=code)
        t.status = 'Email Verified'
        t.save()
        return HttpResponse('Verified! Login <a href="http://127.0.0.1:8000/">here</a>')
    return HttpResponse('Verification Failed!!')

def register(request):
    '''
        Loads Page for student register
        Return django.shortcuts.render object with register.html
    '''
    return render(request, 'register.html')


def student_load(request):
    '''
        Sends all student details for admin to view in tabular form
        Return django.shortcuts.HttpResponse object with results
    '''
    students = student.objects.all()
    output = ""
    for s in students:
        c = 'No actions'
        if s.status=='Email Verified':
            c = f'<button type="button" class="btn btn-primary" onclick="update(\'{s.ldap}\');">Verify</button>'
        output += f"<tr><td>{s.ldap}</td><td>{s.name}</td><td>{s.status}</td><td>{c}</td></tr>"
    print(output)
    return HttpResponse(output)

def verify(request):
    '''
        Student Verification confirmation done by Admin
        Return django.shortcuts.HttpResponse with response
    '''
    ldap = request.POST.get("ldap", "")
    t = student.objects.get(ldap=ldap)
    t.status = 'Admin Verified'
    t.save()
    return HttpResponse()

def reg(request):
    '''
        Registers student to the portal and sends confirmation email to their emails.
        Return django.shortcuts.HttpResponse
    '''
    print("hi")
    name = request.POST.get("name", "")
    passw = request.POST.get("pass", "")
    ldap = request.POST.get("ldap", "")
    print(name, passw, ldap)
    if student.objects.filter(ldap=ldap).exists():
        student.objects.filter(ldap=ldap).delete()
    code = random.randint(100000, 9999999)
    new_stu = student(name=name, ldap=ldap, password=passw, code=code, status='unverified')
    new_stu.save()


    link = f'http://127.0.0.1:8000/confirm/?sn={code}&ldap={ldap}'
    # return render(request, 'index.html')
    send_mail(
        'Register to IITB Hostel Mess',
        f'Hi {name}, you have registered to IITB hostel Mess Web app, please confirm your email by clicking on the below link\n {link}',
        'jingax.dev@gmail.com',
        ['aastik.soul@gmail.com'],
        fail_silently=True,
    )

    return HttpResponse('')
# Create your views here.

def home(request):
    '''
        Loads Page to view Admin's home page
        Return django.shortcuts.render object with admin.html
    '''
    return render(request, 'home.html')
