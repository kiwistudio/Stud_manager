# _*_ coding: utf-8 _*_ #

from django.db import models

class Group(models.Model):
	"""Group Model"""

	# Призначаємо user-friendly ім’я моделі групи в адмінці
	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Групи"

	# Додаємо метод для гарного представлення групи у shell та Django адмінці	
	def __unicode__(self):
		if self.leader:
			return u"%s (%s %s)" % (self.title, self.leader.first_name,
			self.leader.last_name)
		else:
			return u"%s" % (self.title,)			

	title = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва")

	leader = models.OneToOneField('Student',
		verbose_name=u"Староста",
		blank=True,
		null=True,
		on_delete=models.SET_NULL)
	
	notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")

	