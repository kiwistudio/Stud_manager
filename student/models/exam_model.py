# _*_ coding: utf-8 _*_ #

from django.db import models
 
# Create your models here.
class Exam(models.Model):
	"""Exam Model"""

	# Призначаємо user-friendly ім’я моделі іспитів в адмінці
	class Meta(object):
		verbose_name = u'іспит'
		verbose_name_plural = u"іспити"

	# Додаємо метод для гарного представлення Іспиту у shell та Django адмінці
	def __unicode__(self):
		return u"%s %s" % (self.subject, self.exam_group)
			

	subject = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва предмету")

	
	time_of_act = models.DateField(
		blank=False,
		verbose_name=u"Дата і час проведення",
		null=True)

	lecturer = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"им’я викладача")

	exam_group = models.ForeignKey('Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)
