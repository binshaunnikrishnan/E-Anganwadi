"""Eanganavadi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Eanaganavadiapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logincode', views.logincode, name="logincode"),
    path('logout', views.logout, name="logout"),
    path('add_items', views.add_items, name="add_items"),
    path('view_comp_search', views.view_comp_search, name="view_comp_search"),
    path('add_replyss', views.add_replyss, name="add_replyss"),
    path('add_anganwadi', views.add_anganwadi, name="add_anganwadi"),
    path('add_fooditem', views.add_fooditem, name="add_fooditem"),
    path('add_reply/<int:id>', views.add_reply, name="add_reply"),
    path('add_staff', views.add_staff, name="add_staff"),
    path('addedstaff', views.addedstaff, name="addedstaff"),
    path('add_staffanganwadi', views.add_staffanganwadi, name="add_staffanganwadi"),
    path('addedstaffanganwadi', views.addedstaffanganwadi, name="addedstaffanganwadi"),
    path('add_syllabus', views.add_syllabus, name="add_syllabus"),
    path('addedsyllabus', views.addedsyllabus, name="addedsyllabus"),
    path('add_time', views.add_time, name="add_time"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('assign_stafftoanganwadi', views.assign_stafftoanganwadi, name="assign_stafftoanganwadi"),
    path('block_unblockstaff', views.block_unblockstaff, name="block_unblockstaff"),
    path('manage_anganwadi', views.manage_anganwadi, name="manage_anganwadi"),
    path('manage_foodschedule', views.manage_foodschedule, name="manage_foodschedule"),
    path('manage_staff', views.manage_staff, name="manage_staff"),
    path('manage_workingtime', views.manage_workingtime, name="manage_workingtime"),
    path('syllabus_management', views.syllabus_management, name="syllabus_management"),
    path('view_complaintssendreply', views.view_complaintssendreply, name="view_complaintssendreply"),

    path('search_day',views.search_day,name="search_day"),
    path('add_feedback',views.add_feedback,name="add_feedback"),
    path('add_leaverequest',views.add_leaverequest,name="add_leaverequest"),
    path('parent_home',views.parent_home,name="parent_home"),
    path('send_complaint',views.send_complaint,name="send_complaint"),
    path('send_complaintviewreply',views.send_complaintviewreply,name="send_complaintviewreply"),
    path('send_leaverequest',views.send_leaverequest,name="send_leaverequest"),
    path('view_fooditemsschedule',views.view_fooditemsschedule,name="view_fooditemsschedule"),
    path('view_notesvideos',views.view_notesvideos,name="view_notesvideos"),
    path('view_studentdetails',views.view_studentdetails,name="view_studentdetails"),
    path('view_workingtime',views.view_workingtime,name="view_workingtime"),
    path('manage_staff_search',views.manage_staff_search,name="manage_staff_search"),
    path('blockblk_staff_search',views.blockblk_staff_search,name="blockblk_staff_search"),
    path('addedtime',views.addedtime,name="addedtime"),
    path('edits_food',views.edits_food,name="edits_food"),
    path('edit_sylbus',views.edit_sylbus,name="edit_sylbus"),
    path('addangana',views.addangana,name="addangana"),
    path('edited_angn',views.edited_angn,name="edited_angn"),
    path('manage_angan_search',views.manage_angan_search,name="manage_angan_search"),
    path('view_feedback_search',views.view_feedback_search,name="view_feedback_search"),
    path('add_smaterials',views.add_smaterials,name="add_smaterials"),

    path('add_student', views.add_student, name="add_student"),
    path('updatestaff', views.updatestaff, name="updatestaff"),
    path('updatep', views.updatep, name="updatep"),
    path('edit_studentss', views.edit_studentss, name="edit_studentss"),
    path('add_studymaterials', views.add_studymaterials, name="add_studymaterials"),
    path('addstudent', views.addstudent, name="addstudent"),
    path('manage_studentdetails', views.manage_studentdetails, name="manage_studentdetails"),
    path('staff_home', views.staff_home, name="staff_home"),
    path('upload_studynotesvideos', views.upload_studynotesvideos, name="upload_studynotesvideos"),
    # path('View_Syllabus', views.View_Syllabus, name="View_Syllabus"),
    path('view_assignedanganwadi', views.view_assignedanganwadi, name="view_assignedanganwadi"),
    path('view_feedback', views.view_feedback, name="view_feedback"),
    path('view_feedback_searchs', views.view_feedback_searchs, name="view_feedback_searchs"),
    path('add_requests', views.add_requests, name="add_requests"),
    path('student_search', views.student_search, name="student_search"),
    path('edit_leve', views.edit_leve, name="edit_leve"),
    path('view_fooditemsschedules', views.view_fooditemsschedules, name="view_fooditemsschedules"),
    path('view_leaverequest', views.view_leaverequest, name="view_leaverequest"),
    path('view_profilestaff', views.view_profilestaff, name="view_profilestaff"),
    path('view_syllabus', views.view_syllabus, name="view_syllabus"),
    path('viewP_search', views.viewP_search, name="viewP_search"),
    path('view_workingtimes', views.view_workingtimes, name="view_workingtimes"),
    path('block_unblock_sraff', views.block_unblock_sraff, name="block_unblock_sraff"),
    path('edit_staff', views.edit_staff, name="edit_staff"),
    # path('view_P', views.view_P, name="view_P"),
    path('add_feedbacks', views.add_feedbacks, name="add_feedbacks"),
    path('add_feed', views.add_feed, name="add_feed"),
    path('addnewcomplaint', views.addnewcomplaint, name="addnewcomplaint"),
    path('addnewcomp', views.addnewcomp, name="addnewcomp"),
    path('upd_staf', views.upd_staf, name="upd_staf"),
    path('unblock_staff/<int:id>', views.unblock_staff, name="unblock_staff"),
    path('block_staff/<int:id>', views.block_staff, name="block_staff"),
    path('edit_leaverequest/<int:id>', views.edit_leaverequest, name="edit_leaverequest"),
    path('edit_staffs/<int:id>', views.edit_staffs, name="edit_staffs"),
    path('delete_staff/<int:id>', views.delete_staff, name="delete_staff"),
    path('delete_working_time/<int:id>', views.delete_working_time, name="delete_working_time"),
    path('edit_fooditem/<int:id>', views.edit_fooditem, name="edit_fooditem"),
    path('delete_fditem/<int:id>', views.delete_fditem, name="delete_fditem"),
    path('edit_syllabus/<int:id>', views.edit_syllabus, name="edit_syllabus"),
    path('delete_sylubus/<int:id>', views.delete_sylubus, name="delete_sylubus"),
    path('edit_angan/<int:id>', views.edit_angan, name="edit_angan"),
    path('delete_anagn/<int:id>', views.delete_anagn, name="delete_anagn"),
    path('delete_materials/<int:id>', views.delete_materials, name="delete_materials"),
    path('edit_student/<int:id>', views.edit_student, name="edit_student"),
    path('delete_studentsss/<int:id>', views.delete_studentsss, name="delete_studentsss"),
    path('delete_leave/<int:id>', views.delete_leave, name="delete_leave"),
    path('update_staffss', views.update_staffss, name="update_staffss"),
    path('delete_staffanganwadi/<int:id>', views.delete_staffanganwadi, name="delete_staffanganwadi"),




    path('chatwithuser', views.chatwithuser, name='chatwithuser'),
    path('chatview', views.chatview, name='chatview'),
    path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
    path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),





    path('chatwithstaff', views.chatwithstaff, name='chatwithstaff'),
    path('chatviews', views.chatviews, name='chatviews'),
    path('coun_msgs/<int:id>', views.coun_msgs, name='coun_msgs'),

    ]
