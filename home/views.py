from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.conf import settings
<<<<<<< HEAD
from .models import student, admintable, dish, waste, review, complaint, campaign
import random


def stu_waste(request):
    '''
    Loads Page to view wastage for students
    Return django.shortcuts.render object with stu_waste.html
    '''
    if 'student_id' not in request.session:
        return redirect(login)

    return render(request, 'stu_waste.html')
def view_waste(request):
    '''
        Loads Page to view wastage for Admin
        Return django.shortcuts.render object with waste_food.html
    '''
    if 'admin_id' not in request.session:
        return redirect(adminlog)

    return render(request, 'waste_food.html')
def comp_detail(request):
    '''
        Loads Page to view complain details for students
        Return django.shortcuts.render object with comp_detail_stu.html
        '''
    if 'student_id' not in request.session:
        return redirect(login)

    return render(request, 'comp_detail_stu.html')

def admin_comp_detail(request):
    '''
        Loads Page to view complain details for admin
        Return django.shortcuts.render object with comp_detail_admin.html
    '''
    if 'admin_id' not in request.session:
        return redirect(adminlog)

    return render(request, 'comp_detail_admin.html')


def raise_comp(request):
    '''
        Loads Page to view form to raise complaint details for students
        Return django.shortcuts.render object with complain.html
    '''

    if 'student_id' not in request.session:

        return redirect(login)
    return render(request, 'complain.html')

def raise_camp(request):
    '''
        Loads Page to view form to raise campaign details for students
        Return django.shortcuts.render object with new_camp.html
    '''

    if 'student_id' not in request.session:

        return redirect(login)
    return render(request, 'new_camp.html')



def comp(request):
    '''
        Loads Page to view complaint for students
        Return django.shortcuts.render object with view_comp.html
    '''

    return render(request, 'view_comp.html')

def admin_comp(request):
    '''
        Loads Page to view complaints for admin
        Return django.shortcuts.render object with admin_comp.html
    '''

    if 'admin_id' not in request.session:
        return redirect(adminlog)

    return render(request, 'admin_comp.html')


def dishs(request):
    '''
        Loads Page to view all dishes for students
        Return django.shortcuts.render object with dish.html
    '''

    if 'student_id' not in request.session:

        return redirect(login)
    return render(request, 'dish.html')


=======
from .models import student, admintable
import random


>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3

def login(request):
    '''
        Loads Page for student login
        Return django.shortcuts.render object with index.html
    '''
    return render(request, 'index.html')
<<<<<<< HEAD

=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
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
<<<<<<< HEAD

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


=======
    return render(request, 'admin.html')

>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
def log_admin(request):
    '''
        Verifies Admin's Credentials
        Return django.shortcuts.redirect object with /adminhome if success
    '''
<<<<<<< HEAD

=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
    passw = request.POST.get("pwd", "")
    ldap = request.POST.get("ldap", "")
    print(passw,ldap)
    if admintable.objects.filter(ldap=ldap,password=passw).exists():
        print("exists")
        t = admintable.objects.get(ldap=ldap,password=passw)
<<<<<<< HEAD
        request.session['admin_id'] = t.id
        request.session['admin_name'] = t.name
=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
        return redirect(adminhome)
    return HttpResponse('Login failed!! Try again <a href="http://127.0.0.1:8000/adminlog">here</a>')

def log_ver(request):
    '''
        Verify Students Credentials
        Return django.shortcuts.redirect object with /home if success
    '''
<<<<<<< HEAD

=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
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
<<<<<<< HEAD
            request.session['student_id'] = t.id
            request.session['name'] = t.name

=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
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

<<<<<<< HEAD
def show_dish(request):
    '''
        Sends details for a dish id received in a POST request
        Return django.shortcuts.HttpResponse object with results
    '''
    fid = request.POST.get("fid", "")
    print(fid)
    t = dish.objects.get(id=int(fid))
    output = [t.name, str(t.price), t.des, str(t.ifile),t.serve_time]
    print(output)
    output = "##".join(output)
    print(output)
    return HttpResponse(output)
=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3

def student_load(request):
    '''
        Sends all student details for admin to view in tabular form
        Return django.shortcuts.HttpResponse object with results
    '''
<<<<<<< HEAD

=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
    students = student.objects.all()
    output = ""
    for s in students:
        c = 'No actions'
        if s.status=='Email Verified':
            c = f'<button type="button" class="btn btn-primary" onclick="update(\'{s.ldap}\');">Verify</button>'
        output += f"<tr><td>{s.ldap}</td><td>{s.name}</td><td>{s.status}</td><td>{c}</td></tr>"
    print(output)
    return HttpResponse(output)

<<<<<<< HEAD
def view_comp(request):
    '''
        Sends student's complaint details to view in tabular form
        Return django.shortcuts.HttpResponse object with results
    '''
    coms = complaint.objects.filter(onwer= request.session['student_id'])
    output = ""
    ss = 1
    for s in coms:
        c = f'<a href="/comp_detail/?cid={s.id}">View</a>'
        output += f"<tr><td>{ss}</td><td>{s.sub}</td><td>{c}</td></tr>"
        ss+=1
    print(output)
    return HttpResponse(output)

def admin_view_comp(request):
    '''
        Sends all student complaint details for admin to view in tabular form
        Return django.shortcuts.HttpResponse object with results
    '''

    coms = complaint.objects.all()
    output = ""
    ss = 1
    for s in coms:
        if student.objects.filter(id=s.onwer).exists():
            owner = student.objects.get(id=s.onwer)
            owner = f"{owner.name} (LDAP: {owner.ldap})"
        else:
            owner = "User Deleted"

        c = f'<a href="/admin_comp_detail/?cid={s.id}">View</a>'
        output += f"<tr><td>{ss}</td><td>{owner}</td><td>{s.sub}</td><td>{c}</td></tr>"
        ss +=1
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

def show_review(request):
    '''
        Loads all reviews for a dish id, from GET request
        Return django.shortcuts.HttpResponse with results
    '''
    print("XXXXXXXXXXX")
    fid = request.POST.get("fid", "")
    reviews = review.objects.filter(fid=fid)
    output = ""
    rate = 0
    ss = 0
    for s in reviews:
        if s.ifile =='':
            img = ''
        else:
            img = f'<img style="height:25vh;width:auto;" src="/media/{s.ifile}">'
        user = "Deleted User"
        if student.objects.filter(id=s.owner).exists():
            print("exists")
            t = student.objects.get(id=s.owner)
            user=t.name
            if s.anon == 1:
                user = "Anonymous Ninja"


        rate += s.rating
        ss += 1
        output += f'<div class="jumbotron jumbotron-fluid"><div class="container"><h5 class="display-16">{user} - {s.rating}/5</h5><p class="lead">{s.text}</p>{img}</div></div><br>'

    # print(output)
    if ss ==0 :
        rate=0
    else :
        rate = rate/ss
    rate = '%.2f'%rate
    rate =str(rate)
    return HttpResponse(rate+"##"+output)



=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
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

<<<<<<< HEAD
def delete_dish(request):
    '''
        Deletes a dish as requested by Admin
        Return django.shortcuts.HttpResponse with response
    '''
    id = request.POST.get("id", "")
    dish.objects.get(id=id).delete()
    return HttpResponse()


=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
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
<<<<<<< HEAD
    print(link)
=======
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
    send_mail(
        'Register to IITB Hostel Mess',
        f'Hi {name}, you have registered to IITB hostel Mess Web app, please confirm your email by clicking on the below link\n {link}',
        'jingax.dev@gmail.com',
<<<<<<< HEAD
        ['kiran.ranebennur@gmail.com'],
=======
        ['aastik.soul@gmail.com'],
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
        fail_silently=True,
    )

    return HttpResponse('')
# Create your views here.

<<<<<<< HEAD
def post_review(request):
    '''
        Adds review to a dish for student
        Return django.shortcuts.redirect with /dish
    '''
    print("hi")
    anon = request.POST.getlist('checks[]')
    text = request.POST.get("text", "")
    fid = request.POST.get("fid", "")
    rating = request.POST.get("rating", "")
    try:
        file = request.FILES["imagef"]
    except:
        file=''
    print(anon)
    if review.objects.filter(owner=request.session['student_id'],fid=fid).exists():
        review.objects.filter(owner=request.session['student_id'],fid=fid).delete()

    new_rev = review(anon=len(anon),owner=request.session['student_id'], fid=fid, text=text, rating=rating,ifile=file)
    new_rev.save()
    return redirect("/dishs/?fid="+fid)


def home(request):
    '''
        Loads student home page with all dishes
        Return django.shortcuts.render with home.html
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
    if 'admin_id' not in request.session:
        return redirect(adminlog)

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
    return redirect(viewdish)

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

def add_comp(request):
    '''
        Add a complaint for student
        Return django.shortcuts.redirect with comp
    '''
    sub = request.POST.get("sub", "")
    try:
        file = request.FILES["imagef"]
    except:
        file=''

    des = request.POST.get("des", "")
    # print(name, price, des, time, file)
    comp1 = complaint(sub=sub,des=des,ifile=file,onwer=request.session['student_id'])
    comp1.save()
    return redirect(comp)

def add_camp(request):
    '''
        Add a campaign for student
        Return django.shortcuts.redirect with all_camps
    '''

    sub = request.POST.get("sub", "")
    des = request.POST.get("des", "")
    # print(name, price, des, time, file)
    camp1 = campaign(sub=sub,des=des,owner=request.session['student_id'],ups='0',dns='0')
    camp1.save()
    return redirect(all_camps)



def edit_dish(request):
    '''
        Edits dish as recived from POST request
        Return django.shortcuts.render with edit_dish.html
    '''
    id = request.GET.get("id", "")
    t = dish.objects.get(id=id)
    context = {"id":t.id,"name":t.name,"price":t.price,"des":t.des,"image":t.ifile,"time":t.serve_time}
    return render(request, 'edit_dish.html',context)

# def show_comp(request):
#     cid = request.POST.get("cid", "")
#     if complaint.objects.filter(id=int(cid)).exists():
#         t = complaint.objects.get(id=int(cid))
#     else:
#         return HttpResponse("##")
#     if t.onwer != request.session['student_id']:
#         return redirect(comp)
#     if student.objects.filter(id=t.onwer).exists():
#         owner = student.objects.get(id=t.onwer)
#         owner = f"{owner.name} (LDAP: {owner.ldap})"
#     else:
#         owner = "User Deleted"
#
#     output = [t.sub,t.des,owner,str(t.ifile)]
#     return HttpResponse("##".join(output))

def show_comp(request):
    '''
        Sends Complaint details for students and admin
        Return django.shortcuts.HttpResponse with output
    '''
    cid = request.POST.get("cid", "")
    if complaint.objects.filter(id=int(cid)).exists():
        t = complaint.objects.get(id=int(cid))
    else:
        return HttpResponse("#########################")
    flag = True
    flag2 = True
    for sesskey in request.session.keys():
        if sesskey == 'admin_id':
            flag = False
        if sesskey == 'student_id':
            if t.onwer != request.session['student_id']:
                flag2 = False
    if flag2 and flag:
        print("################")
        return HttpResponse("#########################")
    if student.objects.filter(id=t.onwer).exists():
        owner = student.objects.get(id=t.onwer)
        owner = f"{owner.name} (LDAP: {owner.ldap})"
    else:
        owner = "User Deleted"

    output = [t.sub,t.des,owner,str(t.ifile)]
    return HttpResponse("##".join(output))



def student_nav(request):
    '''
        Loads nav bar for student
        Return django.shortcuts.HttpResponse with output
    '''
    output = f'<a class="navbar-brand" href="/home">Hostel 1 Mess</a> <span class="navbar-brand" href="/home">Hi, {request.session["name"]}</span><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4"><li class="nav-item"><a class="nav-link active" aria-current="page" href="/home">Home</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/comp">My Complaints</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/raise_comp">New Complaint</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/all_camps">Campaigns</a></li></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/raise_camp">New Campaign</a></li></ul><ul class="nav navbar-nav navbar-right"><li class="nav-item"><a class="nav-link" href="/logout_stu" ><i class="bi bi-box-arrow-right"></i>Logout</a></li></ul>'
    return HttpResponse(output)

def admin_nav(request):
    '''
        Loads nav bar for admin
        Return django.shortcuts.HttpResponse with output
    '''
    output = f'<a class="navbar-brand" href="/home">Hostel 1 Mess</a> <span class="navbar-brand" href="/home">Hi, Admin</span><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4"><li class="nav-item"><a class="nav-link active" aria-current="page" href="/adminhome">Home</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/adddish">Add Dish</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/viewdish">View Dish</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/view_waste">Wastage</a></li></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/admin_comp">All Complaints</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/all_camps_admin">All Campaigns</a></li></ul><ul class="nav navbar-nav navbar-right"><li class="nav-item"><a class="nav-link" href="/logout_admin" ><i class="bi bi-box-arrow-right"></i>Logout</a></li></ul>'
    return HttpResponse(output)


def all_camps(request):
    '''
        Loads page for students to view all campaigns
        Return django.shortcuts.render with campaigns.html
    '''
    if 'student_id' not in request.session:

        return redirect(login)
    return render(request, 'campaigns.html')

def all_camps_admin(request):
    '''
        Loads page for admin to view all campaigns
        Return django.shortcuts.render with campaigns_admin.html
    '''
    if 'admin_id' not in request.session:

        return redirect(login)
    return render(request, 'campaigns_admin.html')




def vote_page(request):
    '''
        Sends all campaign details to student along with choice to up/down vote campaigns
        Return django.shortcuts.HttpResponse with response
    '''
    print("hi")
    output = ['','','']
    camps = campaign.objects.all()
    for s in camps:
         user = "Deleted User"
         b1 = 'success'
         b2 = 'success'
         dis = ''
         ups = s.ups
         dns = s.dns
         ups = ups.split(',')
         ups = ups[1:]
         dns = dns.split(',')
         dns = dns[1:]
         print(s.sub)
         print(len(ups),len(dns))

         total = 0
         try:

             votes = len(ups)/(len(ups)+len(dns))
             votes *= 100
             votes = '%.2f'%votes
             total = len(ups)+len(dns)
         except:
             print("ex")
             votes = 0

         print(votes)

         if str(request.session['student_id']) in set(ups):
             dis = 'disabled'
             b2 = 'secondary'
         if str(request.session['student_id']) in set(dns):
             dis = 'disabled'
             b1 = 'secondary'

         if student.objects.filter(id=s.owner).exists():
             print("exists")
             t = student.objects.get(id=s.owner)
             user = t.name
         if s.status != 'Active':
             dis = 'disabled'
         button = f'<div class="row"><div class="col-8"></div><div class="col-2"><button type="button" class="btn btn-{b1}" onclick="vote(1,{s.id})" {dis}>Up Vote</button></div><div class="col-2"><button type="button" class="btn btn-{b2}" onclick="vote(0,{s.id})" {dis}>Down Vote</button></div></div>'
         c = f'<div class="card mb-3"><div class="card" ><div class="card-body"><h5 class="card-title">{s.sub}</h5><p class="card-text">{s.des}</p><p class="card-text"><small class="text-muted">Raised By: {user}</small></p><p class="card-text"><small class="text-muted">Status: {s.status} Total votes : {total}</small></p></div><div class="progress" style="margin:2vh 10vw;"><div class="progress-bar progress-bar-striped progress-bar-animated"  role="progressbar" aria-valuenow="{votes}" aria-valuemin="0" aria-valuemax="100" style="width: {votes}%">{votes}%</div></div>{button}<br></div></div>'
         if s.status == 'Active':
            output[0] += c
         else:
            output[2] += c
         output[1] += c
         # print(c)
    return HttpResponse("##".join(output))


def vote_page_admin(request):
    '''
        Sends all campaign details to admin along with choice to accept reject campaigns
        Return django.shortcuts.HttpResponse with response
    '''
    print("hi")
    output = ['','','']
    camps = campaign.objects.all()
    for s in camps:
         user = "Deleted User"
         b1 = 'success'
         b2 = 'success'
         dis = ''
         ups = s.ups
         dns = s.dns
         ups = ups.split(',')
         ups = ups[1:]
         dns = dns.split(',')
         dns = dns[1:]
         print(s.sub)
         print(len(ups),len(dns))

         total = 0
         try:

             votes = len(ups)/(len(ups)+len(dns))
             votes *= 100
             votes = '%.2f'%votes
             total = len(ups)+len(dns)
         except:
             print("ex")
             votes = 0

         print(votes)

         if s.status == 'Rejected':
             dis = 'disabled'
             b1 = 'secondary'
         if s.status == 'Accepted':
             dis = 'disabled'
             b2 = 'secondary'

         if student.objects.filter(id=s.owner).exists():
             print("exists")
             t = student.objects.get(id=s.owner)
             user = t.name
         if s.status != 'Active':
             dis = 'disabled'
         button = f'<div class="row"><div class="col-8"></div><div class="col-2"><button type="button" class="btn btn-{b1}" onclick="vote(1,{s.id})" {dis}>Accept</button></div><div class="col-2"><button type="button" class="btn btn-{b2}" onclick="vote(0,{s.id})" {dis}>Reject</button></div></div>'
         c = f'<div class="card mb-3"><div class="card" ><div class="card-body"><h5 class="card-title">{s.sub}</h5><p class="card-text">{s.des}</p><p class="card-text"><small class="text-muted">Raised By: {user}</small></p><p class="card-text"><small class="text-muted">Status: {s.status} Total votes : {total}</small></p></div><div class="progress" style="margin:2vh 10vw;"><div class="progress-bar progress-bar-striped progress-bar-animated"  role="progressbar" aria-valuenow="{votes}" aria-valuemin="0" aria-valuemax="100" style="width: {votes}%">{votes}%</div></div>{button}<br></div></div>'
         if s.status == 'Active':
            output[0] += c
         else:
            output[2] += c
         output[1] += c
         # print(c)
    return HttpResponse("##".join(output))



def vote(request):
    '''
        Updates student's choice of up/down voting Campaigns
        Return django.shortcuts.HttpResponse
    '''
    cid = request.POST.get("cid", "")
    v = request.POST.get("v", "")
    t = campaign.objects.get(id=int(cid))
    if str(v) == '0':
        t.dns += f',{request.session["student_id"]}'
    else:
        t.ups += f',{request.session["student_id"]}'
    t.save()
    return HttpResponse("")


def vote_admin(request):
    '''
        Updates Admin's choice of accepting/rejecting Campaigns
        Return django.shortcuts.HttpResponse
    '''
    cid = request.POST.get("cid", "")
    v = request.POST.get("v", "")
    t = campaign.objects.get(id=int(cid))
    if str(v) == '0':
        t.status = 'Rejected'
    else:
        t.status = 'Accepted'
    t.save()
    return HttpResponse("")

def logout_stu(request):
    '''
        Deletes Session for Student
        Return django.shortcuts.redirect object with login
    '''
    s = []
    for sesskey in request.session.keys():
        s.append(sesskey)
    for sesskey in s:
        del request.session[sesskey]
    return redirect(login)

def logout_admin(request):
    '''
        Deletes Session for Admin
        Return django.shortcuts.redirect object with /adminhome
    '''

    s = []
    for sesskey in request.session.keys():
        s.append(sesskey)
    for sesskey in s:
        del request.session[sesskey]
    return redirect(adminhome)



=======
def home(request):
    '''
        Loads Page to view Admin's home page
        Return django.shortcuts.render object with admin.html
    '''
    return render(request, 'home.html')
>>>>>>> 4a97713f1a1fe005134fd2c29ff509416f5334d3
