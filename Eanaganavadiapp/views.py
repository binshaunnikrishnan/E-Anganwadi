from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

from Eanaganavadiapp.models import *

from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render




def logout(request):
    auth.logout(request)
    return render(request,'login.html')



def login(request):
    return render(request,"login.html")

def logincode(request):
    try:

        username = request.POST['textfield']
        pwd = request.POST['textfield2']
        ob = login_table.objects.get(username=username,password=pwd)
        if ob.type == "admin":
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("successfully");window.location="/admin_home"</script>''')
        elif ob.type == "staff":
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("successfully");window.location="/staff_home"</script>''')
        elif ob.type == "student":
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='123')
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("successfully");window.location="/parent_home"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid user......");window.location="/"</script>''')
    except Exception as e:
        print(e)
        return HttpResponse('''<script>alert("invalid user");window.location="/"</script>''')


def add_anganwadi(request):
    ob=anganwadi_table.objects.all()
    return render(request,"ADMIN/addanganwadi.html",{'val':ob})

@login_required(login_url='/')



def addangana(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    phone=request.POST['textfield5']
    email=request.POST['textfield6']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name, photo)
    ob=anganwadi_table()
    ob.anganwadiname=name
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.email=email
    ob.photo=fn
    ob.save()
    return HttpResponse('''<script>alert(" added");window.location="/manage_anganwadi#about"</script>''')

@login_required(login_url='/')












def edit_angan(request,id):
    ob=anganwadi_table.objects.get(id=id)
    request.session['aid']=ob.id
    return render(request, "ADMIN/edit_angan.html", {'val': ob})


@login_required(login_url='/')


def edited_angn(request):
    if 'file' in request.FILES:
        ob = anganwadi_table.objects.get(id= request.session['aid'])
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        phone = request.POST['textfield5']
        email = request.POST['textfield6']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        ob.anganwadiname = name
        ob.place = place
        ob.post = post
        ob.pin = pin
        ob.phone = phone
        ob.email = email
        ob.photo = fn
        ob.save()
        return HttpResponse('''<script>alert(" edited");window.location="/manage_anganwadi#about"</script>''')

    else:
        ob = anganwadi_table.objects.get(id= request.session['aid'])
        name = request.POST['textfield']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        phone = request.POST['textfield5']
        email = request.POST['textfield6']
        ob.anganwadiname = name
        ob.place = place
        ob.post = post
        ob.pin = pin
        ob.phone = phone
        ob.email = email
        ob.save()
        return HttpResponse('''<script>alert(" edited");window.location="/manage_anganwadi#about"</script>''')


@login_required(login_url='/')





def delete_anagn(request,id):
    ob=anganwadi_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert(" deleted");window.location="/manage_anganwadi#about"</script>''')


@login_required(login_url='/')


def manage_angan_search(request):
    name=request.POST['textfield']
    ob=anganwadi_table.objects.filter(anganwadiname__icontains=name)
    return render(request, "ADMIN/manageanganwadi.html", {'val': ob,'search':name})


@login_required(login_url='/')



def add_fooditem(request):
    ob=fooditems_table.objects.all()
    return render(request,"ADMIN/addfooditem.html",{'val':ob})

@login_required(login_url='/')


def add_items(request):
    time=request.POST['textfield']
    fooditem=request.POST['textfield2']
    day=request.POST['select']
    ob=fooditems_table()
    ob.fooditem=fooditem
    ob.time=time
    ob.day=day
    ob.save()
    return HttpResponse('''<script>alert(" added");window.location="/manage_foodschedule#about"</script>''')

@login_required(login_url='/')

def add_reply(request,id):
    ob=complaints_table.objects.get(id=id)
    request.session['comid']=ob.id
    return render(request,"ADMIN/addreply.html",{'val':ob})

@login_required(login_url='/')



def add_replyss(request):
    ob = complaints_table.objects.get(id= request.session['comid'])
    reply=request.POST['textfield']
    ob.reply=reply
    ob.save()
    return HttpResponse('''<script>alert(" added");window.location="/view_complaintssendreply#about"</script>''')


@login_required(login_url='/')



def add_staff(request):
    ob=staff_table.objects.all()
    return render(request,"ADMIN/addstaff.html",{'val':ob})
@login_required(login_url='/')

def addedstaff(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    age=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    phone=request.POST['textfield7']
    email=request.POST['textfield8']
    photo=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(photo.name,photo)
    username=request.POST['textfield9']
    pw=request.POST['textfield10']
    ob=login_table()
    ob.username=username
    ob.password=pw
    ob.type="staff"
    ob.save()
    obj=staff_table()
    obj.firstname=fname
    obj.lastname=lname
    obj.age=age
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.phone=phone
    obj.email=email
    obj.photo=fn
    obj.LOGIN=ob
    obj.save()
    return HttpResponse('''<script>alert("Added");window.location="/manage_staff#about"</script>''')

@login_required(login_url='/')



def edit_staffs(request,id):
    ob=staff_table.objects.get(id=id)
    request.session['sid']=ob.id
    return render(request,"ADMIN/edit_staff.html",{'val':ob})

@login_required(login_url='/')


def edit_staff(request):
    if 'files' in request.FILES:
        obj = staff_table.objects.get(id=request.session['sid'])
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        age = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        pin = request.POST['textfield6']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        obj.firstname = fname
        obj.lastname = lname
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.phone = phone
        obj.email = email
        obj.photo = fn
        obj.save()
        return HttpResponse('''<script>alert("sucsesfully edit staff");window.location="/manage_staff#about"</script>''')

    else:
        obj = staff_table.objects.get(id=request.session['sid'])
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        age = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        pin = request.POST['textfield6']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        obj.firstname = fname
        obj.lastname = lname
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.phone = phone
        obj.email = email
        obj.save()
        return HttpResponse(
            '''<script>alert("sucsesfully edit staff");window.location="/manage_staff#about"</script>''')


@login_required(login_url='/')




def delete_staff(request,id):
    ob=staff_table.objects.get(id=id)
    ob1=login_table.objects.get(id=ob.LOGIN.id)
    ob1.delete()
    return HttpResponse('''<script>alert("sucsesfully delete staff");window.location="/manage_staff#about"</script>''')

@login_required(login_url='/')


def add_staffanganwadi(request):
    ob=staff_table.objects.all()
    ok=anganwadi_table.objects.all()
    return render(request,"ADMIN/addstaff-anganwadi.html",{'val':ob,'va':ok})

@login_required(login_url='/')

def addedstaffanganwadi(request):
    staff=request.POST['st']
    anganwadi=request.POST['aw']
    ob=assign_table()
    ob.STAFF=staff_table.objects.get(id=staff)
    ob.ANGANWADI=anganwadi_table.objects.get(id=anganwadi)
    ob.date=datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/assign_stafftoanganwadi#about"</script>''')



def delete_staffanganwadi(request,id):
    ob=assign_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("delete");window.location="/assign_stafftoanganwadi#about"</script>''')





@login_required(login_url='/')


def add_syllabus(request):
    ob=syllabus_table.objects.all()
    return render(request,"ADMIN/addsyllabus.html",{'val':ob})
@login_required(login_url='/')


def addedsyllabus(request):
    subject=request.POST['textfield']
    syllabus=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(syllabus.name, syllabus)
    ob=syllabus_table()
    ob.subject=subject
    ob.syllabus=fn
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/syllabus_management#about"</script>''')

@login_required(login_url='/')

def edit_syllabus(request,id):
    ob=syllabus_table.objects.get(id=id)
    request.session['sid']=ob.id
    return render(request,"ADMIN/edit_sylabus.html",{'val':ob})
@login_required(login_url='/')

def edit_sylbus(request):
    if 'file' in request.FILES:
        ob = syllabus_table.objects.get(id=request.session['sid'])
        subject = request.POST['textfield']
        syllabus = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(syllabus.name, syllabus)
        ob.subject = subject
        ob.syllabus = fn
        ob.save()
        return HttpResponse('''<script>alert("edited");window.location="/syllabus_management#about"</script>''')

    else:
        ob = syllabus_table.objects.get(id=request.session['sid'])
        subject = request.POST['textfield']
        ob.subject = subject
        ob.save()
        return HttpResponse('''<script>alert("edited");window.location="/syllabus_management#about"</script>''')


@login_required(login_url='/')

def delete_sylubus(request,id):
    ob=syllabus_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location="/syllabus_management#about"</script>''')

@login_required(login_url='/')


def add_time(request):
    ob=workingtime_table.objects.all()
    return render(request,"ADMIN/addtime.html",{'val':ob})

@login_required(login_url='/')

def addedtime(request):
    fromtime=request.POST['textfield']
    totime=request.POST['textfield2']
    date=request.POST['date']
    ob=workingtime_table()
    ob.fromtime=fromtime
    ob.totime=totime
    ob.date=date
    ob.save()
    return HttpResponse('''<script>alert("Sucsesfully Added Working Time");window.location="/manage_workingtime#about"</script>''')

@login_required(login_url='/')


def delete_working_time(request,id):
    ob=workingtime_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Sucsesfully deleted Working Time");window.location="/manage_workingtime#about"</script>''')

@login_required(login_url='/')
def admin_home(request):
    return render(request,'index.html')


@login_required(login_url='/')
def assign_stafftoanganwadi(request):
    ob=assign_table.objects.all()
    return render(request,"ADMIN/assignstafftoanganwadi.html",{'val':ob})

@login_required(login_url='/')

def block_unblockstaff(request):
    ob=staff_table.objects.all()
    return render(request,"ADMIN/blockunblockstaff.html",{'val':ob})

@login_required(login_url='/')


def blockblk_staff_search(request):
    name=request.POST['textfield']
    ob=staff_table.objects.filter(firstname__icontains=name)
    return render(request,"ADMIN/blockunblockstaff.html",{'val':ob,'search':name})


@login_required(login_url='/')



def block_unblock_sraff(request):
    ob = login_table.objects.all()
    return render(request, "ADMIN/blockunblockstaff.html", {'val': ob})

@login_required(login_url='/')



def unblock_staff(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='staff'
    ob.save()
    return HttpResponse('''<script>alert("unblocked");window.location="/block_unblockstaff#about"</script>''')

@login_required(login_url='/')


def block_staff(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked");window.location="/block_unblockstaff#about"</script>''')

@login_required(login_url='/')


def manage_anganwadi(request):
    ob=anganwadi_table.objects.all()
    return render(request,"ADMIN/manageanganwadi.html",{'val':ob})

@login_required(login_url='/')

def manage_foodschedule(request):
    ob=fooditems_table.objects.all()
    return render(request,"ADMIN/managefood&schedule.html",{'val':ob})

def search_day(request):
    day=request.POST['day']
    ob=fooditems_table.objects.filter(day=day)
    return render(request,"ADMIN/managefood&schedule.html",{'val':ob,'search':ob,'day':day})


@login_required(login_url='/')


# def manage_foodschedule_search(request):


def edit_fooditem(request,id):
    ob=fooditems_table.objects.get(id=id)
    request.session['fid']=ob.id
    return render(request,"ADMIN/edit_fooditem.html",{'val':ob,'tm':str(ob.time)})

@login_required(login_url='/')


def edits_food(request):
    ob = fooditems_table.objects.get(id=request.session['fid'])
    time = request.POST['textfield']
    fooditem = request.POST['textfield2']
    day = request.POST['select']
    ob.fooditem = fooditem
    ob.time = time
    ob.day = day
    ob.save()
    return HttpResponse('''<script>alert(" edited");window.location="/manage_foodschedule#about"</script>''')

@login_required(login_url='/')


def delete_fditem(request,id):
    ob=fooditems_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert(" deleted");window.location="/manage_foodschedule#about"</script>''')

@login_required(login_url='/')



def manage_staff(request):
    ob=staff_table.objects.all()
    return render(request,"ADMIN/managestaff.html",{'val':ob})

@login_required(login_url='/')


def manage_staff_search(request):
    name=request.POST['textfield']
    ob=staff_table.objects.filter(firstname__icontains=name)
    return render(request,"ADMIN/managestaff.html",{'val':ob,'search':name})


@login_required(login_url='/')


def manage_workingtime(request):
    ob=workingtime_table.objects.all()
    return render(request,"ADMIN/manageworkingtime.html",{'val':ob})

@login_required(login_url='/')

def syllabus_management(request):
    ob=syllabus_table.objects.all()
    return render(request,"ADMIN/syllabusmanagement.html",{'val':ob})

@login_required(login_url='/')


def view_complaintssendreply(request):
    ob=complaints_table.objects.all()
    return render(request,"ADMIN/viewcomplaints&sendreply.html",{'val':ob})

@login_required(login_url='/')



def view_comp_search(request):
    date=request.POST['date']
    ob=complaints_table.objects.filter(date=date)
    return render(request,"ADMIN/viewcomplaints&sendreply.html",{'val':ob,'search':date})

@login_required(login_url='/')






#/////////////////////////// PARENT ////////////////////////////#

def add_feedbacks(request):
    ob=feedback_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request,"PARENT/addfeedback.html",{'val':ob})


@login_required(login_url='/')


def add_feedback(request):
    ob = feedback_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request, "PARENT/viewfeedbacks.html", {'val': ob})

@login_required(login_url='/')



def add_feed(request):
    rating=request.POST['select']
    feedback=request.POST['textfield2']
    ob=feedback_table()
    ob.rating=rating
    ob.feedback=feedback
    ob.date=datetime.now()
    ob.STUDENT=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("added");window.location='/add_feedback#about'</script>''')
@login_required(login_url='/')

#
#
# def add_feedback_search(request):
#     date=request.POST['date']
#     ob=feedback_table.objects.filter(date=date)
#     return render(request,"STAFF/viewfeedback.html",{'val':ob,'search':date})
#
#
#
#

def add_leaverequest(request):
    ob=leaverequest_table.objects.all()
    return render(request,"PARENT/addleaverequest.html",{'val':ob})

@login_required(login_url='/')


def add_requests(request):
    requestss=request.POST['textfield']
    ldate=request.POST['date']
    ob=leaverequest_table()
    ob.request=requestss
    ob.date=datetime.now()
    ob.levedate=ldate
    ob.STUDENT=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("added");window.location='/send_leaverequest#about'</script>''')

@login_required(login_url='/')



def edit_leaverequest(request,id):
    ob = leaverequest_table.objects.get(id=id)
    request.session['zid']=ob.id
    return render(request,"PARENT/edit_leve.html",{'val':ob})

@login_required(login_url='/')


def edit_leve(request):
    ob = leaverequest_table.objects.get(id= request.session['zid'])
    requestss = request.POST['textfield']
    ldate = request.POST['date']
    ob.request = requestss
    ob.date = datetime.now()
    ob.levedate = ldate
    ob.STUDENT = student_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("edited");window.location='/send_leaverequest#about'</script>''')

@login_required(login_url='/')


def delete_leave(request,id):
    ob=leaverequest_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/send_leaverequest#about'</script>''')

@login_required(login_url='/')


def parent_home(request):
    return render(request,"indexparent.html")

@login_required(login_url='/')


def send_complaint(request):
    return render(request,"PARENT/sendcomplaint.html")

@login_required(login_url='/')


def addnewcomplaint(request):
    ob = complaints_table.objects.all()
    return render(request,"PARENT/sendcomplaints&viewreply.html",{'val':ob})
@login_required(login_url='/')


def addnewcomp(request):
    comp = request.POST['textfield']
    obj = complaints_table()
    obj.complaint = comp
    obj.date = datetime.today()
    obj.reply = 'pending'
    obj.STUDENT= student_table.objects.get(LOGIN__id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("sended");window.location='/addnewcomplaint#about'</script>''')

@login_required(login_url='/')


def send_complaintviewreply(request):
    ob=complaints_table.objects.all()
    return render(request,"PARENT/sendcomplaints&viewreply.html",{'val':ob})

@login_required(login_url='/')


def send_leaverequest(request):
    ob=leaverequest_table.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request,"PARENT/sendleaverequest.html",{'val':ob})

@login_required(login_url='/')


def view_fooditemsschedule(request):
    ob=fooditems_table.objects.all()
    return render(request,"PARENT/viewfooditems&schedule.html",{'val':ob})

@login_required(login_url='/')

def view_notesvideos(request):
    os=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob=studymaterials_table.objects.filter(STAFF__id=os.STAFF.id)
    return render(request,"PARENT/viewnotes&videos.html",{'val':ob})

@login_required(login_url='/')


def view_studentdetails(request):
    ob=student_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"PARENT/viewstudentdetails.html",{'val':ob})

@login_required(login_url='/')


def view_workingtime(request):
    ob=workingtime_table.objects.all()
    return render(request,"PARENT/viewworkingtime.html",{'val':ob})



@login_required(login_url='/')








#/////////////////////////// STAFF ////////////////////////////#

def add_student(request):
    ob=student_table.objects.filter(STAFF__id=request.session['lid'])
    return render(request,"STAFF/addstudent.html",{'val':ob})

@login_required(login_url='/')

def addstudent(request):
    fnm=request.POST['textfield']
    lnm=request.POST['textfield2']
    age=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    pin=request.POST['textfield6']
    phone=request.POST['textfield7']
    email=request.POST['textfield8']
    pnme=request.POST['textfield9']
    photo=request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name, photo)
    um=request.POST['textfield10']
    psd=request.POST['textfield11']

    ob=login_table()
    ob.username=um
    ob.password=psd
    ob.type='student'
    ob.save()

    obj=student_table()
    obj.firstname=fnm
    obj.lastname=lnm
    obj.age=age
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.photo=fn
    obj.phone=phone
    obj.email=email
    obj.parentname=pnme
    obj.LOGIN=ob
    obj.STAFF=staff_table.objects.get(LOGIN__id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert(" sucsesfully added");window.location="/manage_studentdetails#about"</script>''')


@login_required(login_url='/')





def edit_student(request,id):
    ob=student_table.objects.get(id=id)
    request.session['eid']=ob.id
    return render(request,"STAFF/edit_student.html",{'val':ob})


@login_required(login_url='/')


def edit_studentss(request):
    if 'file' in request.FILES:
        obj = student_table.objects.get(id=request.session['eid'])
        fnm = request.POST['textfield']
        lnm = request.POST['textfield2']
        age = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        pin = request.POST['textfield6']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        pnme = request.POST['textfield9']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        obj.firstname = fnm
        obj.lastname = lnm
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.photo = fn
        obj.phone = phone
        obj.email = email
        obj.parentname = pnme
        obj.save()
        return HttpResponse('''<script>alert(" sucsesfully edited");window.location="/manage_studentdetails#about"</script>''')
    else:
        obj = student_table.objects.get(id=request.session['eid'])
        fnm = request.POST['textfield']
        lnm = request.POST['textfield2']
        age = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        pin = request.POST['textfield6']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        pnme = request.POST['textfield9']
        obj.firstname = fnm
        obj.lastname = lnm
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.phone = phone
        obj.email = email
        obj.parentname = pnme
        obj.save()
        return HttpResponse( '''<script>alert(" sucsesfully edited");window.location="/manage_studentdetails#about"</script>''')

@login_required(login_url='/')



def delete_studentsss(request,id):
    ob=student_table.objects.get(id=id)
    ob1=login_table.objects.get(id=ob.LOGIN.id)
    ob1.delete()
    return HttpResponse('''<script>alert(" sucsesfully deleted");window.location="/manage_studentdetails#about"</script>''')



@login_required(login_url='/')



def add_studymaterials(request):
    ob=studymaterials_table.objects.all()
    return render(request,"STAFF/addstudymaterials.html",{'val':ob})


@login_required(login_url='/')


def add_smaterials(request):
    materials=request.FILES['file']
    tile=request.POST['textfield']
    fs = FileSystemStorage()
    fn = fs.save(materials.name, materials)
    ob=studymaterials_table()
    ob.studymaterials=fn
    ob.title=tile
    ob.STAFF=staff_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert(" sucsesfully added");window.location="/upload_studynotesvideos#about"</script>''')

@login_required(login_url='/')


def delete_materials(request,id):
    ob=studymaterials_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert(" sucsesfully delete");window.location="/upload_studynotesvideos#about"</script>''')


@login_required(login_url='/')



def manage_studentdetails(request):
    ob=student_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request,"STAFF/managestudentdetails.html",{'val':ob})


@login_required(login_url='/')


def student_search(request):
    name=request.POST['textfield']
    ob=student_table.objects.filter(firstname__icontains=name)
    return render(request,"STAFF/managestudentdetails.html",{'val':ob,'search':name})

@login_required(login_url='/')



def staff_home(request):
    return render(request,"indexstaff.html")

@login_required(login_url='/')


def upload_studynotesvideos(request):
    ob=studymaterials_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request,"STAFF/uploadstudynotes&videos.html",{'val':ob})
@login_required(login_url='/')


#
# def View_Syllabus(request):
#     ob=syllabus_table.objects.all()
#     return render(request,"STAFF/View Syllabus.html",{'val':ob})

def view_assignedanganwadi(request):
    ob=assign_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request,"STAFF/viewassignedanganwadi.html",{'val':ob})
@login_required(login_url='/')





def view_feedback(request):
    ob=feedback_table.objects.filter(STUDENT__STAFF__LOGIN__id=request.session['lid'])
    return render(request,"STAFF/viewfeedback.html",{'val':ob})
@login_required(login_url='/')



def view_feedback_search(request):
    date=request.POST['date']
    ob=feedback_table.objects.filter(date=date)
    return render(request,"STAFF/viewfeedback.html",{'val':ob,'search':date})





@login_required(login_url='/')



def view_feedback_searchs(request):
    date=request.POST['date']
    ob=feedback_table.objects.filter(date=date)
    return render(request,"PARENT/viewfeedbacks.html",{'val':ob,'search':date})


@login_required(login_url='/')




def view_fooditemsschedules(request):
    ob=fooditems_table.objects.all()
    return render(request, "STAFF/viewfooditems&schedules.html", {'val':ob})

@login_required(login_url='/')



def view_leaverequest(request):
    ob=leaverequest_table.objects.filter(STUDENT__STAFF__LOGIN__id=request.session['lid'])
    return render(request,"STAFF/viewleaverequest.html",{'val':ob})

@login_required(login_url='/')



def view_profilestaff(request):
    ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"STAFF/viewprofile.html",{'val':ob})




@login_required(login_url='/')



def updatestaff(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    age = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    phone = request.POST['textfield7']
    email = request.POST['textfield8']
    photo = request.FILES['file']
    fs = FileSystemStorage()
    fn = fs.save(photo.name, photo)


    obj = staff_table.objects.get(LOGIN__id=request.session['lid'])
    obj.firstname = fname
    obj.lastname = lname
    obj.age = age
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.phone = phone
    obj.email = email
    obj.photo = fn
    obj.LOGIN = ob
    obj.save()

@login_required(login_url='/')



def updatep(request):
    ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"STAFF/updateprofile.html",{'val':ob})

@login_required(login_url='/')

def viewP_search(request):
    name=request.POST['textfield']
    ob=staff_table.objects.filter(firstname__icontains=name)
    return render(request,"STAFF/viewprofile-staff.html",{'val':ob,'search':name})

@login_required(login_url='/')


def update_staffss(request):
    ob=staff_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request,"STAFF/edit_staffs.html",{'val':ob})

@login_required(login_url='/')


def upd_staf(request):
    if 'file' in request.FILES:
        obj = staff_table.objects.get(LOGIN__id=request.session['lid'])
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        age = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        pin = request.POST['textfield6']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        photo = request.FILES['file']
        fs = FileSystemStorage()
        fn = fs.save(photo.name, photo)
        obj.firstname = fname
        obj.lastname = lname
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.phone = phone
        obj.email = email
        obj.photo = fn
        obj.save()
        return HttpResponse('''<script>alert("sucsesfully update staff");window.location="/view_profilestaff#about"</script>''')
    else:
        obj = staff_table.objects.get(LOGIN__id=request.session['lid'])
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        age = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        pin = request.POST['textfield6']
        phone = request.POST['textfield7']
        email = request.POST['textfield8']
        obj.firstname = fname
        obj.lastname = lname
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.phone = phone
        obj.email = email
        obj.save()
        return HttpResponse('''<script>alert("sucsesfully update staff");window.location="/view_profilestaff#about"</script>''')


@login_required(login_url='/')

#
#

def view_syllabus(request):
    ob=syllabus_table.objects.all()
    return render(request,"STAFF/viewsyllabus.html",{'val':ob})


@login_required(login_url='/')


def view_workingtimes(request):
    ob=workingtime_table.objects.all()
    return render(request,"STAFF/viewworkingtime.html",{'val':ob})


@login_required(login_url='/')




# chat----------------------------

def chatwithuser(request):
    ob = student_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    return render(request,"STAFF/fur_chat.html",{'val':ob})




def chatview(request):
    ob = student_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    d=[]
    for i in ob:
        r={"name":i.firstname+i.lastname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat_table()
    ob.fromid=login_table.objects.get(id=request.session['lid'])
    ob.toid=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=chat_table.objects.filter(fromid__id=id,toid__id=request.session['lid'])
    ob2=chat_table.objects.filter(fromid__id=request.session['lid'],toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.fromid.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=student_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.firstname+obu.lastname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})






def chatwithstaff(request):
    obj=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob = staff_table.objects.filter(id=obj.STAFF.id)
    return render(request,"PARENT/fur_chat.html",{'val':ob})




def chatviews(request):
    obj=student_table.objects.get(LOGIN__id=request.session['lid'])
    ob = staff_table.objects.filter(id=obj.STAFF.id)
    d=[]
    for i in ob:
        r={"name":i.firstname+i.lastname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)

#
# def coun_insert_chat(request,msg,id):
#     print("===",msg,id)
#     ob=chat_table()
#     ob.fromid=login_table.objects.get(id=request.session['lid'])
#     ob.toid=login_table.objects.get(id=id)
#     ob.message=msg
#     ob.date=datetime.now().strftime("%Y-%m-%d")
#     ob.save()
#
#     return JsonResponse({"task":"ok"})
#     # refresh messages chatlist



def coun_msgs(request,id):

    ob1=chat_table.objects.filter(fromid__id=id,toid__id=request.session['lid'])
    ob2=chat_table.objects.filter(fromid__id=request.session['lid'],toid__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.fromid.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=staff_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.firstname+obu.lastname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})









