from django.conf.urls import patterns, include, url
from student.views.students import StudentUpdateView, StudentDeleteView
from student.views.groups import GroupDelete, GroupAddView, GroupUpdateView
from student.views.journal import JournalView


urlpatterns = patterns('',
	# Students urls
	url(r'^$', 'student.views.students.students_list', name='home'),
	url(r'^students/add/$', 'student.views.students.students_add', name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
	url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

	# Groups urls
	url(r'^groups/$', 'student.views.groups.groups_list', name='groups'),
	url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
	url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
	url(r'^groups/(?P<pk>\d+)/delete/$', GroupDelete.as_view(), name='groups_delete'),

	# Journal urls
	url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
	# Exam urls
	url(r'^exam/$', 'student.views.exam.exam_list', name='exam'),
	url(r'^exam/add/$', 'student.views.exam.exam_add', name='exam_add'),

	# Contact Admin Form
	url(r'^contact-admin/$', 'student.views.contact_admin.contact_admin', name='contact_admin'),

)

