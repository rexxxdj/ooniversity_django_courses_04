# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from students.models import Student


class StudentsListTest(TestCase):

	def test_course_list(self):
		'''
		Test student page
		'''
		client = Client()
		response = client.get('/students/')
		self.assertEqual(response.status_code, 200)


class StudentsDetailTest(TestCase):

    def test_student_view(self):
    	'''
    	Test for view student detail
    	'''
    	#Create student
    	student1 = Student.objects.create(
    		name = 'Name',
			surname = 'Surname',
			date_of_birth = '2016-05-05',
			email = 'mail@mail.com'
    		)
    	studentnum = 1 
       	#Проверка отображения страницы курса
        client = Client()
        response = client.get(reverse('students:detail', 
        								args=(studentnum,)))
        self.assertEqual(response.status_code, 200)

    def test_student_mail(self):
        student1 = Student.objects.create(
    		name = 'Name',
			surname = 'Surname',
			date_of_birth = '2016-05-05',
			email = 'mail@mail.com'
    		)
    	studentnum = 1 
       	#Проверка отображения страницы курса
        client = Client()
        response = client.get(reverse('students:detail', 
        								args=(studentnum,)))
        self.assertContains(response, student1.email)

    def test_student_phone(self):
        student1 = Student.objects.create(
    		name = 'Name',
			surname = 'Surname',
			date_of_birth = '2016-05-05',
			email = 'mail@mail.com',
			phone = '755-55-55'
    		)
    	studentnum = 1 
       	#Проверка отображения страницы курса
        client = Client()
        response = client.get(reverse('students:detail', 
        								args=(studentnum,)))
        self.assertContains(response, student1.phone)

    def test_student_address(self):
        student1 = Student.objects.create(
    		name = 'Name',
			surname = 'Surname',
			date_of_birth = '2016-05-05',
			email = 'mail@mail.com',
			address = 'Address'
    		)
    	studentnum = 1 
       	#Проверка отображения страницы курса
        client = Client()
        response = client.get(reverse('students:detail', 
        								args=(studentnum,)))
        self.assertContains(response, student1.address)

    def test_student_skype(self):
        student1 = Student.objects.create(
    		name = 'Name',
			surname = 'Surname',
			date_of_birth = '2016-05-05',
			email = 'mail@mail.com',
			skype = 'Skype'
    		)
    	studentnum = 1 
       	#Проверка отображения страницы курса
        client = Client()
        response = client.get(reverse('students:detail', 
        								args=(studentnum,)))
        self.assertContains(response, student1.skype)