# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models import Student, Group, MonthJournal, Exam

class StudentFormAdmin(ModelForm):
	def clean_student_group(self):
		"""Check if student is leader in any group.
		If yes, then ensure it's the same as selected group."""
		# get group where current student is a leader
		groups = Group.objects.filter(leader=self.instance)
		if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
			raise ValidationError(u'Студент є старостою іншої групи.', code='invalid')
		return self.cleaned_data['student_group']

# class for add a parametres to register models
class StudentAdmin(admin.ModelAdmin): # inheritance from django.contrib.admin
	list_display = ('first_name', 'last_name', 'ticket', 'student_group') # display a table in admin
	list_display_links = ['last_name', 'first_name']
	list_per_page = 10
	list_editable = ['student_group']
	list_filter = ['student_group'] # filter by value in this fields
	search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes'] # searching in tables
	date_hierarchy = ('birthday') # filter by date
	ordering = ('last_name',) # sorted by last_name in admin site
	#fields = ('first_name', 'last_name', 'ticket', 'birthday', 'middle_name') # exclude other field if need in admin site
	form = StudentFormAdmin

	def view_on_site(self, obj):
	    return reverse('students_edit', kwargs={'pk': obj.id})

class GroupAdmin(admin.ModelAdmin): # inheritance from django.contrib.admin
	list_display = ('title', 'leader', 'notes') # display a table in admin
	list_display_links = ['title']
	list_per_page = 10
	list_editable = ['leader']
	list_filter = ['leader'] # filter by value in this fields
	search_fields = ['title', 'leader', 'notes'] # searching in tables
	#date_hierarchy = ('leader.birthday') # filter by date
	ordering = ('leader',) # sorted by last_name in admin site

	def view_on_site(self, obj):
	    return reverse('groups_edit', kwargs={'pk': obj.id})


admin.site.register(Student, StudentAdmin) # add a parametrs to register
admin.site.register(Group, GroupAdmin)
admin.site.register(MonthJournal)
admin.site.register(Exam)
