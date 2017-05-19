
import datetime

from django.db import models

from django.utils import timezone


class Question(models.Model):
	question_text = models.CharField(max_length=20)
	pub_date = models.DateTimeField('date publish')

	def __str__(self):
		return self.question_text

	def was_pulished_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_pulished_recently.admin_order_field = 'pub_date'	
	was_pulished_recently.boolean = True
	was_pulished_recently.short_description = 'Publish recently?'
		
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=20)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
