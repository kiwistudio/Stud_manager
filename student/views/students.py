# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Student, Group
from ..util import paginate, get_current_group
#from django.contrib import messages


# Views for Students
def students_list(request):
    students = Student.objects.all()
    
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        # otherwise show all students
        students = Student.objects.all()

	# try to order students list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket', 'id'):
		students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()

	# apply pagination, 3 students per page
    context = paginate(students, 3, request, {},
        var_name='students') 
	
    return render(request, 'students/students_list.html', context)


def students_add(request):
	# was form posted?
	if request.method == "POST":
		# was form add button clicked?

		if request.POST.get('add_button') is not None:

			# errors collection
			errors = {}

			# validate student data will go here
			data = {'middle_name': request.POST.get('middle_name'),
				    'notes': request.POST.get('notes')}
			
			# validate user input
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Ім'я є обов'язковим"
			else:
				data['first_name'] = first_name

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Прізвище є обов'язковим"
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u"Дата народження є обов'язковою"
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception:
					errors['birthday'] = u"Введіть коректний формат дати (напр. 1984-12-30)"
				else:
					data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u"Номер білета є обов'язковим"
			else:
				data['ticket'] = ticket
			
			student_group = request.POST.get('student_group', '').strip()
			if not student_group:
				errors['student_group'] = u"Оберіть групу для студента"
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = u"Оберіть коректну групу"
				else:
					data['student_group'] = groups[0]
				
			photo = request.FILES.get('photo')			
			if photo:
				data['photo'] = photo

			# save student
			if not errors:
				student = Student(**data)
				student.save()	
				messages.success(request, u'Студента %s %s успішно додано!' % (data['first_name'], data['last_name']))
				# redirect to students list
				return HttpResponseRedirect(reverse('home'))
			else:
				# render form with errors and previous user input
				return render(request, 'students/students_add.html',
					{'groups': Group.objects.all().order_by('title'), 'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			messages.info(request, u'Додавання студента скасовано!')
			return HttpResponseRedirect(u'%s' % reverse('home'))
	else:
		# initial form render
		return render(request, 'students/students_add.html',
			{'groups': Group.objects.all().order_by('title')})


class StudentUpdateForm(ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'ticket', 'photo', 'student_group', 'notes']

    def __init__(self, *args, **kwargs):
	    super(StudentUpdateForm, self).__init__(*args, **kwargs)

	    self.helper = FormHelper(self)

	        # set form tag attributes
	    self.helper.form_action = reverse('students_edit', kwargs={'pk': kwargs['instance'].id})
	    self.helper.form_method = 'POST'
	    self.helper.form_class = 'form-horizontal'

	        # set form field properties
	    self.helper.help_text_inline = True
	    self.helper.html5_required = True
	    self.helper.label_class = 'col-sm-2 control-label'
	    self.helper.field_class = 'col-sm-10'

	        # add buttons
	    self.helper.layout[-1] = FormActions(
	        Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
	        Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
	    )    


class StudentUpdateView(UpdateView):
	model = Student
	template_name = 'students/students_edit.html'
	form_class = StudentUpdateForm
	def get_success_url(self):
		return u'%s?status_message=Студента успішно збережено!' % reverse('home')
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!' % reverse('home'))
		else:
			return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
	model = Student
	template_name = 'students/students_confirm_delete.html'
	def get_success_url(self):
		return u'%s?status_message=Студента успішно видалено!' % reverse('home')
