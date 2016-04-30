# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import mail_admins
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse_lazy,reverse
from datetime import datetime
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackForm
from django.conf import settings


class FeedbackView(CreateView):
	model = Feedback
	template_name = "feedback.html"
	success_url = reverse_lazy('feedback')
	form_class = FeedbackForm	

	def form_valid(self,form):
		feedback = form.save()
		mail_admins(feedback.subject, feedback.message, fail_silently=False)
		messages.success(self.request, u"Thank you for your feedback! We will keep in touch with you very soon!")
		return super(FeedbackView, self).form_valid(form)