# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from ..models import Exam


# Views for Students
def exam_list(request):
	exam = Exam.objects.all()

	# try to order exam list
	order_by = request.GET.get('order_by', '')
	if order_by in ('last_name', 'first_name', 'ticket', 'id'):
		exam = exam.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			exam = exam.reverse()

	# paginate exam
	paginator = Paginator(exam, 5)
	page = request.GET.get('page')
	try:
		exam = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		exam = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver
	# last page of results.
		exam = paginator.page(paginator.num_pages)
		
	# add student left to paginator
	try:
		ex = paginator.count - (int(page) * 5)
		if ex < 0:
			ex_left = 0
		else:
			ex_left = ex
	except:
		ex_left = paginator.count - 1 * 5 
	
	return render(request, 'exam/exam_list.html', {'exam': exam, 'ex_left': ex_left})

class ExamAddForm(ModelForm):

    class Meta:
        model = Exam
        fields = ['subject', 'time_of_act', 'lecturer', 'exam_group']

    def __init__(self, *args, **kwargs):
	    super(ExamAddForm, self).__init__(*args, **kwargs)

	    self.helper = FormHelper(self)

	        # set form tag attributes
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


def exam_add(request):
	if request.method == 'POST':
		form = ExamAddForm(request.POST)

		if form.is_valid():
			
			subject = form.cleaned_data['subject']
			time_of_act = form.cleaned_data['time_of_act']
			lecturer = form.cleaned_data['lecturer']
			exam_group = form.cleaned_data['exam_group']
			data = {'subject': subject, 'time_of_act': time_of_act, 'lecturer': lecturer, 'exam_group': exam_group}
			exam = Exam(**data)
			exam.save()
			return HttpResponseRedirect(
					u'%s?status_message=Іспит Додано' % reverse('exam'))

		else:
			return HttpResponseRedirect(
					u'%s?status_message=Додавання іспита скасовано' % reverse('exam'))

	else:
		form = ExamAddForm()

	return render(request, 'exam/exam_add.html', {'form': form})
