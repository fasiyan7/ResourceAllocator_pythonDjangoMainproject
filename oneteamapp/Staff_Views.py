from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages


from oneteamapp.models import Assignment, CustomUser, Staff,Post

@login_required(login_url='/')	
def HOME(request):
    return render(request,'indexoffaculty.html')   

def STAFF_DETAIL(request,staff_id):
    #staff = Staff.objects.all()  
    user = CustomUser.objects.get(id =staff_id)
    staff = Staff.objects.filter(admin_id =user.id)
    context = {
    'staff':staff,
    }
    return render(request,'Staff/view_staff.html',context)
def ADDPOST(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        created = request.POST.get('created')
        post = Post(
            title = title,
            content=content,
            created=created
        )
        post.save()
        messages.success(request,'Success')
        return redirect('addpost')
  

			
    return render(request,'Staff/staffpost.html')
def REMOVEPOSTnot(request):
		remove_posts=Post.objects.all()
		context={
		'posts':remove_posts
		}
		return render(request,'Staff/removepost.html',context)

def REMOVEPOST(request,post_id=0):
	if post_id:
		try:
			post_removed=Post.objects.get(id=post_id)
			post_removed.delete()
			return HttpResponse("Post removed Successfully")
		except:
			return HttpResponse("please enter a valid ID")
	remove_posts=Post.objects.all()
	context={
		'posts':remove_posts
	}
	return render(request,'Staff/removepost.html',context)
def ADDASSIGNMENT(request):		
		if request.method=='POST':
			title=request.POST.get('title')
			content=request.POST.get('content')
			assigntopic=request.POST.get('assigntopic')
			created=request.POST.get('created')
			enddate=request.POST.get('enddate')
			new_assignment=Assignment(
				title=title,content=content,assigntopic=assigntopic,created=created,enddate=enddate)
			#new_assignment=Post(title=title,content=content,created=created,enddate=enddate)

			print(new_assignment)
			new_assignment.save()
			return HttpResponse("A Assignment is Added Successfully")
			
		elif request.method=='GET':
			return render(request,'Staff/addassignment.html')
		else:
			return HttpResponse("An Exception")
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

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        staff = Staff.objects.get(admin =staff_id)
        staff.address = address
        staff.gender = gender
        staff.save()
        messages.success(request,' Details Updated !')
	
    return render(request,'Staff/view_staff.html')

def REMOVEASSIGNMENTnot(request):
        remove_assignment=Assignment.objects.all()
        context={
		'removeassignments':remove_assignment
	    }
        return render(request,'Staff/removeassignment.html',context)

def REMOVEASSIGNMENT(request,assignment_id=0):
	if assignment_id:
		try:
			assignment_removed=Assignment.objects.get(id=assignment_id)
			print("done",assignment_removed)
			assignment_removed.delete()
			return HttpResponse("Assignment removed Successfully")
		except:
			return HttpResponse("please enter a valid ID")
	
	removeassignment=Assignment.objects.all()
	context={
		'removeassignments':removeassignment
	}

	return render(request,'Staff/removeassignment.html',context)



	
















