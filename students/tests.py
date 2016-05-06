# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from students.models import Student


def student_create(stcount=1):
	for i in xrange(stcount):	
		student = Student.objects.create(
				name = 'Name{}'.format(i+1),
				surname = 'Surname{}'.format(i+1),
				date_of_birth = '2016-05-05',
				email = 'mail@mail.com'
				)
	return student	

class StudentsListTest(TestCase):
	'''
	Test student list page
	'''

	def test_student_list(self):
		client = Client()
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)

	def test_student_count(self):
		student_create(10)
		self.assertEqual(Student.objects.all().count(), 10)	

	def test_student_surname(self):
		student = student_create()
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, student.surname)

	def test_student_name(self):
		student = student_create()
		client = Client()
		response = client.get('/students/')
		self.assertContains(response, student.name)

	def test_link_add_student(self):
		response = self.client.get('/students/')
		self.assertContains(response, '/students/add/')	

	def test_link_edit_student(self):
		student = student_create()
		response = self.client.get('/students/')	
		self.assertContains(response, '/students/edit/1/')

	def test_link_delete_student(self):
		student = student_create()
		response = self.client.get('/students/')	
		self.assertContains(response, '/students/remove/1/')


class StudentsDetailTest(TestCase):
	'''
	Test student detail page
	'''

	def test_student_view(self):
		student = student_create()
		client = Client()
		response = client.get(reverse('students:detail', 
										args=(1,)))
		self.assertEqual(response.status_code, 200)

	def test_student_mail(self):
		student = student_create()
		client = Client()
		response = client.get(reverse('students:detail', 
										args=(1,)))
		self.assertContains(response, student.email)

	def test_student_phone(self):
		student = student_create()
		client = Client()
		response = client.get(reverse('students:detail', 
										args=(1,)))
		self.assertContains(response, student.phone)

	def test_student_address(self):
		student = student_create()
		client = Client()
		response = client.get(reverse('students:detail', 
									args=(1,)))
		self.assertContains(response, student.address)

	def test_student_skype(self):
		student = student_create()
		client = Client()
		response = client.get(reverse('students:detail', 
										args=(1,)))
		self.assertContains(response, student.skype)