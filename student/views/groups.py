# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView, CreateView
from django import forms
from django.forms import ModelForm
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


from ..models import Group

# Views for Groups
def groups_list(request):
	groups = Group.objects.all()

	# try to order groups list
	order_by = request.GET.get('order_by', '')
	if order_by in ('title', 'leader', 'id'):
		groups = groups.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			groups = groups.reverse()

	# paginate groups
	paginator = Paginator(groups, 5)
	page = request.GET.get('page')
	try:
		groups = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		groups = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver
	# last page of results.
		groups = paginator.page(paginator.num_pages)

	# add student left to paginator
	try:
		gr = paginator.count - (int(page) * 5)
		if gr < 0:
			gr_left = 0
		else:
			gr_left = gr
	except:
		gr_left = paginator.count - 1 * 5 


	return render(request, 'groups/groups_list.html', {'groups': groups, 'gr_left': gr_left})


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
	    super(GroupForm, self).__init__(*args, **kwargs)

	    self.helper = FormHelper(self)

	        # set form tag attributes
	    #self.helper.form_action = reverse('groups_edit', kwargs={'pk': kwargs['instance'].id})
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

class GroupAddView(CreateView):
    model = Group
    template_name = 'groups/groups_add.html'
    form_class = GroupForm

    def get_success_url(self):
        return u'%s?status_message=Групу успішно додано!' % reverse('groups')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
		    return HttpResponseRedirect(u'%s?status_message=Додавання групи відмінено!' % reverse('groups'))
        else:
			return super(GroupAddView, self).post(request, *args, **kwargs)

class GroupUpdateView(UpdateView):
	model = Group
	template_name = 'groups/groups_add.html'
	form_class = GroupForm

	def get_success_url(self):
		return u'%s?status_message=Групу успішно збережено!' % reverse('groups')

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=Редагування групи відмінено!' % reverse('groups'))
		else:
			return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDelete(DeleteView):
	model = Group
	template_name = 'groups/group_delete.html'
	def get_success_url(self):
		return u'%s?status_message=Групу успішно видалено!' % reverse('groups')
