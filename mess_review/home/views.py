from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import student, admintable, dish, waste
import random



def view_waste(request):
    '''
        Loads Page to view wastage for Admin
        Return django.shortcuts.render object with waste_food.html
    '''
    return render(request, 'waste_food.html')

def dish(request):
    '''
        Loads Page to view all dishes for students
        Return django.shortcuts.render object with dish.html
    '''
    return render(request, 'dish.html')


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
    if 'admin_id' not in request.session:
        return redirect(adminlog)

    return render(request, 'admin.html')

def viewdish(request):
    '''
        Loads Page to view dishes table for admin
        Return django.shortcuts.render object with viewdish.html
    '''
    if 'admin_id' not in request.session:
        return redirect(adminlog)

    return render(request, 'viewdish.html')


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
        request.session['admin_id'] = t.id
        request.session['admin_name'] = t.name
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
            request.session['student_id'] = t.id
            request.session['name'] = t.name

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

def load_waste(request):
    '''
        Sends all wastage details between from and to dates recevied in POST request to view in tabular form
        Return django.shortcuts.HttpResponse object with results
    '''
    to = request.POST.get("to", "")
    from_ = request.POST.get("from", "")
    print(type(from_),type(to))
    if(to == '' or from_ == ''):
        wastes = waste.objects.order_by('date').reverse()
    else:
        wastes = waste.objects.filter(date__range=[from_, to]).order_by('date').reverse()
    output = ""
    c = 1
    for s in wastes:
        perc = 0
        if s.total != 0:
            perc = s.wastage*100/s.total
        output += f"<tr><td>{c}</td><td>{s.date}</td><td>{s.total}</td><td>{s.wastage}</td><td>{perc}</td></tr>"
        c +=1
    print(output)
    return HttpResponse(output)


def dish_load(request):
    '''
        Loads all dishes for admin in tabular form
        Return django.shortcuts.HttpResponse with results
    '''
    dishs = dish.objects.all()
    output = ""
    ss = 1
    for s in dishs:
        c = f'<button type="button" class="btn btn-primary" onclick="update(\'{s.id}\');">Delete</button>'
        c += f' <a href="\edit?id={s.id}"><button type="button" class="btn btn-primary">Edit</button></a>'
        output += f"<tr><td>{ss}</td><td>{s.name}</td><td>Rs. {s.price}</td><td>{c}</td></tr>"
        ss += 1
    # print(output)
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

def delete_dish(request):
    '''
        Deletes a dish as requested by Admin
        Return django.shortcuts.HttpResponse with response
    '''
    id = request.POST.get("id", "")
    dish.objects.get(id=id).delete()
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
    if 'student_id' not in request.session:

        return redirect(login)
    print(request.session['student_id'])
    dishes = dish.objects.all()

    idf = []
    c = 0
    for d in dishes:
        x = [d.id,d.ifile,d.price,d.name]

        idf.append(x)

    context = {"idf":idf}
    return render(request, 'home.html',context)


def add_dish(request):
    '''
        Loads page to add dish form for admin
        Return django.shortcuts.render with Additem.html
    '''
    return render(request, 'Additem.html')

def add_item(request):
    '''
        Add new dish to DB, as received in POST reques
        Return django.shortcuts.redirect with viewdish
    '''
    file = request.FILES["imagef"]
    name = request.POST.get("name", "")
    price = request.POST.get("price", "")
    des = request.POST.get("des", "")
    time = request.POST.getlist('checks[]')
    time = ", ".join(time)
    print(name, price, des, time, file)
    food = dish(name=name,price=int(price),des=des,serve_time=time,ifile=file)
    food.save()
    return render(request, 'home.html')

def add_waste(request):
    '''
        Add a wastage report for the day
        Return django.shortcuts.redirect with view_waste
    '''
    date = request.POST.get("date", "")
    total = request.POST.get("total", "")
    was = request.POST.get("waste", "")
    print(date,total,was)
    if waste.objects.filter(date=date).exists():
        waste.objects.filter(date=date).delete()

    w = waste(date=date,total=int(total),wastage=int(was))
    w.save()
    return redirect(view_waste)


def edit_item(request):
    '''
        Updates a dish as recived in POST request
        Return django.shortcuts.redirect with viewdish
    '''
    id = request.POST.get("id", "")
    try:
        file = request.FILES["imagef"]
    except:
        file=''
    # print("hhhhhhhhhhhhhhhhhhhhhh")
    name = request.POST.get("name", "")
    price = request.POST.get("price", "")
    des = request.POST.get("des", "")
    time = request.POST.getlist('checks[]')
    time = ", ".join(time)
    print(name, price, des, time, file)
    t = dish.objects.get(id=id)
    if file != "":
        t.ifile = file
    if name != "":
        t.name = name
    if price != "":
        t.price = int(price)
    if time != "":
        t.serve_time = time
    if des != "":
        t.des = des

    # food = dish(name=name,price=int(price),des=des,serve_time=time,ifile=file)
    t.save()
    return redirect(viewdish)


def edit_dish(request):
    '''
        Edits dish as recived from POST request
        Return django.shortcuts.render with edit_dish.html
    '''
    id = request.GET.get("id", "")
    t = dish.objects.get(id=id)
    context = {"id":t.id,"name":t.name,"price":t.price,"des":t.des,"image":t.ifile,"time":t.serve_time}
    return render(request, 'edit_dish.html',context)

