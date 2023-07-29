from django.urls import include, path

from oneteamapp import Hod_Views, Staff_Views, Student_Views
from .import views


urlpatterns = [

	path('',views.LOGIN,name='login'),
    path('Homefaculty',views.index,name='index'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('dologout',views.dologout,name='logout'),
    path('profile',views.PROFILE,name='profile'),
    path('Test',views.Test,name='test'),

    #CouseCouncellor
    path('Hod/Home',Hod_Views.HOME,name='hodhome'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),
    path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Course/Add',Hod_Views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_Views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name='delete_course'),
    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Delete/<str:id>',Hod_Views.DELETE_STAFF,name='delete_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Batch/Add',Hod_Views.Add_BATCH,name='add_batch'),
    path('Hod/Laptop/Add',Hod_Views.Add_LAPTOP,name='add_lap'),
    path('Hod/Laptop/view',Hod_Views.VIEW_LAPTOP,name='view_lap'),
    path('Hod/Laptop/Delete/<str:id>',Hod_Views.DELETE_LAPTOP,name='delete_lap'),

    path('Hod/Hall/Add',Hod_Views.Add_HALL,name='add_hall'),
    path('Hod/Hall/view',Hod_Views.VIEW_HALL,name='view_hall'),
    path('Hod/Hall/Delete/<str:id>',Hod_Views.DELETE_HALL,name='delete_hall'),

    path('Hod/Batch/view',Hod_Views.VIEW_BATCH,name='view_batch'),
    path('Hod/Batch/Delete/<str:id>',Hod_Views.DELETE_BATCH,name='delete_batch'),


    #staff
    path('Staff/Home',Staff_Views.HOME,name='staffhome'),
    path('Staff/viewdetails/<int:staff_id>',Staff_Views.STAFF_DETAIL,name='staffdetail'),

    path('Staff/addpost',Staff_Views.ADDPOST,name='addpost'),
    
    path('Staff/removepost',Staff_Views.REMOVEPOSTnot,name='removepost'),
    path('Staff/removepost/<int:post_id>',Staff_Views.REMOVEPOST,name='removepost'),

    path('Staff/addassignment',Staff_Views.ADDASSIGNMENT,name='addassignment'),

    path('Staff/removeassignment',Staff_Views.REMOVEASSIGNMENTnot,name='removeassignment'),
    path('Staff/removeassignment/<int:assignment_id>',Staff_Views.REMOVEASSIGNMENT,name='removeassignment'),


    path('Staff/Logout',views.dologout,name='stafflogout'),
    path('Staff/Update',Staff_Views.UPDATE_STAFF,name='updatestaff'),


    #student
    
    path('Student/Home',Student_Views.HOME,name='studenthome'),
    path('Student/viewdetails/<int:student_id>',Student_Views.STUDENT_DETAIL,name='studentdetails'), #using id important code
    path('Student/Logout',views.dologout,name='studentlogout'),
    path('Student/Update',Student_Views.UPDATE_STUDENT,name='updatestudent'),
    path('Student/Payment',Student_Views.PAYMENT,name='payment'),
    path('paymenthandler/', Student_Views.paymenthandler, name='paymenthandler'),
    path('Student/Success',Student_Views.SUCCESS,name='Success'),
















]
