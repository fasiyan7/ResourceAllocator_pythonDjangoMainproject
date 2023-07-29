
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template import Engine
from oneteamapp.models import Batches, Course, Hall, Laptop,Session_Year,CustomUser, Staff,Student
from django.contrib import messages


@login_required(login_url='/')	
def HOME(request):
    return render(request,'Hod/home.html')   

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists():
           messages.error(request,'Email Is Already Taken')
           return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
           messages.error(request,'Username Is Already Taken')
           return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')



    context = {
        'course':course,
        'session_year':session_year,
    }

    return render(request,'Hod/add_student.html',context)
@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'Hod/view_student.html',context)
@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'Hod/edit_student.html',context)
@login_required(login_url='/')

def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_student')

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'Hod/edit_student.html')
	
@login_required(login_url='/')
def ADD_COURSE(request):

    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Are Successfully Created ')
        return redirect('view_course')
    return render(request,'Hod/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'Hod/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)
    context = {
        'course':course,
    }
    return render(request,'Hod/edit_course.html',context)

		   

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        course_id = request.POST.get('course_id')
        name = request.POST.get('name')
        course = Course.objects.get(id = course_id)
        course.name=name
        course.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_course')

    return render(request,'Hod/edit_course.html')
@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course is Successfully Deleted')

    return redirect('view_course')


@login_required(login_url='/')
def ADD_STAFF(request):

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        gender = request.POST.get('gender')
        if CustomUser.objects.filter(email=email).exists():
           messages.error(request,'Email Is Already Taken')
           return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
           messages.error(request,'Username Is Already Taken')
           return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            staff = Staff(
                admin = user,
                phone=phone,
                address = address,
                gender = gender,
            )
            staff.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_staff')
    return render(request,'Hod/add_staff.html')
@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff':staff,
    }
    return render(request,'Hod/view_staff.html',context)




def EDIT_STAFF(request,id):
    staff = Staff.objects.filter(id = id)
    
    context = {
               'staff':staff,
}
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
def DELETE_STAFF(request,id):
    staff = Staff.objects.get(id =id)
    staff.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_staff')

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        user = CustomUser.objects.get(id = staff_id)
        print(user)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()

        if password != None and password != "":
            user.set_password(password)
            user.save()

        staff= Staff.objects.get(admin =staff_id)
        print(staff)
        staff.address = address
        staff.gender = gender
        staff.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_staff')

    return render(request,'Hod/edit_staff.html')   


def Add_LAPTOP(request):

    if request.method == "POST":
        lap_name = request.POST.get('lapname')

        laptop = Laptop(
            lapname = lap_name,
        )
        laptop.save()
        messages.success(request,'Laptop name is saved Successfully')
        return redirect('add_lap')
    return render(request,'Hod/add_lap.html')

#def VIEW_LAPTOP(request):
def VIEW_LAPTOP(request):
    laptop = Laptop.objects.all()

    context = {
        'laptop':laptop,
    }
    return render(request,'Hod/view_lap.html',context)

def DELETE_LAPTOP(request,id):
    laptop = Laptop.objects.get(id = id)
    laptop.delete()
    messages.success(request,'Laptop is Successfully Deleted')

    return redirect('view_lap')

def Add_HALL(request):

    if request.method == "POST":
        hall_name = request.POST.get('hallname')

        hall = Hall(
            hallname = hall_name,
        )
        hall.save()
        messages.success(request,'Confernece room is saved Successfully')
        return redirect('add_hall')
    return render(request,'Hod/add_hall.html')

#def VIEW_LAPTOP(request):
def VIEW_HALL(request):
    print("hai")
    hall = Hall.objects.all()
    print(hall)

    context = {
        'halls':hall,
    }
    return render(request,'Hod/view_hall.html',context)

def DELETE_HALL(request,id):
    hall = Hall.objects.get(id = id)
    hall.delete()
    messages.success(request,'Conference Room  is Successfully Deleted')

    return redirect('view_hall')

    
def Add_BATCH(request):
    course = Course.objects.all()
    staff = Staff.objects.all()
    laptop = Laptop.objects.all()
    hall = Hall.objects.all()
    #student = Student.objects.all()

    context = {
        'courses':course,
        'staffes':staff,
        'laptops':laptop,
        'halls':hall,
       # 'students':student

    }
    if request.method== "POST":
        batch_name = request.POST.get('batchname')
        course_id = request.POST.get('coursename')
        course = Course.objects.get(id=course_id)
        staff_id = request.POST.get('staffname')
        staff = Staff.objects.get(id = staff_id)
        laptop_id = request.POST.get('lapname')
        laptop= Laptop.objects.get(id =laptop_id)
        print(laptop_id)
        hall_id = request.POST.get('hallname')
        hall= Hall.objects.get(id =hall_id)
        
        startdates=request.POST.get('startdate')
        enddates= request.POST.get('enddate')

        '''std_id = request.POST.get('stdname')
        student = CustomUser.objects.get(id = std_id)
        print(student)'''

        batch = Batches(
            batchname=batch_name,
            course_id=course,
            staff_id=staff,
            laptop_id=laptop,
            hall_id=hall,
            #starttime=startdates,
            #endtime=enddates
           # admin_id =student,
            )
        batch.save()
        messages.success(request," New Batch is successfully Adde !")
        return redirect('add_batch')
  
    return render(request,'Hod/add_batch.html',context)

def VIEW_BATCH(request):
    batch = Batches.objects.all()
    context = {
        'batchs':batch,
    }
    return render(request,'Hod/view_batch.html',context)

def DELETE_BATCH(request,id):
    batch = Batches.objects.get(id = id)
    batch.delete()
    messages.success(request,'Batch is Successfully Deleted')

    return redirect('view_batch')





    

    
